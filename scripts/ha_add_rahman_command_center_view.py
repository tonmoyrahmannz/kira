import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
VIEW_TITLE = "Rahman's Command Centre"
VIEW_PATH = 'rahman-command-center'


def load_env(path: Path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"')
    return env


async def ws_call(ws, msg_id: int, payload: dict):
    await ws.send(json.dumps({'id': msg_id, **payload}))
    while True:
        data = json.loads(await ws.recv())
        if data.get('id') == msg_id:
            return data


def status_tile(name: str, icon: str, entity: str, color_template: str) -> dict:
    return {
        'type': 'custom:mushroom-template-card',
        'primary': name,
        'secondary': "{{ states('" + entity + "') }}",
        'entity': entity,
        'icon': icon,
        'layout': 'vertical',
        'fill_container': True,
        'multiline_secondary': False,
        'icon_color': color_template.strip(),
    }


def build_view() -> dict:
    infra_status = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Infrastructure Status', 'content': 'Executive one-glance status across core infrastructure.'},
            {
                'type': 'grid',
                'columns': 6,
                'square': False,
                'cards': [
                    status_tile('Home Assistant', 'mdi:home-assistant', 'sensor.system_monitor_processor_use', """
{% set s = states('sensor.system_monitor_processor_use') %}
{% if s in ['unknown','unavailable','none','None',''] %}amber
{% else %}{% set v=s|float(0) %}{% if v>90 %}red{% elif v>75 %}amber{% else %}green{% endif %}{% endif %}
"""),
                    status_tile('Mac Mini', 'mdi:monitor-dashboard', 'sensor.macmini_cpu_usage', """
{% set s = states('sensor.macmini_cpu_usage') %}
{% if s in ['unknown','unavailable','none','None',''] %}amber
{% else %}{% set v=s|float(0) %}{% if v>90 %}red{% elif v>75 %}amber{% else %}green{% endif %}{% endif %}
"""),
                    status_tile('NAS', 'mdi:nas', 'sensor.nas_total_usage', """
{% set online = states('binary_sensor.nas_online') %}
{% if online != 'on' %}red
{% else %}{% set v=states('sensor.nas_total_usage')|float(0) %}{% if v>90 %}red{% elif v>75 %}amber{% else %}green{% endif %}{% endif %}
"""),
                    status_tile('Omarchy', 'mdi:laptop', 'binary_sensor.omarchy_online', "{% set s=states('binary_sensor.omarchy_online') %}{% if s=='on' %}green{% elif s in ['unknown','unavailable'] %}amber{% else %}red{% endif %}"),
                    status_tile('Kira Gateway', 'mdi:robot-industrial', 'binary_sensor.kira_online', "{% set s=states('binary_sensor.kira_online') %}{% if s=='on' %}green{% elif s in ['unknown','unavailable'] %}amber{% else %}red{% endif %}"),
                    status_tile('Internet', 'mdi:web', 'sensor.internet_status', "{% set s=states('sensor.internet_status') %}{% if s=='online' %}green{% elif s=='degraded' %}amber{% elif s=='offline' %}red{% else %}amber{% endif %}"),
                ],
            },
        ],
    }

    infra_map = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Infrastructure Map', 'content': 'Topology-style operational map with live status markers.'},
            {
                'type': 'markdown',
                'content': """
{% macro dot(state, good='on') -%}
  {%- if state == good -%}🟢
  {%- elif state in ['unknown','unavailable','none','None',''] -%}🟠
  {%- else -%}🔴
  {%- endif -%}
{%- endmacro %}

{% set internet = states('sensor.internet_status') %}
{% set internet_dot = '🟢' if internet == 'online' else ('🟠' if internet == 'degraded' else '🔴') %}
{% set ha_dot = '🟢' if states('sensor.system_monitor_processor_use') not in ['unknown','unavailable'] else '🟠' %}
{% set mac_dot = '🟢' if states('sensor.macmini_cpu_usage') not in ['unknown','unavailable'] else '🟠' %}
{% set nas_dot = dot(states('binary_sensor.nas_online')) %}
{% set oma_dot = dot(states('binary_sensor.omarchy_online')) %}
{% set kira_dot = dot(states('binary_sensor.kira_openclaw_running')) %}
{% set gree_dot = '🟢' if states('climate.ac_master') not in ['unknown','unavailable'] else '🟠' %}
{% set blinds_dot = '🟢' if states('cover.study_blind') not in ['unknown','unavailable'] else '🟠' %}

```text
{{ internet_dot }} Internet
      |
🟢 Router
      |
{{ mac_dot }} Mac Mini
      |
{{ ha_dot }} Home Assistant
      |
------------------------------------------------
|            |              |                 |
{{ nas_dot }} NAS   {{ oma_dot }} Omarchy   {{ gree_dot }} Gree HVAC   {{ blinds_dot }} Neo Blinds
              |
       {{ kira_dot }} Kira / OpenClaw
```
""".strip(),
            },
        ],
    }

    services = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Critical Services', 'content': 'Service-layer health for automation, connectivity, and media services.'},
            {
                'type': 'grid',
                'columns': 3,
                'square': False,
                'cards': [
                    status_tile('OpenClaw', 'mdi:robot-industrial', 'binary_sensor.openclaw_service_online', "{% if is_state('binary_sensor.openclaw_service_online','on') %}green{% else %}red{% endif %}"),
                    status_tile('MQTT', 'mdi:transit-connection-variant', 'binary_sensor.mqtt_service_online', "{% if is_state('binary_sensor.mqtt_service_online','on') %}green{% else %}red{% endif %}"),
                    status_tile('Zigbee', 'mdi:zigbee', 'binary_sensor.zigbee_service_online', "{% if is_state('binary_sensor.zigbee_service_online','on') %}green{% else %}red{% endif %}"),
                    status_tile('Tuya', 'mdi:power-plug-outline', 'sensor.tuya_service_status', "{% set s=states('sensor.tuya_service_status') %}{% if s == 'online' %}green{% elif s == 'warning' %}amber{% else %}red{% endif %}"),
                    status_tile('Tailscale', 'mdi:relation-many-to-many', 'binary_sensor.tailscale_service_online', "{% if is_state('binary_sensor.tailscale_service_online','on') %}green{% else %}red{% endif %}"),
                    status_tile('Plex', 'mdi:plex', 'binary_sensor.plex_service_online', "{% if is_state('binary_sensor.plex_service_online','on') %}green{% else %}red{% endif %}"),
                ],
            },
        ],
    }

    attention = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Attention Needed', 'content': 'Visible only when operational issues require action.'},
            {
                'type': 'conditional',
                'conditions': [{'condition': 'state', 'entity': 'binary_sensor.kira_openclaw_running', 'state': 'off'}],
                'card': {'type': 'markdown', 'content': '🔴 **OpenClaw is not running** — self-recovery should attempt restart.'},
            },
            {
                'type': 'conditional',
                'conditions': [{'condition': 'state', 'entity': 'sensor.internet_status', 'state_not': 'online'}],
                'card': {'type': 'markdown', 'content': '🟠 **Internet is degraded/offline** — check WAN/router uplink.'},
            },
            {
                'type': 'conditional',
                'conditions': [{'condition': 'numeric_state', 'entity': 'sensor.nas_total_usage', 'above': 85}],
                'card': {'type': 'markdown', 'content': '🟠 **NAS storage high** — above 85% utilization.'},
            },
            {
                'type': 'conditional',
                'conditions': [{'condition': 'state', 'entity': 'update.home_assistant_core_update', 'state_not': 'off'}],
                'card': {'type': 'markdown', 'content': '🟠 **Home Assistant update available**.'},
            },
            {
                'type': 'conditional',
                'conditions': [
                    {'condition': 'state', 'entity': 'binary_sensor.kira_online', 'state': 'off'}
                ],
                'card': {'type': 'markdown', 'content': '🔴 **Kira Gateway offline** — check Omarchy connectivity.'},
            },
        ],
    }

    actions = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Operator Actions', 'content': 'Safe operational controls and links.'},
            {
                'type': 'grid',
                'columns': 5,
                'square': False,
                'cards': [
                    {
                        'type': 'button',
                        'name': 'Core Systems View',
                        'icon': 'mdi:view-dashboard',
                        'tap_action': {'action': 'navigate', 'navigation_path': '/rahman-command-centre'},
                    },
                    {
                        'type': 'button',
                        'name': 'Reload Automations',
                        'icon': 'mdi:reload-alert',
                        'tap_action': {'action': 'call-service', 'service': 'automation.reload'},
                    },
                    {
                        'type': 'button',
                        'name': 'Refresh View',
                        'icon': 'mdi:refresh',
                        'tap_action': {'action': 'navigate', 'navigation_path': '/rahman-command-centre/rahman-command-center'},
                    },
                    {
                        'type': 'button',
                        'name': 'Refresh Telemetry',
                        'icon': 'mdi:database-refresh',
                        'tap_action': {
                            'action': 'call-service',
                            'service': 'homeassistant.update_entity',
                            'target': {
                                'entity_id': [
                                    'sensor.macmini_cpu_usage',
                                    'sensor.nas_total_usage',
                                    'sensor.internet_status',
                                    'sensor.kira_last_heartbeat',
                                ]
                            },
                        },
                    },
                    {
                        'type': 'button',
                        'name': 'Service Layer View',
                        'icon': 'mdi:server-network',
                        'tap_action': {'action': 'navigate', 'navigation_path': '/rahman-command-centre/service-detail'},
                    },
                ],
            },
        ],
    }

    return {
        'title': VIEW_TITLE,
        'path': VIEW_PATH,
        'icon': 'mdi:monitor-dashboard',
        'type': 'sections',
        'max_columns': 2,
        'sections': [
            {'type': 'grid', 'cards': [infra_status]},
            {'type': 'grid', 'cards': [infra_map]},
            {'type': 'grid', 'cards': [services]},
            {'type': 'grid', 'cards': [attention]},
            {'type': 'grid', 'cards': [actions]},
        ],
        'badges': [],
    }


def build_service_detail_view() -> dict:
    return {
        'title': 'Service Detail',
        'path': 'service-detail',
        'icon': 'mdi:server-network',
        'type': 'sections',
        'max_columns': 2,
        'sections': [
            {
                'type': 'grid',
                'cards': [
                    {
                        'type': 'markdown',
                        'title': 'Critical Services Detail',
                        'content': 'Operational health for automation and network services.',
                    },
                    {
                        'type': 'grid',
                        'columns': 2,
                        'square': False,
                        'cards': [
                            {'type': 'entity', 'entity': 'binary_sensor.openclaw_service_online', 'name': 'OpenClaw Gateway'},
                            {'type': 'entity', 'entity': 'binary_sensor.mqtt_service_online', 'name': 'MQTT Broker'},
                            {'type': 'entity', 'entity': 'binary_sensor.zigbee_service_online', 'name': 'Zigbee Service'},
                            {'type': 'entity', 'entity': 'binary_sensor.tailscale_service_online', 'name': 'Tailscale VPN'},
                            {'type': 'entity', 'entity': 'binary_sensor.plex_service_online', 'name': 'Plex Media Server'},
                            {'type': 'entity', 'entity': 'sensor.zigbee_unavailable_device_count', 'name': 'Zigbee Unavailable Devices'},
                            {'type': 'entity', 'entity': 'sensor.mqtt_telemetry_freshness', 'name': 'MQTT Telemetry Freshness'},
                        ],
                    },
                ],
            },
            {
                'type': 'grid',
                'cards': [
                    {
                        'type': 'markdown',
                        'title': 'Tuya Service Health',
                        'content': 'Detailed health and inventory for Tuya integration and LAN gateway.',
                    },
                    {
                        'type': 'grid',
                        'columns': 2,
                        'square': False,
                        'cards': [
                            {'type': 'entity', 'entity': 'binary_sensor.tuya_integration_connected', 'name': 'Connection Status'},
                            {'type': 'entity', 'entity': 'binary_sensor.tuya_gateway_reachable', 'name': 'Gateway Reachable (192.168.50.100)'},
                            {'type': 'entity', 'entity': 'sensor.tuya_device_count', 'name': 'Total Tuya Devices'},
                            {'type': 'entity', 'entity': 'sensor.tuya_unavailable_device_count', 'name': 'Unavailable Tuya Devices'},
                            {'type': 'entity', 'entity': 'sensor.tuya_last_update', 'name': 'Last Update'},
                            {'type': 'entity', 'entity': 'sensor.tuya_service_status', 'name': 'Overall Tuya Status'},
                        ],
                    },
                    {
                        'type': 'conditional',
                        'conditions': [{'condition': 'numeric_state', 'entity': 'sensor.tuya_unavailable_device_count', 'above': 0}],
                        'card': {
                            'type': 'markdown',
                            'content': '🟠 **Warning:** One or more Tuya devices are unavailable. Check Tuya cloud session and LAN gateway power/network.',
                        },
                    },
                    {
                        'type': 'conditional',
                        'conditions': [{'condition': 'state', 'entity': 'binary_sensor.tuya_gateway_reachable', 'state': 'off'}],
                        'card': {
                            'type': 'markdown',
                            'content': '🔴 **Gateway unreachable:** Tuya Zigbee LAN gateway ping failed at `192.168.50.100`.',
                        },
                    },
                ],
            }
        ],
        'badges': [],
    }


async def main():
    env = load_env(ENV_PATH)
    ws_url = env['HA_URL'].rstrip('/').replace('http://', 'ws://').replace('https://', 'wss://') + '/api/websocket'
    token = env['HA_TOKEN']

    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5) as ws:
        hello = json.loads(await ws.recv())
        if hello.get('type') != 'auth_required':
            raise RuntimeError(f'Unexpected hello: {hello}')

        await ws.send(json.dumps({'type': 'auth', 'access_token': token}))
        auth = json.loads(await ws.recv())
        if auth.get('type') != 'auth_ok':
            raise RuntimeError(f'Auth failed: {auth}')

        current = await ws_call(ws, 1, {'type': 'lovelace/config', 'url_path': DASHBOARD_URL_PATH})
        if not current.get('success'):
            raise RuntimeError(f"Cannot load dashboard config: {current.get('error')}")

        config = current['result']
        views = config.get('views', [])
        new_main_view = build_view()
        new_service_view = build_service_detail_view()

        replaced_main = False
        replaced_service = False

        for i, view in enumerate(views):
            if view.get('title') == VIEW_TITLE or view.get('path') == VIEW_PATH:
                views[i] = new_main_view
                replaced_main = True
            elif view.get('title') == 'Service Detail' or view.get('path') == 'service-detail':
                views[i] = new_service_view
                replaced_service = True

        if not replaced_main:
            views.append(new_main_view)
        if not replaced_service:
            views.append(new_service_view)

        config['views'] = views

        save_resp = await ws_call(ws, 2, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': config,
        })

        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        print(json.dumps({
            'ok': True,
            'dashboard': DASHBOARD_URL_PATH,
            'main_view': VIEW_TITLE,
            'main_view_replaced': replaced_main,
            'service_view_replaced': replaced_service,
            'total_views_after_save': len(views),
            'requires_custom_cards': ['custom:mushroom-template-card'],
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

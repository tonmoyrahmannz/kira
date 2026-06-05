import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
VIEW_TITLE = 'Service Detail'
VIEW_PATH = 'service-detail'
RCC_PATH = 'rahman-command-center'


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


def service_tile(name: str, icon: str, entity: str) -> dict:
    return {
        'type': 'custom:mushroom-template-card',
        'primary': name,
        'secondary': "{{ states('" + entity + "') }}",
        'entity': entity,
        'icon': icon,
        'layout': 'vertical',
        'fill_container': True,
        'multiline_secondary': False,
        'icon_color': (
            "{% set s = states('" + entity + "') %}"
            "{% if s in ['on','online','running'] %}green"
            "{% elif s in ['unknown','unavailable','none','None',''] %}amber"
            "{% else %}red{% endif %}"
        ),
    }


def build_view() -> dict:
    summary = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Service Summary', 'content': 'Operational drill-down for service layer monitoring.'},
            {
                'type': 'grid',
                'columns': 5,
                'square': False,
                'cards': [
                    service_tile('OpenClaw', 'mdi:robot-industrial', 'binary_sensor.openclaw_service_online'),
                    service_tile('Tailscale', 'mdi:relation-many-to-many', 'binary_sensor.tailscale_service_online'),
                    service_tile('MQTT', 'mdi:transit-connection-variant', 'binary_sensor.mqtt_service_online'),
                    service_tile('Zigbee', 'mdi:zigbee', 'binary_sensor.zigbee_service_online'),
                    service_tile('Plex', 'mdi:plex', 'binary_sensor.plex_service_online'),
                ],
            },
        ],
    }

    openclaw = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'OpenClaw — Omarchy Host', 'content': 'Gateway process state and self-recovery telemetry.'},
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    {'entity': 'binary_sensor.openclaw_service_online', 'name': 'Service Online'},
                    {'entity': 'binary_sensor.kira_openclaw_running', 'name': 'Process Running'},
                    {'entity': 'sensor.kira_openclaw_pid', 'name': 'Process ID'},
                    {'entity': 'sensor.kira_openclaw_memory_mb', 'name': 'Memory Usage (MB)'},
                    {'entity': 'sensor.kira_cpu_usage', 'name': 'CPU Usage (%)'},
                    {'entity': 'sensor.kira_last_heartbeat', 'name': 'Last Heartbeat'},
                    {'entity': 'input_datetime.openclaw_last_auto_recovery', 'name': 'Last Auto-Restart'},
                ],
            },
            {
                'type': 'markdown',
                'content': """
**Recovery Cooldown Guard (10 min):**
{% set last = states('input_datetime.openclaw_last_auto_recovery') %}
{% if last in ['unknown','unavailable','none','None',''] %}
🟠 No recovery timestamp recorded yet.
{% else %}
{% set age = (as_timestamp(now()) - as_timestamp(last, 0)) / 60 %}
{% if age < 10 %}
🟠 Cooldown active — automatic restart suppression is enabled ({{ age|round(1) }} min since last restart).
{% else %}
🟢 Cooldown clear — eligible for auto-recovery if needed.
{% endif %}
{% endif %}
""".strip(),
            },
        ],
    }

    tailscale = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Tailscale', 'content': 'Remote connectivity state for Omarchy and overlay network.'},
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    {'entity': 'binary_sensor.tailscale_service_online', 'name': 'Tailscale Connected'},
                    {'entity': 'binary_sensor.omarchy_tailscale_connected', 'name': 'Omarchy Tailscale Link'},
                    {'entity': 'sensor.omarchy_last_seen', 'name': 'Omarchy Last Seen'},
                    {'entity': 'binary_sensor.omarchy_online', 'name': 'Omarchy Reachable from HA'},
                ],
            },
        ],
    }

    mqtt = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'MQTT Broker', 'content': 'Broker reachability and telemetry freshness indicators.'},
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    {'entity': 'binary_sensor.mqtt_service_online', 'name': 'Broker Online (Port 1883)'},
                    {'entity': 'sensor.mqtt_service_status', 'name': 'Broker Status Label'},
                    {'entity': 'sensor.mqtt_last_probe_age_seconds', 'name': 'Last Probe Age (s)'},
                    {'entity': 'sensor.mqtt_telemetry_freshness', 'name': 'Telemetry Freshness'},
                ],
            },
        ],
    }

    zigbee = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Zigbee Network (Tuya Cloud Bridge)', 'content': 'Gateway reachability and Zigbee service state.'},
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    {'entity': 'binary_sensor.zigbee_service_online', 'name': 'Zigbee Service Online'},
                    {'entity': 'binary_sensor.192_168_50_100', 'name': 'Tuya Zigbee Gateway Reachable'},
                    {'entity': 'sensor.zigbee_service_status', 'name': 'Zigbee Status Label'},
                ],
            },
            {
                'type': 'markdown',
                'content': """
{% set zigbee_entities = (integration_entities('zha') + integration_entities('z2m') + integration_entities('zigbee2mqtt')) | unique | list %}

{% set ns_unavail = namespace(ids=[]) %}
{% for entity_id in zigbee_entities %}
  {% if states(entity_id) == 'unavailable' %}
    {% set obj = entity_id.split('.')[1] %}
    {% if obj not in ns_unavail.ids %}
      {% set ns_unavail.ids = ns_unavail.ids + [obj] %}
    {% endif %}
  {% endif %}
{% endfor %}
{% set unavailable = ns_unavail.ids | count %}

{% set ns_batt = namespace(ids=[]) %}
{% for entity_id in zigbee_entities %}
  {% set domain = entity_id.split('.')[0] %}
  {% set object_id = entity_id.split('.')[1] %}
  {% set state = states(entity_id) %}
  {% set low_percent = ('battery' in object_id and domain == 'sensor' and is_number(state) and (state | float(101)) <= 20) %}
  {% set low_flag = (('battery_low' in object_id or 'low_battery' in object_id) and domain == 'binary_sensor' and state == 'on') %}
  {% if low_percent or low_flag %}
    {% set device_key = object_id | replace('_battery_low','') | replace('_low_battery','') | replace('_battery','') | replace('battery_','') %}
    {% if device_key not in ns_batt.ids %}
      {% set ns_batt.ids = ns_batt.ids + [device_key] %}
    {% endif %}
  {% endif %}
{% endfor %}
{% set battery = ns_batt.ids | count %}

- **Unavailable Device Count:** {{ unavailable }}
- **Battery Warning Count (≤20% / battery_low):** {{ battery }}

{% if unavailable == 0 and battery == 0 %}
🟢 Zigbee fleet healthy.
{% else %}
🟠 Zigbee needs attention.
{% endif %}
""".strip(),
            },
        ],
    }

    plex = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Plex (NAS)', 'content': 'Plex endpoint and media service availability.'},
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    {'entity': 'binary_sensor.plex_service_online', 'name': 'Plex Port 32400 Reachable'},
                    {'entity': 'sensor.plex_service_status', 'name': 'Plex Status Label'},
                ],
            },
            {
                'type': 'markdown',
                'content': 'Active stream/session count is not yet wired as a sensor (placeholder for next phase).',
            },
        ],
    }

    events = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Recent Service Events / Alerts', 'content': 'Recent logbook activity for service-layer troubleshooting.'},
            {
                'type': 'logbook',
                'hours_to_show': 24,
                'entities': [
                    'binary_sensor.kira_openclaw_running',
                    'binary_sensor.openclaw_service_online',
                    'binary_sensor.tailscale_service_online',
                    'binary_sensor.mqtt_service_online',
                    'binary_sensor.zigbee_service_online',
                    'binary_sensor.plex_service_online',
                ],
            },
        ],
    }

    actions = {
        'type': 'vertical-stack',
        'cards': [
            {'type': 'markdown', 'title': 'Operator Actions', 'content': 'Safe controls and quick navigation.'},
            {
                'type': 'grid',
                'columns': 4,
                'square': False,
                'cards': [
                    {
                        'type': 'button',
                        'name': "Back to Command Centre",
                        'icon': 'mdi:monitor-dashboard',
                        'tap_action': {'action': 'navigate', 'navigation_path': '/rahman-command-centre/rahman-command-center'},
                    },
                    {
                        'type': 'button',
                        'name': 'Go to Core Systems',
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
                        'name': 'Refresh This View',
                        'icon': 'mdi:refresh',
                        'tap_action': {'action': 'navigate', 'navigation_path': '/rahman-command-centre/service-detail'},
                    },
                ],
            },
        ],
    }

    return {
        'title': VIEW_TITLE,
        'path': VIEW_PATH,
        'icon': 'mdi:server-network',
        'type': 'sections',
        'max_columns': 2,
        'sections': [
            {'type': 'grid', 'cards': [summary]},
            {'type': 'grid', 'cards': [openclaw, tailscale]},
            {'type': 'grid', 'cards': [mqtt, zigbee]},
            {'type': 'grid', 'cards': [plex, events]},
            {'type': 'grid', 'cards': [actions]},
        ],
        'badges': [],
    }


def update_rcc_services_button(view: dict) -> bool:
    """Set Service Layer button destination to service-detail path."""
    changed = False
    if view.get('path') != RCC_PATH:
        return changed

    sections = view.get('sections', [])
    for sec in sections:
        for card in sec.get('cards', []):
            if isinstance(card, dict) and card.get('type') == 'vertical-stack':
                for sc in card.get('cards', []):
                    if isinstance(sc, dict) and sc.get('type') == 'grid':
                        for btn in sc.get('cards', []):
                            if isinstance(btn, dict) and btn.get('type') == 'button' and btn.get('name') == 'Service Layer View':
                                tap = btn.get('tap_action', {})
                                if tap.get('action') == 'navigate' and tap.get('navigation_path') != '/rahman-command-centre/service-detail':
                                    tap['navigation_path'] = '/rahman-command-centre/service-detail'
                                    btn['tap_action'] = tap
                                    changed = True
    return changed


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
        new_view = build_view()

        replaced = False
        for i, view in enumerate(views):
            if view.get('title') == VIEW_TITLE or view.get('path') == VIEW_PATH:
                views[i] = new_view
                replaced = True
            else:
                update_rcc_services_button(view)

        if not replaced:
            views.append(new_view)

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
            'view': VIEW_TITLE,
            'view_replaced': replaced,
            'total_views_after_save': len(views),
            'requires_custom_cards': ['custom:mushroom-template-card'],
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

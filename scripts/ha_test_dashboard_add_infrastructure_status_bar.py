import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
CARD_TITLE = 'Infrastructure Status'


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


def tile(name: str, icon: str, entity: str, icon_color_template: str) -> dict:
    return {
        'type': 'custom:mushroom-template-card',
        'primary': name,
        'secondary': "{{ states('" + entity + "') }}",
        'icon': icon,
        'entity': entity,
        'layout': 'vertical',
        'fill_container': True,
        'multiline_secondary': False,
        'icon_color': icon_color_template,
    }


def build_infra_status_card() -> dict:
    tiles = [
        tile(
            'Home Assistant',
            'mdi:home-assistant',
            'sensor.system_monitor_processor_use',
            """
{% set s = states('sensor.system_monitor_processor_use') %}
{% if s in ['unknown','unavailable','none','None',''] %}amber
{% else %}
  {% set v = s|float(0) %}
  {% if v > 90 %}red
  {% elif v > 75 %}amber
  {% else %}green
  {% endif %}
{% endif %}
""".strip(),
        ),
        tile(
            'MacMini',
            'mdi:monitor-dashboard',
            'sensor.macmini_cpu_usage',
            """
{% set s = states('sensor.macmini_cpu_usage') %}
{% if s in ['unknown','unavailable','none','None',''] %}amber
{% else %}
  {% set v = s|float(0) %}
  {% if v > 90 %}red
  {% elif v > 75 %}amber
  {% else %}green
  {% endif %}
{% endif %}
""".strip(),
        ),
        tile(
            'NAS',
            'mdi:nas',
            'sensor.nas_total_usage',
            """
{% set online = states('binary_sensor.nas_online') %}
{% set s = states('sensor.nas_total_usage') %}
{% if online in ['unknown','unavailable','none','None',''] %}amber
{% elif online != 'on' %}red
{% elif s in ['unknown','unavailable','none','None',''] %}amber
{% else %}
  {% set v = s|float(0) %}
  {% if v > 90 %}red
  {% elif v > 75 %}amber
  {% else %}green
  {% endif %}
{% endif %}
""".strip(),
        ),
        tile(
            'Omarchy',
            'mdi:laptop',
            'binary_sensor.omarchy_online',
            """
{% set s = states('binary_sensor.omarchy_online') %}
{% if s == 'on' %}green
{% elif s in ['unknown','unavailable','none','None',''] %}amber
{% else %}red
{% endif %}
""".strip(),
        ),
        tile(
            'Kira Gateway',
            'mdi:robot-industrial',
            'binary_sensor.kira_online',
            """
{% set s = states('binary_sensor.kira_online') %}
{% if s == 'on' %}green
{% elif s in ['unknown','unavailable','none','None',''] %}amber
{% else %}red
{% endif %}
""".strip(),
        ),
        tile(
            'Internet',
            'mdi:web',
            'sensor.internet_status',
            """
{% set s = states('sensor.internet_status') %}
{% if s == 'online' %}green
{% elif s == 'degraded' %}amber
{% elif s == 'offline' %}red
{% else %}amber
{% endif %}
""".strip(),
        ),
    ]

    return {
        'type': 'vertical-stack',
        'cards': [
            {
                'type': 'markdown',
                'title': CARD_TITLE,
                'content': 'Single-glance operational health for core infrastructure.',
            },
            {
                'type': 'grid',
                'columns': 6,
                'square': False,
                'cards': tiles,
            },
        ],
    }


def is_infra_status_card(card: dict) -> bool:
    return (
        isinstance(card, dict)
        and card.get('type') == 'vertical-stack'
        and isinstance(card.get('cards'), list)
        and any(
            isinstance(sc, dict)
            and sc.get('type') == 'markdown'
            and sc.get('title') == CARD_TITLE
            for sc in card.get('cards', [])
        )
    )


def upsert_first(view: dict, infra_card: dict):
    if view.get('type') == 'sections':
        sections = view.get('sections', [])
        if not sections:
            sections = [{'type': 'grid', 'cards': []}]
            view['sections'] = sections

        first = sections[0]
        cards = first.get('cards', [])
        cards = [c for c in cards if not is_infra_status_card(c)]
        cards.insert(0, infra_card)
        first['cards'] = cards
        sections[0] = first
        view['sections'] = sections
        return len(cards)

    cards = view.get('cards', [])
    cards = [c for c in cards if not is_infra_status_card(c)]
    cards.insert(0, infra_card)
    view['cards'] = cards
    return len(cards)


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

        cfg_resp = await ws_call(ws, 1, {'type': 'lovelace/config', 'url_path': DASHBOARD_URL_PATH})
        if not cfg_resp.get('success'):
            raise RuntimeError(f"Cannot load dashboard {DASHBOARD_URL_PATH}: {cfg_resp.get('error')}")

        cfg = cfg_resp['result']
        views = cfg.get('views', [])
        if not views:
            raise RuntimeError('Dashboard has no views')

        view = views[0]
        infra = build_infra_status_card()
        card_count = upsert_first(view, infra)
        views[0] = view
        cfg['views'] = views

        save_resp = await ws_call(ws, 2, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': cfg,
        })
        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        print(json.dumps({
            'ok': True,
            'dashboard': DASHBOARD_URL_PATH,
            'inserted': CARD_TITLE,
            'cards_in_first_container': card_count,
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

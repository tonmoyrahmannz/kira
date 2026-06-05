import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
SECTION_TITLE = 'Services'


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


def build_services_section() -> dict:
    cards = [
        {
            'type': 'markdown',
            'title': SECTION_TITLE,
            'content': 'Application and service-layer availability.',
        },
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
    ]

    return {'type': 'grid', 'cards': cards}


def is_services_section(section: dict) -> bool:
    if section.get('type') != 'grid':
        return False
    cards = section.get('cards', [])
    if not cards:
        return False
    first = cards[0]
    return (
        isinstance(first, dict)
        and first.get('type') == 'markdown'
        and first.get('title') == SECTION_TITLE
    )


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
        if view.get('type') != 'sections':
            raise RuntimeError('Expected sections-style dashboard view')

        sections = [s for s in view.get('sections', []) if not is_services_section(s)]
        sections.append(build_services_section())

        view['sections'] = sections
        views[0] = view
        cfg['views'] = views

        save_resp = await ws_call(ws, 2, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': cfg,
        })
        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        print(json.dumps({'ok': True, 'section': SECTION_TITLE, 'sections': len(sections)}, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

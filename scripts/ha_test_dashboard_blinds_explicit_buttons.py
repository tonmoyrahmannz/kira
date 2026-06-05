import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'

BLINDS = [
    ('cover.dining_blind_1', 'Dining Blind 1'),
    ('cover.dining_blind_2_3', 'Dining Blind 2'),
    ('cover.living_room_blind', 'Living Room Blind'),
    ('cover.master_bedroom_blind', 'Master Bedroom Blind'),
    ('cover.sophie_s_blind', "Sophie's Blind"),
    ('cover.study_blind', 'Study Blind'),
]


def load_env(path: Path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"')
    return env


def build_explicit_control_cards():
    cards = []
    for entity_id, name in BLINDS:
        cards.append({
            'type': 'horizontal-stack',
            'cards': [
                {
                    'type': 'button',
                    'name': f'{name} Open',
                    'icon': 'mdi:arrow-up-bold-circle',
                    'tap_action': {
                        'action': 'call-service',
                        'service': 'cover.open_cover',
                        'target': {'entity_id': entity_id},
                    },
                },
                {
                    'type': 'button',
                    'name': f'{name} Close',
                    'icon': 'mdi:arrow-down-bold-circle',
                    'tap_action': {
                        'action': 'call-service',
                        'service': 'cover.close_cover',
                        'target': {'entity_id': entity_id},
                    },
                },
            ],
        })
    return {
        'type': 'vertical-stack',
        'title': 'Blinds (Explicit Controls)',
        'cards': cards,
    }


async def ws_call(ws, msg_id: int, payload: dict):
    await ws.send(json.dumps({'id': msg_id, **payload}))
    data = json.loads(await ws.recv())
    if data.get('id') != msg_id:
        raise RuntimeError(f'Unexpected response id: {data}')
    return data


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

        main_view = views[0]
        cards = main_view.get('cards', [])

        # Remove existing explicit control block if present (idempotent)
        cards = [
            c for c in cards
            if not (isinstance(c, dict) and c.get('type') == 'vertical-stack' and c.get('title') == 'Blinds (Explicit Controls)')
        ]

        cards.insert(1, build_explicit_control_cards())

        main_view['cards'] = cards
        views[0] = main_view
        cfg['views'] = views

        save_resp = await ws_call(ws, 2, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': cfg,
        })
        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        print(json.dumps({'ok': True, 'dashboard': DASHBOARD_URL_PATH, 'inserted': 'Blinds (Explicit Controls)'}, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import requests
import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'

BROKEN_AUTOMATIONS = [
    'automation.alexa_sync_dining_blind_1',
    'automation.alexa_sync_dining_blind_2',
    'automation.alexa_sync_living_room_blind',
    'automation.alexa_sync_master_bedroom_blind',
    'automation.alexa_sync_sophie_s_blind',
    'automation.alexa_sync_study_blind',
]

BLIND_ENTITIES = [
    'cover.dining_blind_1',
    'cover.dining_blind_2_3',
    'cover.living_room_blind',
    'cover.master_bedroom_blind',
    'cover.sophie_s_blind',
    'cover.study_blind',
]

DASHBOARD_URL_PATH = 'rahman-command-centre'
REFRESH_CARD = {
    'type': 'button',
    'name': 'Refresh Blind Status',
    'icon': 'mdi:refresh',
    'tap_action': {
        'action': 'call-service',
        'service': 'homeassistant.update_entity',
        'target': {'entity_id': BLIND_ENTITIES},
    },
}


def load_env(path: Path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"')
    return env


def call_service(ha_url: str, token: str, domain: str, service: str, body: dict):
    r = requests.post(
        f"{ha_url.rstrip('/')}/api/services/{domain}/{service}",
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        json=body,
        timeout=20,
    )
    r.raise_for_status()
    return r.json()


async def ws_call(ws, msg_id: int, payload: dict):
    await ws.send(json.dumps({'id': msg_id, **payload}))
    data = json.loads(await ws.recv())
    if data.get('id') != msg_id:
        raise RuntimeError(f'Unexpected response id: {data}')
    return data


async def ensure_refresh_button(ha_url: str, token: str):
    ws_url = ha_url.rstrip('/').replace('http://', 'ws://').replace('https://', 'wss://') + '/api/websocket'

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
            return {'updated': False, 'reason': 'no_views'}

        target_view = views[0]  # existing main HVAC view
        cards = target_view.get('cards', [])

        already = any(
            isinstance(c, dict)
            and c.get('type') == 'button'
            and c.get('tap_action', {}).get('service') == 'homeassistant.update_entity'
            and c.get('name') == 'Refresh Blind Status'
            for c in cards
        )

        if already:
            return {'updated': False, 'reason': 'already_present'}

        cards.insert(0, REFRESH_CARD)
        target_view['cards'] = cards
        views[0] = target_view
        cfg['views'] = views

        save_resp = await ws_call(ws, 2, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': cfg,
        })
        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        return {'updated': True, 'reason': 'inserted'}


def main():
    env = load_env(ENV_PATH)
    ha_url = env['HA_URL']
    token = env['HA_TOKEN']

    off_res = call_service(
        ha_url,
        token,
        'automation',
        'turn_off',
        {'entity_id': BROKEN_AUTOMATIONS, 'stop_actions': True},
    )

    refresh_once = call_service(
        ha_url,
        token,
        'homeassistant',
        'update_entity',
        {'entity_id': BLIND_ENTITIES},
    )

    dash_res = asyncio.run(ensure_refresh_button(ha_url, token))

    print(json.dumps({
        'ok': True,
        'disabled_automations': len(off_res),
        'manual_refresh_called': True,
        'dashboard_refresh_button': dash_res,
    }, indent=2))


if __name__ == '__main__':
    main()

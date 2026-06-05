import asyncio
import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import requests
import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
VIEW_TITLE = 'All Entities'


def load_env(path: Path):
    env = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"')
    return env


def get_entities(ha_url: str, token: str):
    resp = requests.get(
        f"{ha_url.rstrip('/')}/api/states",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=20,
    )
    resp.raise_for_status()
    states = resp.json()

    # Sort and group by domain
    grouped = defaultdict(list)
    for s in states:
        eid = s.get('entity_id')
        if not eid or '.' not in eid:
            continue
        domain = eid.split('.', 1)[0]
        grouped[domain].append(eid)

    for domain in grouped:
        grouped[domain] = sorted(grouped[domain])

    return dict(sorted(grouped.items(), key=lambda kv: kv[0]))


def build_view(grouped_entities: dict):
    cards = []
    total = 0
    for domain, entities in grouped_entities.items():
        if not entities:
            continue
        total += len(entities)
        cards.append({
            'type': 'entities',
            'title': f'{domain} ({len(entities)})',
            'show_header_toggle': False,
            'entities': entities,
        })

    view = {
        'title': VIEW_TITLE,
        'path': 'all-entities',
        'icon': 'mdi:format-list-bulleted-square',
        'type': 'masonry',
        'cards': cards,
        'badges': [],
    }
    return view, total


async def ws_call(ws, msg_id: int, payload: dict):
    payload = {'id': msg_id, **payload}
    await ws.send(json.dumps(payload))
    raw = await ws.recv()
    data = json.loads(raw)
    if data.get('id') != msg_id:
        raise RuntimeError(f'Unexpected WS response id: {data}')
    return data


async def save_dashboard(ha_url: str, token: str, new_view: dict):
    ws_url = ha_url.rstrip('/').replace('http://', 'ws://').replace('https://', 'wss://') + '/api/websocket'

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

        replaced = False
        for i, view in enumerate(views):
            if view.get('title') == VIEW_TITLE or view.get('path') == 'all-entities':
                views[i] = new_view
                replaced = True
                break

        if not replaced:
            views.append(new_view)

        config['views'] = views

        save_resp = await ws_call(
            ws,
            2,
            {
                'type': 'lovelace/config/save',
                'url_path': DASHBOARD_URL_PATH,
                'config': config,
            },
        )

        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        return replaced, len(views)


def main():
    env = load_env(ENV_PATH)
    ha_url = env['HA_URL']
    token = env['HA_TOKEN']

    grouped = get_entities(ha_url, token)
    new_view, total_entities = build_view(grouped)

    replaced, total_views = asyncio.run(save_dashboard(ha_url, token, new_view))

    print(json.dumps({
        'ok': True,
        'dashboard': DASHBOARD_URL_PATH,
        'view_title': VIEW_TITLE,
        'view_replaced': replaced,
        'domains': len(grouped),
        'entities': total_entities,
        'total_views_after_save': total_views,
    }, indent=2))


if __name__ == '__main__':
    main()

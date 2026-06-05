import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
MAC_CARD_TITLE = 'MacMini Health'
NAS_CARD_TITLE = 'NAS Overview'


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


def _is_target_stack(card: dict, title: str) -> bool:
    return (
        isinstance(card, dict)
        and card.get('type') == 'vertical-stack'
        and isinstance(card.get('cards'), list)
        and any(
            isinstance(sc, dict)
            and sc.get('type') == 'markdown'
            and sc.get('title') == title
            for sc in card.get('cards', [])
        )
    )


def build_macmini_card() -> dict:
    return {
        'type': 'vertical-stack',
        'cards': [
            {
                'type': 'markdown',
                'title': MAC_CARD_TITLE,
                'content': 'Live MacMini stats (CPU/GPU/Memory/Storage).',
            },
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    'sensor.macmini_cpu_usage',
                    'sensor.macmini_gpu_usage',
                    'sensor.macmini_memory_usage',
                    'sensor.macmini_storage_usage',
                ],
            },
        ],
    }


def build_nas_card() -> dict:
    pie_markdown = """
{% set media = states('sensor.nas_media_usage_percent')|float(0) %}
{% set docs = states('sensor.nas_documents_usage_percent')|float(0) %}
{% set backups = states('sensor.nas_backups_usage_percent')|float(0) %}
{% set archive = states('sensor.nas_archive_usage_percent')|float(0) %}
{% set other = [100 - media - docs - backups - archive, 0]|max %}

<div style="display:flex; gap:16px; align-items:center; flex-wrap: wrap;">
  <div style="width:140px; height:140px; border-radius:50%; background:
    conic-gradient(
      #4caf50 0 {{ media }}%,
      #2196f3 {{ media }}% {{ media + docs }}%,
      #ff9800 {{ media + docs }}% {{ media + docs + backups }}%,
      #9c27b0 {{ media + docs + backups }}% {{ media + docs + backups + archive }}%,
      #9e9e9e {{ media + docs + backups + archive }}% 100%
    );">
  </div>
  <div>
    <div>🟢 Media: {{ media }}%</div>
    <div>🔵 Documents: {{ docs }}%</div>
    <div>🟠 Backups: {{ backups }}%</div>
    <div>🟣 Archive: {{ archive }}%</div>
    <div>⚪ Other: {{ other|round(1) }}%</div>
  </div>
</div>
""".strip()

    return {
        'type': 'vertical-stack',
        'cards': [
            {
                'type': 'markdown',
                'title': NAS_CARD_TITLE,
                'content': 'NAS online status and storage split by category.',
            },
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': [
                    'binary_sensor.nas_online',
                    'sensor.nas_total_usage',
                    'sensor.nas_media_usage_percent',
                    'sensor.nas_documents_usage_percent',
                    'sensor.nas_backups_usage_percent',
                    'sensor.nas_archive_usage_percent',
                ],
            },
            {
                'type': 'markdown',
                'title': 'NAS Category Usage (Pie)',
                'content': pie_markdown,
            },
        ],
    }


def upsert_cards(view: dict, cards_to_add: list[dict]):
    if view.get('type') == 'sections':
        sections = view.get('sections', [])
        if not sections:
            sections = [{'type': 'grid', 'cards': []}]
            view['sections'] = sections

        first = sections[0]
        cards = first.get('cards', [])
        cards = [
            c for c in cards
            if not (_is_target_stack(c, MAC_CARD_TITLE) or _is_target_stack(c, NAS_CARD_TITLE))
        ]
        cards.extend(cards_to_add)
        first['cards'] = cards
        sections[0] = first
        view['sections'] = sections
        return len(cards)

    cards = view.get('cards', [])
    cards = [
        c for c in cards
        if not (_is_target_stack(c, MAC_CARD_TITLE) or _is_target_stack(c, NAS_CARD_TITLE))
    ]
    cards.extend(cards_to_add)
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

        target_view = views[0]
        cards_count = upsert_cards(target_view, [build_macmini_card(), build_nas_card()])
        views[0] = target_view
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
            'inserted': [MAC_CARD_TITLE, NAS_CARD_TITLE],
            'cards_in_target_container': cards_count,
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
import copy
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
SECTION_HEADER = 'Core Systems'


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


def is_titled_stack(card: dict, title: str) -> bool:
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


def find_card_by_title(views: list, title: str):
    for view in views:
        if view.get('type') == 'sections':
            for section in view.get('sections', []):
                for card in section.get('cards', []):
                    if is_titled_stack(card, title):
                        return copy.deepcopy(card)
        else:
            for card in view.get('cards', []):
                if is_titled_stack(card, title):
                    return copy.deepcopy(card)
    return None


def build_machine_card(title: str, entities: list[str]) -> dict:
    return {
        'type': 'vertical-stack',
        'cards': [
            {
                'type': 'markdown',
                'title': title,
                'content': f'{title} operational telemetry.',
            },
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': entities,
            },
        ],
    }


def build_core_section(cards_in_order: list[dict]) -> dict:
    return {
        'type': 'grid',
        'cards': [
            {
                'type': 'markdown',
                'title': SECTION_HEADER,
                'content': "Core infrastructure monitoring layer for Rahman's Command Centre.",
            },
            *cards_in_order,
        ],
    }


def is_core_systems_section(section: dict) -> bool:
    if section.get('type') != 'grid':
        return False
    cards = section.get('cards', [])
    if not cards:
        return False
    first = cards[0]
    return (
        isinstance(first, dict)
        and first.get('type') == 'markdown'
        and first.get('title') == SECTION_HEADER
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

        system_health = find_card_by_title(views, 'System Health')
        macmini_health = find_card_by_title(views, 'MacMini Health')
        nas_overview = find_card_by_title(views, 'NAS Overview')

        if system_health is None:
            raise RuntimeError('System Health card not found; cannot build ordered Core Systems section.')
        if macmini_health is None:
            raise RuntimeError('MacMini Health card not found; cannot build ordered Core Systems section.')
        if nas_overview is None:
            raise RuntimeError('NAS Overview card not found; cannot build ordered Core Systems section.')

        kira_card = build_machine_card(
            'Kira Gateway Health',
            [
                'binary_sensor.kira_online',
                'sensor.kira_cpu_usage',
                'sensor.kira_memory_usage',
                'sensor.kira_disk_usage',
                'binary_sensor.kira_openclaw_running',
                'sensor.kira_openclaw_pid',
                'sensor.kira_openclaw_memory_mb',
                'sensor.kira_last_heartbeat',
            ],
        )

        omarchy_card = build_machine_card(
            'Omarchy Laptop Health',
            [
                'binary_sensor.omarchy_online',
                'sensor.omarchy_cpu_usage',
                'sensor.omarchy_memory_usage',
                'sensor.omarchy_disk_usage',
                'sensor.omarchy_gpu_usage',
                'binary_sensor.omarchy_tailscale_connected',
                'sensor.omarchy_last_seen',
            ],
        )

        ordered = [system_health, macmini_health, nas_overview, kira_card, omarchy_card]
        core_section = build_core_section(ordered)

        target_view = views[0]
        if target_view.get('type') != 'sections':
            raise RuntimeError('Expected sections-style dashboard for rahman-command-centre view 0.')

        sections = target_view.get('sections', [])
        sections = [s for s in sections if not is_core_systems_section(s)]
        sections.append(core_section)

        target_view['sections'] = sections
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
            'section': SECTION_HEADER,
            'ordered_cards': [
                'System Health',
                'MacMini Health',
                'NAS Overview',
                'Kira Gateway Health',
                'Omarchy Laptop Health',
            ],
            'sections_count': len(sections),
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

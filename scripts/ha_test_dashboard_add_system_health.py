import asyncio
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
DASHBOARD_URL_PATH = 'rahman-command-centre'
CARD_TITLE = 'System Health'

# Core metrics requested + commonly useful health entities.
REQUIRED_ENTITIES = [
    'sensor.system_monitor_processor_use',
    'sensor.system_monitor_memory_usage',
    'sensor.system_monitor_disk_usage',
]

CANDIDATE_ENTITIES = REQUIRED_ENTITIES + [
    'sensor.processor_use',
    'sensor.memory_use_percent',
    'sensor.disk_use_percent',
    'sensor.system_monitor_disk_free',
    'sensor.system_monitor_disk_use',
    'sensor.system_monitor_load_1_min',
    'sensor.system_monitor_last_boot',
    'sensor.system_monitor_ipv4_address_enp2s0',
    'sensor.system_monitor_network_throughput_in_enp2s0',
    'sensor.system_monitor_network_throughput_out_enp2s0',
    'sensor.disk_free',
    'sensor.disk_use',
    'sensor.load_1m',
    'sensor.last_boot',
    'sensor.ipv4_address_eth0',
    'sensor.home_assistant_uptime',
    'sensor.home_assistant_core_cpu_percent',
    'sensor.home_assistant_core_memory_percent',
    'sensor.throughput_network_in_eth0',
    'sensor.throughput_network_out_eth0',
    'sensor.network_in',
    'sensor.network_out',
    'sensor.network_throughput_in',
    'sensor.network_throughput_out',
    'sensor.database_size',
    'binary_sensor.1_1_1_1',
    'binary_sensor.internet_connection',
    'binary_sensor.updater',
    'update.home_assistant_core_update',
    'update.home_assistant_operating_system_update',
    'update.home_assistant_supervisor_update',
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


async def ws_call(ws, msg_id: int, payload: dict):
    await ws.send(json.dumps({'id': msg_id, **payload}))
    data = json.loads(await ws.recv())
    if data.get('id') != msg_id:
        raise RuntimeError(f'Unexpected response id: {data}')
    return data


def build_health_card(existing_entity_ids: set[str]):
    optional_entities = [
        eid for eid in CANDIDATE_ENTITIES
        if eid not in REQUIRED_ENTITIES and eid in existing_entity_ids
    ]
    entities = REQUIRED_ENTITIES + optional_entities

    return {
        'type': 'vertical-stack',
        'cards': [
            {
                'type': 'markdown',
                'title': CARD_TITLE,
                'content': 'Quick operational view of CPU, storage, memory, and HA health. If CPU/storage show as unavailable, enable system_monitor sensors.'
            },
            {
                'type': 'entities',
                'show_header_toggle': False,
                'entities': entities,
            }
        ]
    }


def upsert_card_into_view(view: dict, health_card: dict):
    if view.get('type') == 'sections':
        sections = view.get('sections', [])
        if not sections:
            sections = [{'type': 'grid', 'cards': []}]
            view['sections'] = sections

        first_section = sections[0]
        cards = first_section.get('cards', [])
        cards = [
            c for c in cards
            if not (
                isinstance(c, dict)
                and c.get('type') == 'vertical-stack'
                and isinstance(c.get('cards'), list)
                and any(
                    isinstance(sc, dict)
                    and sc.get('type') == 'markdown'
                    and sc.get('title') == CARD_TITLE
                    for sc in c.get('cards', [])
                )
            )
        ]
        cards.append(health_card)
        first_section['cards'] = cards
        sections[0] = first_section
        view['sections'] = sections
        return len(cards)

    cards = view.get('cards', [])
    cards = [
        c for c in cards
        if not (
            isinstance(c, dict)
            and c.get('type') == 'vertical-stack'
            and isinstance(c.get('cards'), list)
            and any(
                isinstance(sc, dict)
                and sc.get('type') == 'markdown'
                and sc.get('title') == CARD_TITLE
                for sc in c.get('cards', [])
            )
        )
    ]
    cards.append(health_card)
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

        states_resp = await ws_call(ws, 1, {'type': 'get_states'})
        if not states_resp.get('success'):
            raise RuntimeError(f"Cannot load states: {states_resp.get('error')}")
        existing_entity_ids = {s.get('entity_id') for s in states_resp['result'] if s.get('entity_id')}

        cfg_resp = await ws_call(ws, 2, {'type': 'lovelace/config', 'url_path': DASHBOARD_URL_PATH})
        if not cfg_resp.get('success'):
            raise RuntimeError(f"Cannot load dashboard {DASHBOARD_URL_PATH}: {cfg_resp.get('error')}")

        cfg = cfg_resp['result']
        views = cfg.get('views', [])
        if not views:
            raise RuntimeError('Dashboard has no views')

        view = views[0]
        health_card = build_health_card(existing_entity_ids)
        card_count = upsert_card_into_view(view, health_card)
        views[0] = view
        cfg['views'] = views

        save_resp = await ws_call(ws, 3, {
            'type': 'lovelace/config/save',
            'url_path': DASHBOARD_URL_PATH,
            'config': cfg,
        })
        if not save_resp.get('success'):
            raise RuntimeError(f"Save failed: {save_resp.get('error')}")

        matched = [eid for eid in CANDIDATE_ENTITIES if eid in existing_entity_ids]
        print(json.dumps({
            'ok': True,
            'dashboard': DASHBOARD_URL_PATH,
            'inserted': CARD_TITLE,
            'matched_entities': matched,
            'matched_count': len(matched),
            'cards_in_target_container': card_count,
        }, indent=2))


if __name__ == '__main__':
    asyncio.run(main())

import json, asyncio
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
import websockets

env = {}
for line in (BASE_DIR / 'config' / 'ha.env').read_text().splitlines():
    line = line.strip()
    if not line or line.startswith('#') or '=' not in line:
        continue
    k, v = line.split('=', 1)
    env[k.strip()] = v.strip().strip('"')

url = env['HA_URL'].rstrip('/').replace('http://', 'ws://').replace('https://', 'wss://') + '/api/websocket'
token = env['HA_TOKEN']

async def main():
    async with websockets.connect(url, open_timeout=10, close_timeout=5) as ws:
        print(await ws.recv())
        await ws.send(json.dumps({'type': 'auth', 'access_token': token}))
        print(await ws.recv())
        reqs = [
            {'id': 1, 'type': 'get_config'},
            {'id': 2, 'type': 'lovelace/config'},
            {'id': 3, 'type': 'lovelace/config', 'url_path': 'rahman_command_centre'},
            {'id': 4, 'type': 'lovelace/dashboards/list'},
        ]
        for r in reqs:
            await ws.send(json.dumps(r))
            print(await ws.recv())

if __name__ == '__main__':
    asyncio.run(main())

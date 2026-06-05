import asyncio, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
import websockets

env = {}
for ln in (BASE_DIR / 'config' / 'ha.env').read_text().splitlines():
    ln = ln.strip()
    if not ln or ln.startswith('#') or '=' not in ln:
        continue
    k, v = ln.split('=', 1)
    env[k.strip()] = v.strip().strip('"')

ws_url = env['HA_URL'].rstrip('/').replace('http://', 'ws://').replace('https://', 'wss://') + '/api/websocket'

async def main():
    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5) as s:
        await s.recv()
        await s.send(json.dumps({'type': 'auth', 'access_token': env['HA_TOKEN']}))
        await s.recv()

        async def call(i, method, endpoint, data=None):
            payload = {'id': i, 'type': 'supervisor/api', 'method': method, 'endpoint': endpoint}
            if data is not None:
                payload['data'] = data
            await s.send(json.dumps(payload))
            return json.loads(await s.recv())

        r1 = await call(1, 'post', '/network/interface/enp2s0/update', {'mdns': 'announce', 'llmnr': 'resolve'})
        r2 = await call(2, 'post', '/network/reload', {})
        r3 = await call(3, 'post', '/host/reload', {})
        r4 = await call(4, 'get', '/network/interface/enp2s0/info')

        print(json.dumps({
            'update_ok': r1.get('success'),
            'reload_network_ok': r2.get('success'),
            'reload_host_ok': r3.get('success'),
            'interface_info': r4.get('result', {}),
            'errors': [r.get('error') for r in (r1, r2, r3, r4) if not r.get('success')]
        }, indent=2))

asyncio.run(main())

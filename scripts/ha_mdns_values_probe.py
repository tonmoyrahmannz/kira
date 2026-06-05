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
    async with websockets.connect(ws_url) as s:
        await s.recv()
        await s.send(json.dumps({'type': 'auth', 'access_token': env['HA_TOKEN']}))
        await s.recv()

        async def call(i, method, endpoint, data=None):
            payload = {'id': i, 'type': 'supervisor/api', 'method': method, 'endpoint': endpoint}
            if data is not None:
                payload['data'] = data
            await s.send(json.dumps(payload))
            r = json.loads(await s.recv())
            print(i, method, endpoint, '=>', r.get('success'), r.get('error') or '')
            if r.get('result') is not None:
                print(str(r.get('result'))[:500])

        i = 1
        await call(i, 'get', '/network/interface/enp2s0/info'); i += 1
        await call(i, 'post', '/network/interface/enp2s0/update', {'mdns': 'enabled', 'llmnr': 'enabled'}); i += 1
        await call(i, 'post', '/network/interface/enp2s0/update', {'mdns': 'on', 'llmnr': 'on'}); i += 1
        await call(i, 'post', '/network/interface/enp2s0/update', {'mdns': 'true', 'llmnr': 'true'}); i += 1
        await call(i, 'post', '/network/interface/enp2s0/update', {'mdns': 'default', 'llmnr': 'default'}); i += 1
        await call(i, 'post', '/network/reload', {}); i += 1
        await call(i, 'get', '/network/interface/enp2s0/info')

asyncio.run(main())

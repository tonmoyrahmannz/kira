import asyncio, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
import websockets

env={}
for line in (BASE_DIR / 'config' / 'ha.env').read_text().splitlines():
    line=line.strip()
    if not line or line.startswith('#') or '=' not in line:
        continue
    k,v=line.split('=',1)
    env[k.strip()] = v.strip().strip('"')

ws_url = env['HA_URL'].rstrip('/').replace('http://','ws://').replace('https://','wss://') + '/api/websocket'
out = BASE_DIR / 'scripts' / '.cache' / 'supervisor_probe.json'
out.parent.mkdir(parents=True, exist_ok=True)

async def main():
    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type':'auth','access_token':env['HA_TOKEN']}))
        await ws.recv()
        async def call(i, endpoint):
            await ws.send(json.dumps({'id':i,'type':'supervisor/api','method':'get','endpoint':endpoint}))
            return json.loads(await ws.recv())
        a = await call(1,'/addons')
        i = await call(2,'/info')
        b = await call(3,'/backups')
    data = {
        'addons': a.get('result',{}).get('addons',[]) if a.get('success') else [],
        'info': i.get('result',{}) if i.get('success') else {},
        'backups': b.get('result',{}).get('backups',[]) if b.get('success') else [],
    }
    out.write_text(json.dumps(data, indent=2))
    print(str(out))

asyncio.run(main())

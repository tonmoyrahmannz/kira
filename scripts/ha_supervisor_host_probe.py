import asyncio, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
import websockets

env={}
for line in (BASE_DIR / 'config' / 'ha.env').read_text().splitlines():
    line=line.strip()
    if not line or line.startswith('#') or '=' not in line: continue
    k,v=line.split('=',1)
    env[k.strip()]=v.strip().strip('"')

ws_url=env['HA_URL'].rstrip('/').replace('http://','ws://').replace('https://','wss://')+'/api/websocket'

EPS=[
    '/info','/host/info','/host/options','/host/network/info','/dns/info','/core/info','/supervisor/info',
    '/network/info','/os/info','/resolution/info','/services'
]

async def main():
    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type':'auth','access_token':env['HA_TOKEN']}))
        await ws.recv()
        i=1
        for ep in EPS:
            await ws.send(json.dumps({'id':i,'type':'supervisor/api','method':'get','endpoint':ep}))
            r=json.loads(await ws.recv())
            ok=r.get('success')
            print('---',ep,'success=',ok)
            if ok:
                print(json.dumps(r.get('result',{}))[:1200])
            else:
                print(r.get('error'))
            i+=1

asyncio.run(main())

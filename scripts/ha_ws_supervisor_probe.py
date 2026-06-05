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

async def main():
    async with websockets.connect(ws_url) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type':'auth','access_token':env['HA_TOKEN']}))
        await ws.recv()
        for i,p in enumerate([
            {'type':'supervisor/api','method':'get','endpoint':'/addons'},
            {'type':'supervisor/api','method':'get','endpoint':'/info'},
            {'type':'supervisor/api','method':'get','endpoint':'/backups'},
        ],start=1):
            await ws.send(json.dumps({'id':i, **p}))
            print(await ws.recv())

asyncio.run(main())

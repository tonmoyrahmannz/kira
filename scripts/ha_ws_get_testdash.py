import json, asyncio
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
import websockets

env={}
for line in (BASE_DIR / 'config' / 'ha.env').read_text().splitlines():
    line=line.strip()
    if not line or line.startswith('#') or '=' not in line:
        continue
    k,v=line.split('=',1)
    env[k.strip()]=v.strip().strip('"')
url=env['HA_URL'].rstrip('/').replace('http://','ws://').replace('https://','wss://')+'/api/websocket'
token=env['HA_TOKEN']

async def query(url_path):
    async with websockets.connect(url, open_timeout=10, close_timeout=5) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type':'auth','access_token':token}))
        await ws.recv()
        await ws.send(json.dumps({'id':1,'type':'lovelace/config','url_path':url_path}))
        print(url_path)
        print(await ws.recv())

async def main():
    for p in ['rahman_command_centre','rahman-command-centre','test_2','test-2']:
        await query(p)

asyncio.run(main())

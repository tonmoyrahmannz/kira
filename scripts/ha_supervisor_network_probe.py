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

async def call(ws,i,method,endpoint,data=None):
    p={'id':i,'type':'supervisor/api','method':method,'endpoint':endpoint}
    if data is not None: p['data']=data
    await ws.send(json.dumps(p))
    return json.loads(await ws.recv())

async def main():
    async with websockets.connect(ws_url) as ws:
        await ws.recv(); await ws.send(json.dumps({'type':'auth','access_token':env['HA_TOKEN']})); await ws.recv()
        tests=[
            ('get','/network/interface/enp2s0/info',None),
            ('post','/host/options',{'hostname':'homeassistant'}),
            ('post','/network/interface/enp2s0/update',{}),
            ('post','/network/interface/enp2s0/update',{'mdns':'default'}),
            ('post','/network/interface/enp2s0/update',{'llmnr':'default'}),
            ('post','/network/interface/enp2s0/update',{'ipv4':{'method':'auto'}}),
            ('post','/network/interface/enp2s0/update',{'enabled':True}),
            ('post','/network/reload',{}),
            ('post','/host/reload',{}),
        ]
        i=1
        for m,e,d in tests:
            r=await call(ws,i,m,e,d)
            print(m,e,'=>',r.get('success'), r.get('error'))
            if r.get('success'):
                print(str(r.get('result'))[:500])
            i+=1

asyncio.run(main())

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

async def call(ws, i, method, endpoint, data=None):
    payload={'id':i,'type':'supervisor/api','method':method,'endpoint':endpoint}
    if data is not None:
        payload['data']=data
    await ws.send(json.dumps(payload))
    r=json.loads(await ws.recv())
    return r

async def main():
    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5) as ws:
        await ws.recv()
        await ws.send(json.dumps({'type':'auth','access_token':env['HA_TOKEN']}))
        await ws.recv()

        i=1
        # inspect options endpoints
        for ep in ['/dns/info','/dns/options','/host/info','/network/info']:
            r=await call(ws,i,'get',ep)
            print('GET',ep,r.get('success'), r.get('error') or '')
            if r.get('success'):
                print(json.dumps(r.get('result',{}))[:600])
            i+=1

        # try setting dns options explicitly
        r=await call(ws,i,'post','/dns/options',{'mdns':True,'llmnr':True,'fallback':True})
        print('POST /dns/options',r.get('success'), r.get('error') or '', json.dumps(r.get('result',{}))[:200])
        i+=1

        # try host options (if supported)
        r=await call(ws,i,'post','/host/options',{'hostname':'homeassistant','llmnr_hostname':'homeassistant','broadcast_mdns':True,'broadcast_llmnr':True})
        print('POST /host/options',r.get('success'), r.get('error') or '', json.dumps(r.get('result',{}))[:200])
        i+=1

        # restart network manager service inside HAOS host
        r=await call(ws,i,'post','/host/services/systemd/restart',{'service':'systemd-resolved'})
        print('restart resolved',r.get('success'), r.get('error') or '')
        i+=1
        r=await call(ws,i,'post','/host/services/systemd/restart',{'service':'systemd-networkd'})
        print('restart networkd',r.get('success'), r.get('error') or '')

asyncio.run(main())

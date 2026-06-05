import json, asyncio, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
from datetime import datetime, timezone
import requests, websockets

ENV_PATH = BASE_DIR / 'config' / 'ha.env'
OUT_DIR = BASE_DIR / 'scripts' / '.cache'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_env(path):
    env = {}
    for line in Path(path).read_text().splitlines():
        line=line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k,v=line.split('=',1)
        env[k.strip()] = v.strip().strip('"')
    return env


def rest_get(base, token, endpoint):
    r = requests.get(f"{base.rstrip('/')}{endpoint}", headers={"Authorization": f"Bearer {token}", "Content-Type":"application/json"}, timeout=30)
    r.raise_for_status()
    return r.json()


async def ws_fetch(base, token):
    ws_url = base.rstrip('/').replace('http://','ws://').replace('https://','wss://') + '/api/websocket'
    async with websockets.connect(ws_url, open_timeout=20, close_timeout=5, max_size=20_000_000) as ws:
        await ws.recv()  # auth_required
        await ws.send(json.dumps({'type':'auth','access_token':token}))
        await ws.recv()  # auth_ok
        async def call(i,payload):
            await ws.send(json.dumps({'id':i, **payload}))
            return json.loads(await ws.recv())

        results = {}
        calls = {
            'dashboards': {'type':'lovelace/dashboards/list'},
            'device_registry': {'type':'config/device_registry/list'},
            'entity_registry': {'type':'config/entity_registry/list'},
            'area_registry': {'type':'config/area_registry/list'},
            'automation_configs': {'type':'config/automation/list'},
            'config_entries': {'type':'config_entries/get'},
        }
        i=1
        for k,v in calls.items():
            resp = await call(i,v)
            results[k]=resp
            i+=1
        return results


def main():
    env = load_env(ENV_PATH)
    base, token = env['HA_URL'], env['HA_TOKEN']

    data = {}
    data['generated_at_utc'] = datetime.now(timezone.utc).isoformat()

    data['config'] = rest_get(base, token, '/api/config')
    data['states'] = rest_get(base, token, '/api/states')
    data['services'] = rest_get(base, token, '/api/services')
    # supervisor endpoints (if available)
    for name, ep in [
        ('hassio_info','/api/hassio/info'),
        ('hassio_addons','/api/hassio/addons'),
        ('hassio_backups','/api/hassio/backups'),
    ]:
        try:
            data[name] = rest_get(base, token, ep)
        except Exception as e:
            data[name] = {'error': str(e)}

    data['ws'] = asyncio.run(ws_fetch(base, token))

    out = OUT_DIR / 'runbook_v8_data.json'
    out.write_text(json.dumps(data, indent=2))
    print(str(out))

if __name__ == '__main__':
    main()

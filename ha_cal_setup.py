#!/usr/bin/env python3
"""Remove old remote_calendar entries and create new ics_calendar entries."""
import json
import os
import subprocess

with open(os.path.expanduser('~/.hermes/.env')) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, _, v = line.partition('=')
        os.environ[k.strip()] = v.strip()

HASS_URL = os.environ.get('HASS_URL', 'http://homeassistant.local:8123')
TOKEN=os.env...EN', '')

HEADERS = ['-H', f'Authorization: Bearer ***', '-H', 'Content-Type: application/json']

def ha_api(method, path, data=None):
    cmd = ['curl', '-s', '-S', '--max-time', '15', '-X', method] + HEADERS
    if data:
        cmd += ['-d', json.dumps(data)]
    cmd += [f'{HASS_URL}{path}']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"curl error: {r.stderr}")
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Raw: {r.stdout[:500]}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        print(f"Raw: {r.stdout[:500]}")
        return None

# === DELETE OLD remote_calendar entries ===
print("=== Deleting old remote_calendar entries ===")
entries = ha_api('GET', '/api/config/config_entries/entry')
if entries:
    for e in entries:
        if e.get('domain') == 'remote_calendar':
            eid = e['entry_id']
            print(f"  Deleting: {eid} - {e.get('title', '?')}")
            del_result = ha_api('DELETE', f'/api/config/config_entries/entry/{eid}')
            print(f"    Result: {del_result}")

# === CREATE ics_calendar entries via config flow ===
print("\n=== Creating ics_calendar entries ===")

calendars = [
    {
        "name": "Airbnb",
        "url": "https://www.airbnb.com/calendar/ical/41503501.ics?t=666bad4d73424972b22d21b046879895&locale=en-AU"
    },
    {
        "name": "Booking.com",
        "url": "https://ical.booking.com/v1/export?t=784dbd76-f784-4d1f-8704-8120ac4c431b",
        "verify_ssl": False
    }
]

for cal in calendars:
    print(f"\n  Setting up: {cal['name']}")
    
    # Start config flow
    flow_data = {
        "handler": "ics_calendar",
        "show_advanced_options": True
    }
    flow = ha_api('POST', '/api/config/config_entries/flow', flow_data)
    if not flow:
        print(f"    Failed to start flow for {cal['name']}")
        continue
    
    flow_id = flow.get('flow_id')
    print(f"    Flow ID: {flow_id}")
    
    # Submit step data
    step_data = {
        "name": cal['name'],
        "url": cal['url']
    }
    if cal.get('verify_ssl') is not None:
        step_data['verify_ssl'] = False
    
    result = ha_api('POST', f'/api/config/config_entries/flow/{flow_id}', step_data)
    print(f"    Result: {json.dumps(result, indent=2)[:500] if result else 'No result'}")

# === VERIFY ===
print("\n=== Verification ===")
states = ha_api('GET', '/api/states')
if states:
    cals = [s for s in states if s['entity_id'].startswith('calendar.') and s.get('attributes',{}).get('source') != 'remote_calendar']
    for c in cals:
        a = c.get('attributes', {})
        print(f"  CAL: {c['entity_id']} state={c.get('state','?')} name={a.get('friendly_name','?')} source={a.get('source','?')}")

print("\n=== Done ===")

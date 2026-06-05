#!/usr/bin/env python3
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

import requests

HA_ENV = BASE_DIR / 'config' / 'ha.env'
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH = LOG_DIR / 'garage_heat_once_20260515.log'

CLIMATE_ENTITY = 'climate.dyson_sz1_au_nja5315a'
TEMP_ENTITY = 'sensor.garage_sensor_temperature'
TARGET_SETPOINT = 25
TARGET_TEMP = 22.0
POLL_SECONDS = 120
MAX_WAIT_SECONDS = 3 * 60 * 60


def load_env(path: Path):
    text = path.read_text()
    def get(name: str) -> str:
        m = re.search(rf'^{name}="([^"]+)"', text, re.M)
        if not m:
            raise RuntimeError(f'Missing {name} in {path}')
        return m.group(1)
    return get('HA_URL').rstrip('/'), get('HA_TOKEN')


def log(msg: str):
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG_PATH.open('a') as f:
        f.write(line + '\n')


def request(session: requests.Session, method: str, url: str, **kwargs):
    timeout = kwargs.pop('timeout', 90)
    for attempt in range(1, 4):
        try:
            r = session.request(method, url, timeout=timeout, **kwargs)
            r.raise_for_status()
            return r
        except Exception as e:
            if attempt == 3:
                raise
            log(f'{method} {url} failed on attempt {attempt}: {e}; retrying')
            time.sleep(10)


def call_service(session: requests.Session, base: str, domain: str, service: str, payload: dict):
    url = f'{base}/api/services/{domain}/{service}'
    log(f'Calling {domain}.{service} with {json.dumps(payload, sort_keys=True)}')
    r = request(session, 'POST', url, json=payload)
    log(f'{domain}.{service} -> HTTP {r.status_code}')


def get_state(session: requests.Session, base: str, entity_id: str):
    r = request(session, 'GET', f'{base}/api/states/{entity_id}')
    return r.json()


def parse_temp(state: str):
    try:
        return float(state)
    except Exception:
        return None


def main():
    base, token = load_env(HA_ENV)
    session = requests.Session()
    session.headers.update({
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    })

    log('Starting garage heat job')
    try:
        climate_before = get_state(session, base, CLIMATE_ENTITY)
        temp_before = get_state(session, base, TEMP_ENTITY)
        log(f"Initial climate state: {climate_before.get('state')}")
        log(f"Initial garage temp state: {temp_before.get('state')}")
    except Exception as e:
        log(f'Initial state read failed: {e}')

    call_service(session, base, 'climate', 'set_hvac_mode', {
        'entity_id': CLIMATE_ENTITY,
        'hvac_mode': 'heat',
    })
    call_service(session, base, 'climate', 'set_temperature', {
        'entity_id': CLIMATE_ENTITY,
        'temperature': TARGET_SETPOINT,
    })

    deadline = time.time() + MAX_WAIT_SECONDS
    turned_off = False
    while time.time() < deadline:
        try:
            temp_state = get_state(session, base, TEMP_ENTITY)
            raw = temp_state.get('state')
            temp = parse_temp(raw)
            log(f'Garage temperature reading: {raw}')
            if temp is not None and temp >= TARGET_TEMP:
                log(f'Garage reached {temp}°C; turning heater off')
                call_service(session, base, 'climate', 'turn_off', {'entity_id': CLIMATE_ENTITY})
                turned_off = True
                break
        except Exception as e:
            log(f'Temperature check failed: {e}')
        time.sleep(POLL_SECONDS)

    if not turned_off:
        log('Safety timeout reached; turning heater off')
        call_service(session, base, 'climate', 'turn_off', {'entity_id': CLIMATE_ENTITY})

    log('Garage heat job complete')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log(f'Fatal error: {e}')
        sys.exit(1)

# Tuya IR Remote Runbook

Last updated: 2026-03-08  
Owner: Tonmoy / Kira

## 1) Architecture Overview

Implemented approach: **Home Assistant custom integration + package scripts + Lovelace remote dashboard**.

Why this approach:
- Additive to existing Official Tuya + LocalTuya setup.
- Provides HA-native services (`tuya_ir_remote.send_button`, `tuya_ir_remote.send_key`).
- Provides optional true HA `remote` entities (`remote.soundbar_ir_remote`, `remote.projector_ir_remote`).
- Uses script wrappers for stable user-facing actions.
- Supports robust token refresh/signing in backend.

Key paths (staged in Kira workspace):
- `ha-config-staging/config/custom_components/tuya_ir_remote/`
- `ha-config-staging/config/packages/tuya_ir_remote.yaml`
- `ha-config-staging/config/ui/garage_ir_remote.yaml`

## 2) Authentication & Token Handling

Backend calls Tuya OpenAPI directly:
- Endpoint: `https://openapi.tuyaus.com`
- Token API: `GET /v1.0/token?grant_type=1`
- Command API: `POST /v2.0/infrareds/{infrared_id}/remotes/{remote_id}/command`

Behavior:
- Auto-fetches token at startup/use.
- Reuses token until near expiry.
- Auto-refreshes token and retries on auth-like failures (`1010`, `1106`, `1011`).
- Logs request/refresh events via HA logger.

## 3) Device IDs and Mapping

Infrared hub:
- `infrared_id = ebab7105bb50cd8408etyu`

Soundbar:
- `remote_id = eb63f0598155a83d99dyhf`
- `remote_index = 414165031`
- `category_id = 7`

Projector:
- `remote_id = ebfb979fc0f3bb3f1fjeap`
- `remote_index = 6667`
- `category_id = 6`

### Soundbar button mapping
| Script | Tuya key |
|---|---|
| `script.soundbar_volume_up` | `Volume-` |
| `script.soundbar_volume_down` | `Volume+` |
| `script.soundbar_power` | `power` |
| `script.soundbar_bluetooth` | `bluetooth` |
| `script.soundbar_play` | `Play` |
| `script.soundbar_pause` | `Pause` |
| `script.soundbar_previous` | `Previous` |
| `script.soundbar_next` | `Next` |

> Note: volume keys are intentionally reversed in Tuya profile; script names preserve correct user-facing behavior.

### Projector button mapping
| Script | Tuya key |
|---|---|
| `script.projector_power_on` | `PowerOn` |
| `script.projector_power_off` | `PowerOff` |
| `script.projector_source` | `source` |
| `script.projector_menu` | `Menu` |
| `script.projector_ok` | `OK` |
| `script.projector_back` | `Back` |
| `script.projector_exit` | `exit` |
| `script.projector_up` | `Up` |
| `script.projector_down` | `Down` |
| `script.projector_left` | `Left` |
| `script.projector_right` | `Right` |
| `script.projector_mute` | `Mute` |

Optional (commented until verified): mode/input/info.

## 4) Dashboard UI

Dashboard YAML:
- `/config/ui/garage_ir_remote.yaml`

Layout sections:
- Projector Remote: power on/off, source/menu/mute, full D-pad cluster (up/down/left/right/ok), back/exit
- Soundbar Remote: power, bluetooth, volume +/-, media transport controls

Design goals met:
- iPad-friendly
- grouped control surfaces
- human-readable labels

## 5) Additive Safety

This implementation does **not** replace or modify:
- Official Tuya integration
- LocalTuya integration
- existing Tuya scenes
- unrelated dashboards

Everything is additive under custom component + package + dashboard YAML.

## 6) How to Add Another IR Device

1. Add new device under `tuya_ir_remote.devices` in config.
2. Add button mappings in `const.py`.
3. Add script wrappers in package YAML.
4. Add UI buttons in `ui/garage_ir_remote.yaml`.

## 7) How to Add a New Button

1. Determine exact Tuya `key` string.
2. Add button->key mapping in `const.py`.
3. Add corresponding `script.*` wrapper in package.
4. Add button in dashboard YAML.
5. Reload scripts or restart HA.

## 8) Troubleshooting

Enable debug logging:
```yaml
logger:
  logs:
    custom_components.tuya_ir_remote: debug
```

Check for:
- token refresh failures
- HTTP/signature errors
- wrong key names
- incorrect remote_index/category_id

Quick service test:
- Developer Tools -> Services -> `tuya_ir_remote.send_key`
- Example data:
```yaml
device: projector
key: Menu
```

## 9) Validation Status (final, after real credentials)

Validation run executed after credentials update and HA restart.

Deployment context:
- HAOS over SSH (`root@192.168.50.166:22`)
- Integration loaded and services present
- Scripts invoked via Home Assistant service API

### Pass/Fail Matrix

| Script | Result | Notes |
|---|---|---|
| `script.soundbar_power` | ❌ Fail | HTTP 500, Tuya API error `30706` (`command or value not support`) |
| `script.soundbar_bluetooth` | ❌ Fail | HTTP 500, Tuya API error `30706` (`command or value not support`) |
| `script.soundbar_volume_up` | ✅ Pass | HTTP 200 |
| `script.soundbar_volume_down` | ✅ Pass | HTTP 200 |
| `script.projector_power_on` | ✅ Pass | HTTP 200 |
| `script.projector_power_off` | ✅ Pass | HTTP 200 |
| `script.projector_source` | ❌ Fail | HTTP 500, Tuya API error `30706` (`command or value not support`) |
| `script.projector_menu` | ✅ Pass | HTTP 200 |
| `script.projector_ok` | ✅ Pass | HTTP 200 |
| `script.projector_back` | ✅ Pass | HTTP 200 |
| `script.projector_exit` | ❌ Fail | HTTP 500, Tuya API error `30706` (`command or value not support`) |
| `script.projector_up` | ✅ Pass | HTTP 200 |
| `script.projector_down` | ✅ Pass | HTTP 200 |
| `script.projector_left` | ✅ Pass | HTTP 200 |
| `script.projector_right` | ✅ Pass | HTTP 200 |

Summary:
- **11/15 passed**
- **4/15 failed** (`soundbar_power`, `soundbar_bluetooth`, `projector_source`, `projector_exit`)

Interpretation:
- Authentication/signing are now working (many commands succeed).
- Remaining failures are likely key-profile mismatches for those specific buttons in current Tuya IR profile.
- Candidate alternatives to test safely next: `Power`, `BT`, `Source`, `Exit` (case/profile variants), while keeping existing working keys unchanged.

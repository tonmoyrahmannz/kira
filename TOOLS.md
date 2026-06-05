# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Hermes Desktop

- Installed app: `/Applications/Hermes Agent.app`
- Bundle ID: `com.nousresearch.hermes`
- Version installed: `0.4.5`
- Source: `fathah/hermes-desktop` release `v0.4.5`, Apple Silicon DMG.
- App data path: `/Users/tonmoyrahman/Library/Application Support/hermes-desktop`
- Launch from terminal:

```bash
open -a '/Applications/Hermes Agent.app'
```

## Home Assistant

- Home Assistant URL: `http://192.168.50.166:8123`
- Long-lived HA token for Kira/Hermes automation is stored privately at `/Users/tonmoyrahman/Kira/secrets/homeassistant.env`.
- Use from shell:

```bash
source /Users/tonmoyrahman/Kira/secrets/homeassistant.env
```

## SSH

### Home Assistant add-on SSH

- Alias: `ha`
- Host: `192.168.50.166`
- User: `root`
- Port: `22`
- Key: `/Users/tonmoyrahman/.ssh/id_ed25519`
- Configured in `/Users/tonmoyrahman/.ssh/config`.
- The Mac Mini public key `tonmoy-macmini-ha` is authorised in the Advanced SSH & Web Terminal add-on.
- Verified 2026-05-23:

```bash
ssh ha
```

returns `SSH_OK`; `/config` maps to `/homeassistant`.

## Device map

- `192.168.50.166` — Wyse 5070 / HAOS / primary Home Assistant.
- `192.168.50.208` — Mac Mini / active Kira-Hermes / Plex / NAS / Tailscale.
- `192.168.50.28` — Omarchy laptop / previous Kira-OpenClaw host.
- `192.168.50.1` — ASUS router/gateway.
- `192.168.50.188` — Gree Controller.
- `192.168.50.224` — Neo Controller.
- `192.168.50.100` — Tuya Zigbee Gateway.

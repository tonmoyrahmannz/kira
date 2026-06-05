# SYSTEM_MAP.md (Bootstrap Summary)

Last verified: 2026-05-16
Last updated: 2026-05-16
Updated by: Kira
Verification source: live host check, AGENTS.md, BOOT.md, docs/session_state.md, smart-home docs, runbooks

Purpose: quick, startup-safe system map for Kira.  
Canonical detailed architecture remains in `docs/system-map.md` and smart-home docs.

## Core Control Plane
- Assistant system: **Kira**
- Kira workspace: `/Users/tonmoyrahman/Kira`
- Primary host machine for Kira: Mac Mini (`Macmini`, user `tonmoyrahman`)

## Home Infrastructure (High Level)
- Router: `192.168.50.1`
- Home Assistant appliance: Wyse 5070 thin client `192.168.50.166`
  - HAOS on bare metal (`generic-x86-64`)
  - Dedicated appliance with local SSD storage
- Mac Mini (M1) `192.168.50.208`
  - Kira runtime
  - Plex host
  - NAS host
  - Tailscale subnet router
  - Other auxiliary services
- Omarchy laptop `192.168.50.28`
  - Legacy/secondary Linux node
  - Historical source of some runbooks, dashboards, and telemetry scripts
- Home Assistant endpoint used by Kira: `http://192.168.50.166:8123`

## Key Smart-Home Components
- **Home Assistant**: primary orchestration/control layer
- **Tuya IR hub/blaster**: IR device control bridge
- **Projector**: controlled via Tuya scenes/integration
- **Soundbar**: controlled via Tuya scenes/integration
- **Gree HVAC**: ducted zone control via HA integrations/entities
- **NeoSmartBlinds**: blind entities + Alexa-sync automations
- **Tailscale**: secure remote access overlay (no public inbound exposure)

## Voice / Briefing Direction
- Alexa is used as voice surface.
- Planned universal morning briefing: guest unit status + calendar + reminders (+ optional Outlook).
- Practical integration path: HA + Alexa routines/webhooks (dynamic speech via HA bridge).

## Canonical Documents
- Documentation hub: `docs/README.md`
- Detailed system map: `docs/system-map.md`
- Current smart-home professional documentation: `/Volumes/Plex_HD/Backups/HomeAssistant/Smart_Home_Technical_Documentation_v5_Professional.md`
- Smart-home architecture: `docs/smart-home/Smart_Home_Technical_Documentation_v7_Enterprise.md`
- Gree zoning architecture: `docs/smart-home/Gree_Ducted_Zoning_Architecture.md`
- Live runbook snapshot: `docs/runbooks/Smart_Home_Runbook_v8.md`
- Kira control plane handover: `docs/kira/Kira_Control_Plane_Handover.md`

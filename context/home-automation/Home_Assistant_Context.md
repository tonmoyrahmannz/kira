# Home Assistant And Home Lab Context - Tonmoy Rahman

## Purpose

This file provides smart home, Home Assistant, NAS, and home lab context for Kira, Hermes, specialist agents, and future AI assistants.

It should be used for:

- Home Assistant troubleshooting
- Dashboard creation
- NAS automation
- Kira/Hermes operations
- Smart home architecture decisions
- Home lab changes
- Network-aware automation
- Runbook generation

Recommended NAS location:

```text
/nas/Documents/Kira/Context/Home_Assistant_Context.md
```

Supporting NAS locations:

```text
/nas/Documents/Projects/
/nas/Documents/Kira/
/nas/Documents/MealPrep/
/nas/Documents/Sketchup/
```

---

# Current Architecture Summary

Primary smart home platform:

```text
Home Assistant OS
```

Current HAOS setup:

```text
Home Assistant OS ARM64
Running as a VM on Wyse 5070
HAOS IP: 192.168.50.166
```

Important note:

Older references to HAOS running primarily on Mac Mini VMware Fusion may be outdated. The current primary architecture places HAOS on the Wyse 5070.

---

# Core Network

Primary LAN:

```text
192.168.50.0/24
```

Gateway:

```text
192.168.50.1
```

Key hosts:

```text
HAOS / Home Assistant: 192.168.50.166
Mac Mini: 192.168.50.208
Omarchy laptop: 192.168.50.28
Tailscale subnet router: Mac Mini
```

Known Tailscale context:

```text
Mac Mini Tailscale IP: 100.78.16.33
```

Use Tailscale for remote access where possible.

---

# Hardware Roles

## Wyse 5070

Role:

- Dedicated Home Assistant OS host.
- Runs HAOS with Core, Supervisor, and Add-on framework available.

Why this matters:

- Home Assistant is more stable when separated from Mac Mini experiments.
- HAOS add-ons are available.
- This host should be treated as core home infrastructure.

## Mac Mini

Roles:

- Plex
- SMB/NAS shares
- Tailscale subnet router
- Auxiliary services
- Kira/Hermes runtime
- General home server functions

Known IP:

```text
192.168.50.208
```

Mac Mini is an important operational hub.

## Omarchy Laptop

Known IP:

```text
192.168.50.28
```

Historical roles:

- OpenClaw Gateway
- Kira runtime
- SSH orchestration
- Automation tooling

Current note:

Kira has moved toward Hermes/Mac Mini. Any assumption that Omarchy is still the main Kira host may be outdated.

---

# Smart Home Integrations

## Home Assistant

Home Assistant is the central automation platform.

Important principles:

- Keep configuration documented.
- Avoid destructive changes without backups.
- Validate YAML before reloads/restarts.
- Prefer packages and modular configuration where useful.
- Use backups before major changes.
- Use local control where practical.

## Apple HomeKit

Apple TV acts as Home Hub.

Home Assistant entities may be exposed to Apple ecosystem via HomeKit Bridge.

## Tuya

Tuya is used for many Zigbee and cloud-connected devices.

Known integration modes:

- Tuya cloud
- LocalTuya for selected local-control use cases
- Tuya Zigbee gateway

Known device:

```text
Tuya Zigbee LAN Gateway: 192.168.50.100
```

Principle:

Use local control where reliable, but accept cloud integration where unavoidable.

## Gree HVAC — Ducted Zoning Architecture

Gree integration is local and encrypted via the G‑Cloud ecosystem.

### Controller
```text
192.168.50.188:7000
```

### System Overview
The house has a **Gree ducted air‑conditioning system with RF zoning** enabling independent room airflow control via wireless thermostats, a master RF hub, and motorised dampers coordinated through a wired zoning interface.

### Hardware Stack

| Layer | Device | Model | Location |
|-------|--------|-------|----------|
| Master Controller | RF / Zone Controller Hub | **ACSG1802** | Attic near ducted indoor unit |
| Zone Interface | Zone Control Interface | **LE60-13/GH** | Wall / ceiling cavity |
| Sensors | RF Wireless Room Controllers | Various Gree RF | Individual rooms |
| Actuators | Motorised Zone Dampers | Various | Duct inlets per zone |
| Cloud | G‑Cloud App | — | Mobile app |

### ACSG1802 (Master RF Hub) — Critical
- Receives RF signals from wireless room remotes
- Central zoning logic controller
- Sends open/close commands to motorised dampers
- Communicates with the ducted indoor unit
- Interfaces with the zone control interface
- Provides Wi‑Fi / cloud connectivity via G‑Cloud app on 2.4 GHz

### LE60-13/GH (Zone Interface) — Critical
- Physical wiring hub for zoning system
- Controls up to 8 motorised dampers
- Interfaces with wired wall controllers
- Communicates with master RF controller via RS485 / HBS

### RF Wireless Room Controllers
- Sense room temperature
- Allow per‑zone heating/cooling requests
- Send RF commands to master controller (≤20 m range, avoid antenna obstruction)

### Signal Flow
```
Temp Rise → RF Call → ACSG1802 Logic →
Damper Opens → Indoor Unit Runs →
Setpoint Reached → Damper Closes →
Status Sync to G‑Cloud
```

### Smart Home Integration
- **Native:** G‑Cloud mobile app, scheduling, remote control
- **Indirect:** IR bridge, Home Assistant automation, Alexa / Google Home linking
- HA integration via local encrypted protocol on port 7000

### Failure Impact
- **ACSG1802 offline:** Critical — no RF, no zoning, dampers default, cloud lost
- **LE60-13/GH failure:** High — dampers non-responsive
- **RF remote failure:** Low — single zone affected
- **Wi‑Fi failure:** Non-critical — app offline only, local still works

### Upgrade Options
- Expand up to 8 dampers per interface
- Add wired thermostats
- Static pressure sensors for demand‑based fan control
- Bypass duct recommended for static pressure balance

### Commissioning / Network Notes
- **Use 2.4 GHz Wi‑Fi** — 5 GHz not supported
- DHCP reservation recommended for the master controller
- Maintain ≤20 m line-of-sight for RF remotes

Be careful with HVAC automations. Comfort and reliability matter more than novelty.

## Neo Smart Blinds

Known controller:

```text
192.168.50.224:8839
```

Used for smart blinds.

Prefer local integration where possible.

## Plex

Runs on Mac Mini.

Plex media is likely stored on Mac Mini/NAS-mounted storage.

---

# NAS Context

NAS path from Linux:

```text
/home/tonmoy/nas
```

Important current NAS document structure:

```text
/nas/Documents/Kira/
/nas/Documents/MealPrep/
/nas/Documents/Projects/
/nas/Documents/Sketchup/
/nas/Documents/Work/
```

Common expected path from Linux:

```text
/home/tonmoy/nas/Documents/
```

Mac Mini likely hosts SMB/NAS shares.

Important share / storage:

```text
Plex_HD
```

Example known storage areas:

```text
Plex_HD/Media/
Plex_HD/Backups/
Plex_HD/Documents/
Plex_HD/Archive/
```

Home Assistant backups may be stored under NAS backup paths.

---

# Home Assistant Project Files

Current relevant project folder:

```text
/nas/Documents/Projects/
```

Known project files include:

```text
Command_centre_Dashbaord.yaml
Garage Dashboard.yaml
html_command_centre.yaml
Rahmans_command_centre.html
RCC_noc_closer_match.yaml
RCC_v3_near_1to1.yaml
Target_NOC_Dashboard_Mockup.jpg
tuya_services.yaml
```

These relate to command centre dashboards, NOC/God’s Eye View dashboards, Tuya services, and smart home UI work.

When modifying dashboard YAML:

1. Preserve a backup.
2. Avoid overwriting working versions.
3. Create versioned outputs when experimenting.
4. Keep raw YAML valid.
5. Prefer iterative changes over full rewrites unless requested.

---

# Home Assistant Dashboard Philosophy

Tonmoy likes:

- “God’s Eye View” / NOC-style dashboards
- Service health cards
- Network topology visuals
- Dynamic status colours
- HTML-card-style topology layouts
- Clean command centre views
- Practical control panels

Known custom Lovelace/HACS resources may include:

- auto-entities
- bubble-card
- button-card
- card-mod
- expander-card
- html-card
- layout-card
- kiosk-mode
- mushroom

When designing dashboards:

- Prioritise clear operational visibility.
- Group systems logically.
- Show health/status first.
- Avoid clutter.
- Make it useful on wall/tablet displays.
- Prefer readable names and strong hierarchy.

---

# MealPrep Integration Context

MealPrep source of truth:

```text
/nas/Documents/MealPrep/
```

Important files:

```text
Meal_Plan.md
Shopping_List.md
README.md
config/Household_Preferences.md
config/Meal_Generation_Rules.md
config/Pantry_Assumptions.md
inventory/Pantry_Inventory.md
Recipes/
```

Known automation concept:

- NAS is source of truth.
- Home Assistant may sync or parse MealPrep markdown into sensors/dashboards.
- Shopping list may integrate with iCloud Reminders via Shortcuts/webhooks.
- Managed blocks should be used where syncing to avoid overwriting human content.

Principle:

MealPrep files should remain human-readable and safe to edit manually.

---

# Kira / Hermes Operational Context

Kira is Tonmoy’s personal AI operator.

Current direction:

```text
Kira moved from OpenClaw/Omarchy toward Hermes/Mac Mini.
```

Important instruction:

Any old notes that assume Kira primarily runs on Omarchy laptop should be checked before use.

Kira should:

- Use NAS source-of-truth files.
- Keep generated drafts separate from source files.
- Log important operational changes.
- Ask before making risky system changes.
- Use specialist agents for coding, debugging, research, and long-running investigations.

Recommended Kira folder structure:

```text
/nas/Documents/Kira/
├── Context/
├── Runbooks/
├── Logs/
├── Agent_Notes/
└── Archive/
```

---

# Backup And Change Safety

Before major Home Assistant changes:

1. Create or confirm a recent HA backup.
2. Copy the current YAML/config file.
3. Validate configuration.
4. Apply changes.
5. Reload only the required integration if possible.
6. Restart HA only when necessary.
7. Document what changed.

Avoid:

- Blindly overwriting `/config/configuration.yaml`
- Making multiple unrelated changes at once
- Restarting HA without validation
- Breaking HomeKit-exposed entities without noting impact
- Removing working automations without backup

---

# Troubleshooting Principles

When diagnosing issues:

1. Confirm current host/IP.
2. Check whether the issue is HA, network, integration, or device-specific.
3. Check logs.
4. Test local connectivity first.
5. Confirm whether cloud services are involved.
6. Avoid assuming old architecture is current.
7. Prefer reversible fixes.
8. Document root cause and resolution.

Useful checks conceptually include:

```text
ping host
curl local endpoint
check HA logs
check add-on logs
check integration status
validate YAML
confirm entity IDs
confirm IP reservations
```

---

# Smart Home Decision Framework

Prefer solutions that are:

1. Reliable.
2. Local-first where practical.
3. Easy to recover.
4. Documented.
5. Maintainable.
6. Wife/family friendly.
7. Not dependent on a single fragile script.
8. Observable in dashboards.
9. Reversible.
10. Useful rather than just clever.

---

# Known Risk Areas

- Tuya cloud dependency.
- LocalTuya complexity.
- HomeKit entity exposure changes.
- HA restarts impacting family automations.
- Kira/Hermes migration state drift.
- Old documentation referring to previous HAOS/Mac Mini/Omarchy layouts.
- NAS mount availability.
- YAML dashboard syntax issues.
- Experimental dashboard files overwriting stable ones.

---

# Future Improvement Ideas

Potential useful future work:

- Create a canonical Home Assistant architecture diagram.
- Build HA runbook under `/nas/Documents/Kira/Runbooks/`.
- Create a dashboard versioning workflow.
- Create a NAS health dashboard.
- Add Kira operational status sensors to HA.
- Add Tailscale health monitoring.
- Improve backup visibility.
- Create household “service status” page.
- Document all static IPs and device roles.

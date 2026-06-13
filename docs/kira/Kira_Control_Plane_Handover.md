
# Kira Control Plane – Architecture & Setup Handover

Author: Tonmoy Rahman  
Location: Wellington, New Zealand  
System Name: **Kira**

---

# 1. Purpose of the System

Kira is a **personal AI control plane** currently running on the Mac Mini that:

- Executes local system actions
- Controls the smart home via Home Assistant
- Interfaces with the user via messaging (Telegram)
- Can later manage other devices (Mac Mini, storage, network)

Design goal:

> Operate the system via natural language while maintaining safe execution boundaries.

---

# 2. System Architecture

```
Telegram
   ↓
Hermes Agent (Kira) Gateway
   ↓
Local Exec Tool
   ↓
Action System
   ↓
Home Assistant API / Local System
```

Principles:

- AI should not run arbitrary commands
- All meaningful actions flow through `action_runner.sh`
- Execution restricted by Hermes exec allowlist
- Elevated actions require predefined scripts

---

# 3. Host Machine

Device: Mac Mini  
Host: `Macmini`  
User: `tonmoyrahman`

Workspace:

```
/Users/tonmoyrahman/Kira
```

Legacy note: Kira originally ran on the Omarchy Linux laptop at `/home/tonmoy/kira`. Omarchy references below are historical unless marked as an active Linux-node integration.

Hermes config:

```
~/.hermes/config.yaml
```

Gateway port:

```
18789
```

---

# 4. Hermes Agent Configuration

File:

```
~/.hermes/config.yaml
```

Important settings:

```json
{
  "agents": {
    "defaults": {
      "workspace": "/Users/tonmoyrahman/Kira",
      "model": {
        "primary": "openai/gpt-5.4"
      }
    }
  },
  "tools": {
    "profile": "coding"
  }
}
```

Purpose:

- Enables filesystem tools
- Enables exec capability
- Sets workspace for AI operations

---

# 5. Exec Security Model

File:

```
~/.hermes/exec-approvals.json
```

Key configuration:

```json
"defaults": {
  "security": "allowlist",
  "ask": "off"
}
```

Behavior:

| Condition | Behaviour |
|-----------|-----------|
Allowlisted command | runs automatically |
Not allowlisted | denied |

---

# 6. Exec Allowlist

Allowed executables:

```
/usr/bin/bash
/bin/bash
/usr/bin/env
/usr/bin/pwd
/usr/bin/ls
/usr/bin/cat
/usr/bin/sed
/usr/bin/jq
/usr/bin/curl
/usr/bin/date
/usr/bin/tail
/usr/bin/stat
/usr/bin/chmod
```

Kira scripts:

```
/Users/tonmoyrahman/Kira/actions/action_runner.sh
/Users/tonmoyrahman/Kira/actions/system_status.sh
/Users/tonmoyrahman/Kira/actions/update_system.sh
```

---

# 7. Kira Workspace Structure

```
~/kira
├── actions
│   ├── action_runner.sh
│   ├── system_status.sh
│   ├── restart_service.sh
│   └── update_system.sh
│
├── config
│   ├── action_registry.json
│   └── ha.env
│
├── logs
│
└── scripts
```

---

# 8. Action System

Primary entrypoint:

```
~/kira/actions/action_runner.sh
```

Responsibilities:

- validate requested action
- check registry
- execute mapped script
- log action
- enforce sudo rules

---

# 9. Action Registry

File:

```
~/kira/config/action_registry.json
```

Example:

```json
{
  "system_status": {
    "script": "/Users/tonmoyrahman/Kira/actions/system_status.sh",
    "mode": "read_only",
    "sudo_required": false
  }
}
```

Modes:

| Mode | Meaning |
|-----|------|
read_only | safe automatic action |
ask_first | requires confirmation |
sudo_required | elevated |

---

# 10. Sudo Restrictions

File:

```
/etc/sudoers.d/kira-actions
```

Allowed commands:

```
restart_service.sh
update_system.sh
```

Meaning:

- Kira cannot run arbitrary sudo
- Only these scripts can escalate

---

# 11. Home Assistant Integration

Home Assistant:

```
http://192.168.50.166:8123
```

Configuration file:

```
~/kira/config/ha.env
```

Example:

```bash
HA_URL="http://192.168.50.166:8123"
HA_TOKEN="REDACTED"
HA_TIMEOUT_SECONDS="10"
```

Token is a Home Assistant long‑lived access token.

---

# 12. Security Model

Protection layers:

### Layer 1 – Exec Allowlist
Only known executables allowed.

### Layer 2 – Action System
All actions routed through controlled scripts.

### Layer 3 – Sudo Boundary
Only predefined scripts can escalate.

---

# 13. Current Capabilities

Kira can currently:

- Execute local commands
- Inspect filesystem
- Run action scripts
- Manage system status
- Access Home Assistant API

---

# 14. Next Planned Work

Future improvements:

### Home Assistant Actions

Scripts to create:

```
ha_get_status.sh
ha_entities.sh
ha_state.sh
ha_service.sh
```

### Automatic Home Assistant Discovery

Entity mapping:

```
climate.*
cover.*
light.*
switch.*
```

### Mac Mini Integration

Planned SSH access rules:

Allowed:
- write files
- read logs
- manage configs

Not allowed:
- delete files
- destructive commands

---

# 15. Communication Interface

Primary interface:

```
Telegram Bot
```

Flow:

```
User → Telegram → Hermes → Kira → Action System
```

---

# 16. Important Notes

Secrets that must be rotated after setup:

- Telegram bot token
- Hermes gateway auth token

---

# 17. Operating Philosophy

The system is designed as a **controlled AI operations layer**, not a free shell.

Core rule:

> AI proposes, action system executes.

---

# 18. Recovery Instructions

Check gateway:

```
hermes gateway status
```

Verify approvals:

```
hermes approvals get --gateway
```

Restart gateway:

```
hermes gateway restart
```

---

# 19. Project Status

Current milestone:

**Kira Control Plane v1 operational**

Working components:

- Hermes gateway
- Exec capability
- Action runner
- Exec allowlist
- Home Assistant connectivity

---

# 20. Maintainer

Tonmoy Rahman

Interests:

- Data engineering
- AI control systems
- Home automation
- philosophy and technology

Family:

- Wife: Esha
- Daughter: Sophie
- Son expected March 2026

---

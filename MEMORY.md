# MEMORY.md (Long-Term Curated)

## User Profile & Preferences
- Human: Tonmoy Rahman.
- **Birthday:** January 17th, 1987.
- **Family:**
  - Esha — birthday September 22nd, 1995.
  - Sophie — birthday August 9th, 2021.
  - Kian — born March 25th, 2026. 🎉
- Prefers practical, implementation-first help and persistence that survives token/session resets.
- Prefers auto-push to remote after successful coding/tasks (unless explicitly asked not to push).
- Interested in AI control systems, home automation, and robust operational setup.
- Tonmoy’s self-understanding lens, not a diagnosis: systems-minded long-term builder; strong internal locus of control; values agency, disciplined self-responsibility, intellectual humility, practical stoicism, and compounding progress. He combines curiosity with execution, questions assumptions deeply, and prefers truth over comfort or unquestionable certainty. Core motivators: mastery, autonomy, building useful things, respected expertise, durable systems, and leaving things better than he found them. Growth edges: update self-concept toward principal architect / head-of-data / consultancy-founder, carry responsibility more lightly, avoid over-responsibility and harsh self-accountability, act on avoided high-leverage work in small reps, and do not confuse productive solitude with emotional stillness. Useful mantra: “Build calmly. Choose carefully. Do the avoided work. Do not carry what is not yours.”
- 2026-06-14 health reset goal: lose ~12 kg in ~4 months after gaining weight from less gym, more eating, and lower movement. Context: `context/personal/health-fitness-reset-2026.md`; tracker: `tasks/health-fitness-12kg-4months.md`; support skill: `health-fitness-coach`.
- Whiro Analytics should now prioritise sales motion over more setup: build 10 warm contacts, send soft outreach/referral messages, aim for 2 discovery calls and 1 small paid Power BI Health Check. Lead tracking is in Microsoft Lists, not a markdown prospect tracker.
- For work/job-related tasks, professional profile updates, LinkedIn changes, and job advert tailoring, use the appropriate folder within `nas/Documents/Work/` as the default context/location.
- Generate new CVs as HTML files by default under `nas/Documents/Work/`. Only create Markdown or PDF versions when explicitly requested.

## Active System Context (Kira)
- Workspace: `/Users/tonmoyrahman/Kira` on the Mac Mini.
- Runtime: **Hermes Agent** — fully migrated from OpenClaw as of 2026-06-13.
- Kira runs as a controlled operations layer (action-runner pattern), not an unrestricted shell.
- Documentation source of truth is `docs/README.md` plus `docs/kira/*`, `docs/system-map.md`, `docs/runbooks/*`.

## Persistence Architecture (2026-03-08)
- Implemented durable identity + recovery:
  - `system/kira_identity.md`
  - `system/boot_prompt.md`
  - `docs/session_state.md`
  - `tasks/{README,active,backlog,done}.md`
  - `BOOT.md`
  - `scripts/kira-resume.sh`
  - `docs/kira/Kira_Persistence_Setup.md`
- `AGENTS.md` startup sequence now requires reading the above recovery files each session.

## Automation
- Daily cron reminder added for persistence maintenance:
  - Name: `Daily Kira session-state refresh`
  - Time: 07:15 Pacific/Auckland
  - Purpose: refresh `docs/session_state.md`, `tasks/*`, and daily memory; send concise status when important changes occur.

## Smart-Home Direction
- User plans a universal morning Alexa briefing, triggered by phrases like “good morning” / “what do I have today?”.
- Desired briefing sources: guest unit status, personal calendar, reminders (including iOS reminders), and optionally Outlook/work calendar.
- Direct Alexa account/device administration by Kira is limited; bridge via Home Assistant + routines/webhooks is the practical path.
- Home Assistant endpoint used by Kira: `http://192.168.50.166:8123`.
- 2026-05-23: Kira can reach Home Assistant at `http://192.168.50.166:8123`. The HA account `kira` is verified as an admin user (`auth/current_user.is_admin=true`), can read `/api/states` and `/api/services`, and can list auth users via websocket. A long-lived token is stored privately at `/Users/tonmoyrahman/Kira/secrets/homeassistant.env` with `0600` permissions. Do not store the password/token in memory.
- Home Assistant now runs on a dedicated Wyse 5070 thin client (`192.168.50.166`) with HAOS on bare metal (`generic-x86-64`), independent of the Mac Mini and VMware.
- Current home network device map: Wyse 5070 HAOS `192.168.50.166`; Mac Mini Kira/Hermes/Plex/NAS host `192.168.50.208`; Omarchy Laptop `192.168.50.28`; ASUS router/gateway `192.168.50.1`; Gree Controller `192.168.50.188`; Neo Controller `192.168.50.224`; Tuya Zigbee Gateway `192.168.50.100`.
- Mac Mini (`192.168.50.208`) no longer hosts HA and no longer runs Tailscale subnet routing; it continues serving Plex, NAS/SMB, and auxiliary services.
- 2026-06-13: **Full Kira workspace consolidation** — `context/`, `tools/`, and `mealprep/` all moved from NAS into `~/Kira/`. NAS `Documents/Kira/` and `Documents/MealPrep/` removed entirely. All scripts/skills updated to default to `~/Kira/` paths. All directories renamed to lowercase-kebab convention (`Context/` → `context/`, `ha_config_staging/` → `ha-config-staging/`, etc.).
- Migration status as of 2026-05-15: bare-metal HAOS installation complete; backup restore still pending.
- 2026-05-16: Post-migration, Home Assistant Supervisor had lost its SMB backup mount definitions. Recreated `plex_hd_backups_homeassistant` as a CIFS backup mount to `192.168.50.208` share `Plex_HD/Backups/HomeAssistant` and set it as the default backup mount again.

## Token-Limit / Session-Reset Recovery SOP
When context gets compacted or session resets, recovery should follow this durable sequence:
1. Update/read `docs/session_state.md` (objective, last done, next step).
2. Update/read `tasks/active.md` and `tasks/done.md`.
3. Append key events to `memory/YYYY-MM-DD.md`.
4. Promote durable facts/decisions to `MEMORY.md`.
5. Use `/Users/tonmoyrahman/Kira/scripts/kira-resume.sh` for quick recovery view.

## Multi-Agent Notes
- User asked about multiple agents and inter-agent communication; answer is yes to both.
- Recommended pattern: keep `main` as personal Kira and use additional specialist sessions/agents for isolated heavy work.

## Operational Notes
- Telegram group allowlist policy may need explicit sender IDs if group messaging is desired.

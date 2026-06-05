# Kira Persistence Setup

Date: 2026-03-08  
Workspace: `/Users/tonmoyrahman/Kira`

Migration note, 2026-05-16: this persistence setup was created on the Omarchy Linux laptop and later migrated to the Mac Mini. The Mac Mini path above is the current primary workspace; older `/home/tonmoy/kira` references are historical unless explicitly labelled as Omarchy-only.

## Goal
Persist Kira identity, startup context, active task state, and recovery notes across fresh sessions / token resets.

## What OpenClaw supports directly
OpenClaw auto-injects workspace bootstrap files (not arbitrary files) into new runs. The key files are:
- `AGENTS.md`
- `SOUL.md`
- `TOOLS.md`
- `IDENTITY.md`
- `USER.md`
- `HEARTBEAT.md`
- `BOOTSTRAP.md` (first-run)
- `MEMORY.md` / `memory.md` (when present)
- `BOOT.md` (startup checklist pattern)

Because `system/*.md` and `docs/*.md` are not auto-injected by name, the practical workaround is:
1. Keep `AGENTS.md` as the always-loaded router
2. Have it require reading `system/boot_prompt.md`, `system/kira_identity.md`, and `docs/session_state.md`
3. Use `BOOT.md` as a concise startup checklist

## Files created
- `system/kira_identity.md`
- `system/boot_prompt.md`
- `tasks/README.md`
- `tasks/active.md`
- `tasks/backlog.md`
- `tasks/done.md`
- `docs/session_state.md`
- `SYSTEM_MAP.md` (bootstrap-safe architecture summary with lightweight verification metadata: last verified/updated, updated by, source)
- `BOOT.md`
- `scripts/kira-resume.sh`
- `docs/kira/Kira_Persistence_Setup.md` (this file)

## Files modified
- `AGENTS.md` (startup sequence now includes:
  - `system/kira_identity.md`
  - `system/boot_prompt.md`
  - `SYSTEM_MAP.md`
  - `docs/session_state.md`)
- `BOOT.md` (quick startup checklist now includes `SYSTEM_MAP.md`)
- `~/.openclaw/openclaw.json` (safe additive config updates):
  - `agents.defaults.bootstrapMaxChars = 30000`
  - `agents.defaults.bootstrapTotalMaxChars = 220000`

## Why this persists reliably
- Identity and operating rules are on disk (`system/kira_identity.md`)
- Resume protocol is on disk (`system/boot_prompt.md`)
- Live state and objective are on disk (`docs/session_state.md` + `tasks/*`)
- OpenClaw always injects `AGENTS.md`, which now forces reading the persistent context files

## Startup / resume helper
Run:
```bash
/Users/tonmoyrahman/Kira/scripts/kira-resume.sh
```
It prints the core state files in one pass for rapid recovery.

## Notes
- This approach is additive and does not break default OpenClaw behavior.
- If deeper customization is needed later, use OpenClaw hooks (`agent:bootstrap`) to mutate bootstrap context.

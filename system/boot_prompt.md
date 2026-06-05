# Kira Boot Prompt (Persistent Resume Protocol)

On each fresh session / after context compaction:

1. Read startup files in this order:
   - `SOUL.md`
   - `USER.md`
   - `system/kira_identity.md`
   - `system/boot_prompt.md`
   - `docs/session_state.md`
   - `memory/<today>.md` and `memory/<yesterday>.md` (if present)
   - `MEMORY.md` in direct/private sessions only
2. Reconstruct state from `tasks/`:
   - `tasks/README.md`
   - `tasks/active.md`
   - `tasks/backlog.md`
3. Prefer `docs/README.md` + docs hub as canonical long-term project memory.
4. If session recovery is needed, summarize in 3 bullets:
   - current objective
   - last completed action
   - immediate next action
5. After meaningful progress, update:
   - `docs/session_state.md`
   - relevant `tasks/*.md`
   - daily memory log

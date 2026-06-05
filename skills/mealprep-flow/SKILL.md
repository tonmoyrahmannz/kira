---
name: mealprep-flow
description: Run and maintain Tonmoy's MealPrep automation flow (Apple Reminders to NAS Shopping_List.md to Home Assistant sync) with one deterministic command and consistent diagnostics. Use when the user asks to run or fix MealPrep sync, verify reminders import health, troubleshoot bridge/NAS/HA failures, or replace long manual prompts with a repeatable workflow.
---

# MealPrep Flow

Run the whole MealPrep pipeline with one command, then report a concise status.

## Quick run

Execute:

```bash
~/kira/skills/mealprep-flow/scripts/run_mealprep_flow.sh
```

The wrapper now derives the workspace root dynamically and respects:
- `ROOT`
- `NAS_ROOT`
- `NAS_MEALPREP_DIR`
- `NAS_REMINDERS_STATUS_JSON`

Success criteria:
- command exits `0`
- output contains `OK: MealPrep flow completed`
- status file is present and shows `ok` or `ok_no_changes`

## What this skill runs

1. `~/kira/scripts/reminders_to_nas_shopping_sync.sh`
2. `~/kira/scripts/sync_mealprep_to_ha.sh`

It keeps the correct order and prints structured failure context.

## Response format for users

After running, return:
- **Result:** success/failure
- **What changed:** imported item count + whether markdown changed
- **Next action:** only if failed

Keep it short and actionable.

## Troubleshooting flow

If command fails:
1. Read `NAS_REMINDERS_STATUS_JSON` or the default status file under `${NAS_MEALPREP_DIR}/.status/reminders_import_status.json`.
2. If `failed_no_bridge`, verify local `osascript` availability first; if running off-Mac, verify `REMINDERS_BRIDGE_SSH`.
3. If NAS issues, verify `${NAS_MEALPREP_DIR}`.
4. If HA sync step fails, re-run `~/kira/scripts/sync_mealprep_to_ha.sh` and surface the first actionable error line.

## Reference

For paths and known-good signals, read:
`references/flow-reference.md`

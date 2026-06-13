# MealPrep Flow Reference

## Canonical paths
- Workspace root: `~/Kira` by convention; wrapper script can derive this dynamically
- MealPrep data folder default: `~/Kira/mealprep`
- Reminders→NAS script: `~/Kira/scripts/reminders_to_nas_shopping_sync.sh`
- NAS→HA script: `~/Kira/scripts/sync_mealprep_to_ha.sh`
- Reminders status JSON default: `~/Kira/mealprep/.status/reminders_import_status.json`

## Supported overrides
- `ROOT`
- `WORKSPACE_ROOT`
- `NAS_ROOT`
- `NAS_MEALPREP_DIR`
- `NAS_SHOPPING_FILE`
- `NAS_SHOPPING_BACKUP_DIR`
- `NAS_REMINDERS_STATUS_JSON`
- `SRC_BASE`
- `LOCAL_MEAL_PARSER`
- `LOCAL_SHOPPING_PARSER`

## Bridge behavior
- `reminders_to_nas_shopping_sync.sh` now prefers local `osascript` when available.
- Use `REMINDERS_BRIDGE_SSH=user@host` only when Reminders must be read from another Mac.
- Use `REMINDERS_ITEMS_FILE=/path/to/test_items.txt` for test mode.

## Healthy run signals
- Script output includes:
  - `No markdown changes needed.` or successful sync line
  - `MealPrep sync run completed.`
- Status JSON usually reports:
  - `status: ok` or `ok_no_changes`
  - `items_imported >= 0`

## Fast failure checks
1. `failed_no_bridge` in status JSON → local `osascript` unavailable and no valid `REMINDERS_BRIDGE_SSH`/test input supplied.
2. Data path missing → check `~/Kira/mealprep` or your overridden MealPrep path.
3. HA sync fails → run `sync_mealprep_to_ha.sh` directly and inspect the first actionable error line.

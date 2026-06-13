#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${ROOT:-$(cd -- "$SCRIPT_DIR/../../.." && pwd)}"
NAS_ROOT="${NAS_ROOT:-${HOME}/Kira}"
NAS_MEALPREP_DIR="${NAS_MEALPREP_DIR:-${NAS_ROOT}/mealprep}"
PAUSE_FILE="${MEALPREP_PAUSE_FILE:-${NAS_MEALPREP_DIR}/.status/paused}"
SYNC_REMINDERS="$ROOT/scripts/reminders_to_nas_shopping_sync.sh"
SYNC_HA="$ROOT/scripts/sync_mealprep_to_ha.sh"
STATUS_JSON="${NAS_REMINDERS_STATUS_JSON:-${NAS_MEALPREP_DIR}/.status/reminders_import_status.json}"

STEP1_OUT=""
STEP2_OUT=""

if [[ -f "$PAUSE_FILE" ]]; then
  echo "OK: MealPrep flow paused"
  echo "pause_file: $PAUSE_FILE"
  cat "$PAUSE_FILE" || true
  exit 0
fi

if [[ ! -x "$SYNC_REMINDERS" ]]; then
  echo "ERROR: missing executable $SYNC_REMINDERS" >&2
  exit 2
fi

if [[ ! -x "$SYNC_HA" ]]; then
  echo "ERROR: missing executable $SYNC_HA" >&2
  exit 2
fi

if ! STEP1_OUT="$($SYNC_REMINDERS 2>&1)"; then
  echo "FAILED: reminders→NAS sync"
  echo "$STEP1_OUT"
  if [[ -f "$STATUS_JSON" ]]; then
    echo "STATUS_JSON: $STATUS_JSON"
    tail -n 20 "$STATUS_JSON" || true
  fi
  exit 1
fi

if ! STEP2_OUT="$($SYNC_HA 2>&1)"; then
  echo "FAILED: NAS→HA sync"
  echo "$STEP2_OUT"
  exit 1
fi

echo "OK: MealPrep flow completed"
[[ -n "$STEP1_OUT" ]] && echo "reminders_sync: $STEP1_OUT"
[[ -n "$STEP2_OUT" ]] && echo "ha_sync: $STEP2_OUT"

if [[ -f "$STATUS_JSON" ]]; then
  echo "status_file: $STATUS_JSON"
  tail -n 12 "$STATUS_JSON" || true
fi

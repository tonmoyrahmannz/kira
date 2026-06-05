#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="${WORKSPACE_ROOT:-$(cd -- "$SCRIPT_DIR/.." && pwd)}"
NAS_ROOT="${NAS_ROOT:-${HOME}/nas}"
HA_HOST="${HA_HOST:-192.168.50.166}"
HA_PORT="${HA_PORT:-22}"
HA_USER="${HA_USER:-root}"
HA_KEY="${HA_KEY:-${HOME}/.ssh/id_ed25519_kira_ha}"

SRC_BASE="${SRC_BASE:-${NAS_ROOT}/Documents/MealPrep}"
SRC_PLAN="$SRC_BASE/Meal_Plan.md"
SRC_SHOPPING="$SRC_BASE/Shopping_List.md"
SRC_RECIPES="$SRC_BASE/Recipes"

DST_BASE="/config/mealprep"
STATUS_DIR="$DST_BASE/.status"
REMOTE_MEAL_PARSER="/config/scripts/mealprep_parser.sh"
REMOTE_SHOPPING_PARSER="/config/scripts/shopping_parser.sh"
REMOTE_PACKAGE="/config/packages/mealprep_sync_observability.yaml"
LOCAL_MEAL_PARSER="${LOCAL_MEAL_PARSER:-${WORKSPACE_ROOT}/tmp/mealprep_parser.sh}"
LOCAL_SHOPPING_PARSER="${LOCAL_SHOPPING_PARSER:-${WORKSPACE_ROOT}/scripts/shopping_parser.sh}"

need_cmd() { command -v "$1" >/dev/null 2>&1 || { echo "Missing required command: $1" >&2; exit 1; }; }
need_cmd ssh
need_cmd scp
need_cmd tar
need_cmd python3

[ -f "$SRC_PLAN" ] || { echo "Source plan missing: $SRC_PLAN" >&2; exit 1; }
[ -f "$SRC_SHOPPING" ] || { echo "Source shopping list missing: $SRC_SHOPPING" >&2; exit 1; }
[ -d "$SRC_RECIPES" ] || { echo "Source recipes dir missing: $SRC_RECIPES" >&2; exit 1; }
[ -f "$LOCAL_MEAL_PARSER" ] || { echo "Missing local parser: $LOCAL_MEAL_PARSER" >&2; exit 1; }
[ -f "$LOCAL_SHOPPING_PARSER" ] || { echo "Missing local parser: $LOCAL_SHOPPING_PARSER" >&2; exit 1; }

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$TMP_DIR/mealprep/Recipes"
cp "$SRC_PLAN" "$TMP_DIR/mealprep/Meal_Plan.md"
cp "$SRC_SHOPPING" "$TMP_DIR/mealprep/Shopping_List.md"
find "$SRC_RECIPES" -maxdepth 1 -type f -name '*.md' -exec cp {} "$TMP_DIR/mealprep/Recipes/" \;

if ! find "$TMP_DIR/mealprep/Recipes" -maxdepth 1 -type f -name '*.md' | grep -q .; then
  echo "No recipe markdown files found in source: $SRC_RECIPES" >&2
  exit 1
fi

read -r SOURCE_HASH SOURCE_LAST_MODIFIED <<EOF
$(python3 - "$TMP_DIR/mealprep" "$SRC_PLAN" "$SRC_SHOPPING" "$SRC_RECIPES" <<'PY'
import hashlib
import sys
from pathlib import Path

mealprep_dir = Path(sys.argv[1])
src_plan = Path(sys.argv[2])
src_shopping = Path(sys.argv[3])
src_recipes = Path(sys.argv[4])

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

entries = []
for path in sorted((mealprep_dir / 'Recipes').glob('*.md')):
    entries.append(f"{sha256_file(path)}  {path.name}")
entries.insert(0, f"{sha256_file(mealprep_dir / 'Shopping_List.md')}  Shopping_List.md")
entries.insert(0, f"{sha256_file(mealprep_dir / 'Meal_Plan.md')}  Meal_Plan.md")
source_hash = hashlib.sha256(('\n'.join(entries) + '\n').encode()).hexdigest()
mtimes = [p.stat().st_mtime for p in [src_plan, src_shopping] + sorted(src_recipes.glob('*.md'))]
latest = int(max(mtimes)) if mtimes else 0
print(source_hash, latest)
PY
)
EOF

TARBALL="$TMP_DIR/mealprep.tar"
tar -C "$TMP_DIR" -cf "$TARBALL" mealprep

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "mkdir -p /config/scripts /config/packages /config/custom_components/mealprep_shopping_webhook $DST_BASE $STATUS_DIR /config/www/mealprep"

scp -i "$HA_KEY" -P "$HA_PORT" "$TARBALL" "$HA_USER@$HA_HOST:/tmp/mealprep_sync.tar"
scp -i "$HA_KEY" -P "$HA_PORT" "$LOCAL_MEAL_PARSER" "$HA_USER@$HA_HOST:$REMOTE_MEAL_PARSER"
scp -i "$HA_KEY" -P "$HA_PORT" "$LOCAL_SHOPPING_PARSER" "$HA_USER@$HA_HOST:$REMOTE_SHOPPING_PARSER"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "chmod +x $REMOTE_MEAL_PARSER $REMOTE_SHOPPING_PARSER"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "cat > '$REMOTE_PACKAGE' <<'YAML'
sensor:
  - platform: command_line
    name: mealprep_last_sync
    unique_id: mealprep_last_sync
    command: \"cat /config/mealprep/.status/last_sync_iso 2>/dev/null || echo never\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_sync_status
    unique_id: mealprep_sync_status
    command: \"cat /config/mealprep/.status/sync_status 2>/dev/null || echo unknown\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_parse_status
    unique_id: mealprep_parse_status
    command: \"cat /config/mealprep/.status/parse_status 2>/dev/null || echo unknown\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_source_last_modified
    unique_id: mealprep_source_last_modified
    command: \"cat /config/mealprep/.status/source_last_modified_iso 2>/dev/null || echo unknown\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_shopping_last_parse
    unique_id: mealprep_shopping_last_parse
    command: \"cat /config/mealprep/.status/shopping_last_parse_iso 2>/dev/null || echo never\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_shopping_parse_status
    unique_id: mealprep_shopping_parse_status
    command: \"cat /config/mealprep/.status/shopping_parse_status 2>/dev/null || echo unknown\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_shopping_items_count
    unique_id: mealprep_shopping_items_count
    command: \"cat /config/mealprep/.status/shopping_items_count 2>/dev/null || echo 0\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_reminders_import_last_sync
    unique_id: mealprep_reminders_import_last_sync
    command: \"cat /config/mealprep/.status/reminders_import_last_sync_iso 2>/dev/null || echo never\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_reminders_import_status
    unique_id: mealprep_reminders_import_status
    command: \"cat /config/mealprep/.status/reminders_import_status 2>/dev/null || echo unknown\"
    scan_interval: 60

  - platform: command_line
    name: mealprep_reminders_import_items_count
    unique_id: mealprep_reminders_import_items_count
    command: \"cat /config/mealprep/.status/reminders_import_items_count 2>/dev/null || echo 0\"
    scan_interval: 60
YAML"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "cat > /config/custom_components/mealprep_shopping_webhook/manifest.json <<'JSON'
{
  \"domain\": \"mealprep_shopping_webhook\",
  \"name\": \"MealPrep Shopping Webhook\",
  \"version\": \"1.0.0\",
  \"documentation\": \"https://docs.openclaw.ai\",
  \"requirements\": [],
  \"codeowners\": [\"@tonmoy\"],
  \"iot_class\": \"local_push\"
}
JSON"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "cat > /config/custom_components/mealprep_shopping_webhook/__init__.py <<'PY'
from __future__ import annotations

import json
from pathlib import Path

from aiohttp import web

from homeassistant.components import webhook
from homeassistant.core import HomeAssistant

DOMAIN = \"mealprep_shopping_webhook\"
WEBHOOK_ID = \"mealprep_shopping_sync\"
SHOPPING_JSON = Path(\"/config/www/mealprep/shopping_list.json\")


def _safe_payload() -> dict:
    if not SHOPPING_JSON.exists():
        return {\"items\": []}
    try:
        data = json.loads(SHOPPING_JSON.read_text(encoding=\"utf-8\"))
    except Exception:
        return {\"items\": []}
    items = data.get(\"items\", []) if isinstance(data, dict) else []
    if not isinstance(items, list):
        items = []
    clean_items = [str(i) for i in items if isinstance(i, str) and i.strip()]
    return {\"items\": clean_items}


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    async def _handle(hass: HomeAssistant, webhook_id: str, request):
        return web.json_response(_safe_payload())

    webhook.async_register(
        hass,
        DOMAIN,
        \"MealPrep Shopping Sync\",
        WEBHOOK_ID,
        _handle,
        allowed_methods=(\"GET\", \"POST\"),
    )
    return True
PY"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "grep -q '^mealprep_shopping_webhook:' /config/configuration.yaml || printf '\nmealprep_shopping_webhook:\n' >> /config/configuration.yaml"

ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" \
  "SOURCE_HASH='$SOURCE_HASH' SOURCE_LAST_MODIFIED='$SOURCE_LAST_MODIFIED' DST_BASE='$DST_BASE' STATUS_DIR='$STATUS_DIR' REMOTE_MEAL_PARSER='$REMOTE_MEAL_PARSER' REMOTE_SHOPPING_PARSER='$REMOTE_SHOPPING_PARSER' sh -s" <<'REMOTE'
set -eu

now_iso() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
write_status() {
  mkdir -p "$STATUS_DIR"
  printf "%s" "$(now_iso)" > "$STATUS_DIR/last_sync_iso"
  printf "%s" "${SYNC_STATUS:-unknown}" > "$STATUS_DIR/sync_status"
  printf "%s" "${PARSE_STATUS:-unknown}" > "$STATUS_DIR/parse_status"
  printf "%s" "${SHOPPING_PARSE_STATUS:-unknown}" > "$STATUS_DIR/shopping_parse_status"
  printf "%s" "${SHOPPING_ITEMS_COUNT:-0}" > "$STATUS_DIR/shopping_items_count"
  printf "%s" "${SHOPPING_LAST_PARSE:-never}" > "$STATUS_DIR/shopping_last_parse_iso"
  printf "%s" "${REMINDERS_IMPORT_LAST_SYNC:-never}" > "$STATUS_DIR/reminders_import_last_sync_iso"
  printf "%s" "${REMINDERS_IMPORT_STATUS:-unknown}" > "$STATUS_DIR/reminders_import_status"
  printf "%s" "${REMINDERS_IMPORT_ITEMS_COUNT:-0}" > "$STATUS_DIR/reminders_import_items_count"
  printf "%s" "${REMINDERS_IMPORT_BACKUP_PATH:-}" > "$STATUS_DIR/reminders_import_backup_path"
  printf "%s" "${SOURCE_LAST_MODIFIED:-unknown}" > "$STATUS_DIR/source_last_modified_epoch"
  if [ "${SOURCE_LAST_MODIFIED:-0}" -gt 0 ] 2>/dev/null; then
    date -u -d "@${SOURCE_LAST_MODIFIED}" +"%Y-%m-%dT%H:%M:%SZ" > "$STATUS_DIR/source_last_modified_iso"
  else
    printf "%s" "unknown" > "$STATUS_DIR/source_last_modified_iso"
  fi
}

mkdir -p "$DST_BASE" "$STATUS_DIR"

HASH_FILE="$STATUS_DIR/source_hash"
PREV_HASH=""
[ -f "$HASH_FILE" ] && PREV_HASH="$(cat "$HASH_FILE" 2>/dev/null || true)"
REMINDERS_IMPORT_LAST_SYNC="$(cat "$STATUS_DIR/reminders_import_last_sync_iso" 2>/dev/null || echo never)"
REMINDERS_IMPORT_STATUS="$(cat "$STATUS_DIR/reminders_import_status" 2>/dev/null || echo unknown)"
REMINDERS_IMPORT_ITEMS_COUNT="$(cat "$STATUS_DIR/reminders_import_items_count" 2>/dev/null || echo 0)"
REMINDERS_IMPORT_BACKUP_PATH="$(cat "$STATUS_DIR/reminders_import_backup_path" 2>/dev/null || true)"

if [ -n "$PREV_HASH" ] && [ "$PREV_HASH" = "$SOURCE_HASH" ]; then
  SYNC_STATUS="unchanged"
  PARSE_STATUS="skipped_unchanged"
  SHOPPING_PARSE_STATUS="skipped_unchanged"
  SHOPPING_ITEMS_COUNT="$(cat "$STATUS_DIR/shopping_items_count" 2>/dev/null || echo 0)"
  SHOPPING_LAST_PARSE="$(cat "$STATUS_DIR/shopping_last_parse_iso" 2>/dev/null || echo never)"
  write_status
  exit 0
fi

STAGE_DIR="/config/.mealprep_stage_$$"
BACKUP_DIR="/config/.mealprep_prev"
MEAL_JSON_OUT="/config/www/mealprep/todays_meal.json"
MEAL_JSON_BAK="/config/www/mealprep/todays_meal.lastgood.json"
SHOPPING_JSON_OUT="/config/www/mealprep/shopping_list.json"
SHOPPING_JSON_BAK="/config/www/mealprep/shopping_list.lastgood.json"

rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR"

tar -C "$STAGE_DIR" -xf /tmp/mealprep_sync.tar
mv "$STAGE_DIR/mealprep" "$STAGE_DIR/new"

[ -f "$STAGE_DIR/new/Meal_Plan.md" ] || { SYNC_STATUS="failed_validation_missing_plan"; PARSE_STATUS="not_run"; SHOPPING_PARSE_STATUS="not_run"; write_status; exit 1; }
[ -f "$STAGE_DIR/new/Shopping_List.md" ] || { SYNC_STATUS="failed_validation_missing_shopping"; PARSE_STATUS="not_run"; SHOPPING_PARSE_STATUS="not_run"; write_status; exit 1; }
ls "$STAGE_DIR/new/Recipes"/*.md >/dev/null 2>&1 || { SYNC_STATUS="failed_validation_missing_recipes"; PARSE_STATUS="not_run"; SHOPPING_PARSE_STATUS="not_run"; write_status; exit 1; }

[ -f "$MEAL_JSON_OUT" ] && cp "$MEAL_JSON_OUT" "$MEAL_JSON_BAK" || true
[ -f "$SHOPPING_JSON_OUT" ] && cp "$SHOPPING_JSON_OUT" "$SHOPPING_JSON_BAK" || true

rm -rf "$BACKUP_DIR"
[ -d "$DST_BASE" ] && mv "$DST_BASE" "$BACKUP_DIR" || true
mv "$STAGE_DIR/new" "$DST_BASE"
rm -rf "$STAGE_DIR"

if [ ! -x "$REMOTE_MEAL_PARSER" ]; then
  rm -rf "$DST_BASE"
  [ -d "$BACKUP_DIR" ] && mv "$BACKUP_DIR" "$DST_BASE" || true
  [ -f "$MEAL_JSON_BAK" ] && cp "$MEAL_JSON_BAK" "$MEAL_JSON_OUT" || true
  [ -f "$SHOPPING_JSON_BAK" ] && cp "$SHOPPING_JSON_BAK" "$SHOPPING_JSON_OUT" || true
  SYNC_STATUS="rolled_back_parser_missing"
  PARSE_STATUS="parser_missing"
  SHOPPING_PARSE_STATUS="not_run"
  write_status
  exit 1
fi

if ! "$REMOTE_MEAL_PARSER" >/dev/null 2>&1; then
  rm -rf "$DST_BASE"
  [ -d "$BACKUP_DIR" ] && mv "$BACKUP_DIR" "$DST_BASE" || true
  [ -f "$MEAL_JSON_BAK" ] && cp "$MEAL_JSON_BAK" "$MEAL_JSON_OUT" || true
  [ -f "$SHOPPING_JSON_BAK" ] && cp "$SHOPPING_JSON_BAK" "$SHOPPING_JSON_OUT" || true
  SYNC_STATUS="rolled_back_parse_failed"
  PARSE_STATUS="failed"
  SHOPPING_PARSE_STATUS="not_run"
  write_status
  exit 1
fi

PARSED_STATUS="$(jq -r '.status // "unknown"' "$MEAL_JSON_OUT" 2>/dev/null || echo unknown)"
if [ "$PARSED_STATUS" != "ok" ]; then
  rm -rf "$DST_BASE"
  [ -d "$BACKUP_DIR" ] && mv "$BACKUP_DIR" "$DST_BASE" || true
  [ -f "$MEAL_JSON_BAK" ] && cp "$MEAL_JSON_BAK" "$MEAL_JSON_OUT" || true
  [ -f "$SHOPPING_JSON_BAK" ] && cp "$SHOPPING_JSON_BAK" "$SHOPPING_JSON_OUT" || true
  SYNC_STATUS="rolled_back_parse_failed"
  PARSE_STATUS="failed"
  SHOPPING_PARSE_STATUS="not_run"
  write_status
  exit 1
fi

PARSE_STATUS="ok"

if [ -x "$REMOTE_SHOPPING_PARSER" ] && "$REMOTE_SHOPPING_PARSER" >/dev/null 2>&1; then
  SHOPPING_PARSE_STATUS="$(cat "$STATUS_DIR/shopping_parse_status" 2>/dev/null || echo ok)"
  SHOPPING_ITEMS_COUNT="$(cat "$STATUS_DIR/shopping_items_count" 2>/dev/null || echo 0)"
  SHOPPING_LAST_PARSE="$(cat "$STATUS_DIR/shopping_last_parse_iso" 2>/dev/null || echo never)"
else
  SHOPPING_PARSE_STATUS="failed"
  SHOPPING_ITEMS_COUNT="$(cat "$STATUS_DIR/shopping_items_count" 2>/dev/null || echo 0)"
  SHOPPING_LAST_PARSE="$(cat "$STATUS_DIR/shopping_last_parse_iso" 2>/dev/null || echo never)"
fi

mkdir -p "$STATUS_DIR"
printf "%s" "$SOURCE_HASH" > "$HASH_FILE"
rm -rf "$BACKUP_DIR"
SYNC_STATUS="ok"
write_status
exit 0
REMOTE

echo "MealPrep sync run completed."

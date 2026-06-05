#!/usr/bin/env sh
set -eu

MEAL_DIR="/config/mealprep"
STATUS_DIR="$MEAL_DIR/.status"
SRC="$MEAL_DIR/Shopping_List.md"
OUT="/config/www/mealprep/shopping_list.json"
BAK="/config/www/mealprep/shopping_list.lastgood.json"
TMP="/tmp/shopping_list.$$.$RANDOM.json"

now_iso() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

mkdir -p /config/www/mealprep "$STATUS_DIR"

write_status() {
  status="$1"
  count="$2"
  printf "%s" "$(now_iso)" > "$STATUS_DIR/shopping_last_parse_iso"
  printf "%s" "$status" > "$STATUS_DIR/shopping_parse_status"
  printf "%s" "$count" > "$STATUS_DIR/shopping_items_count"
}

[ -f "$OUT" ] && cp "$OUT" "$BAK" || true

if [ ! -f "$SRC" ]; then
  write_status "missing_source" "0"
  [ -f "$BAK" ] && cp "$BAK" "$OUT" || printf '{"items":[]}' > "$OUT"
  exit 1
fi

ITEMS_TMP="/tmp/shopping_items.$$.$RANDOM.txt"
trap 'rm -f "$TMP" "$ITEMS_TMP"' EXIT

awk '
  BEGIN {
    in_need=0
  }
  /^##[[:space:]]+NEED TO BUY[[:space:]]*$/ { in_need=1; next }
  /^##[[:space:]]+PANTRY ASSUMED[[:space:]]*$/ { in_need=0; exit }
  in_need {
    if ($0 ~ /^[[:space:]]*-[[:space:]]+/) {
      line=$0
      sub(/^[[:space:]]*-[[:space:]]+/, "", line)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", line)
      if (line == "") next

      low=line
      for (i=1;i<=length(low);i++) {
        c=substr(low,i,1)
        if (c ~ /[A-Z]/) {
          low=substr(low,1,i-1) tolower(c) substr(low,i+1)
        }
      }

      if (line ~ /:$/) next
      if (low == "produce") next
      if (low == "meat / seafood") next
      if (low == "dairy / eggs") next
      if (low == "pantry / dry goods") next
      if (low == "sauces / pastes") next

      print line
    }
  }
' "$SRC" > "$ITEMS_TMP"

COUNT="$(grep -c '.' "$ITEMS_TMP" || true)"

if [ "${COUNT:-0}" -eq 0 ]; then
  write_status "failed_empty_items" "0"
  [ -f "$BAK" ] && cp "$BAK" "$OUT" || printf '{"items":[]}' > "$OUT"
  exit 1
fi

jq -R -s 'split("\n") | map(select(length>0)) | {items:.}' "$ITEMS_TMP" > "$TMP"

if jq -e '.items and (.items | type == "array") and (all(.items[]; type == "string"))' "$TMP" >/dev/null 2>&1; then
  mv "$TMP" "$OUT"
  cp "$OUT" "$BAK"
  write_status "ok" "$COUNT"
  exit 0
fi

write_status "failed_invalid_json" "0"
[ -f "$BAK" ] && cp "$BAK" "$OUT" || printf '{"items":[]}' > "$OUT"
exit 1

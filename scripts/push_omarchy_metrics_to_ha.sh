#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
METRIC_SCRIPT="$BASE_DIR/scripts/omarchy_kira_metrics.sh"
HA_ENV="$BASE_DIR/config/ha.env"

if [[ ! -f "$HA_ENV" ]]; then
  echo "Missing $HA_ENV" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$HA_ENV"

if [[ -z "${HA_URL:-}" || -z "${HA_TOKEN:-}" ]]; then
  echo "HA_URL/HA_TOKEN missing in $HA_ENV" >&2
  exit 1
fi

api_post() {
  local entity_id="$1"
  local payload="$2"
  curl -sS -X POST \
    -H "Authorization: Bearer ${HA_TOKEN}" \
    -H "Content-Type: application/json" \
    "${HA_URL}/api/states/${entity_id}" \
    -d "$payload" >/dev/null
}

# Gather metrics once per run
omarchy_cpu="$($METRIC_SCRIPT cpu)"
omarchy_mem="$($METRIC_SCRIPT memory)"
omarchy_disk="$($METRIC_SCRIPT disk)"
omarchy_gpu="$($METRIC_SCRIPT gpu)"
omarchy_tailscale="$($METRIC_SCRIPT tailscale_connected)"
omarchy_last_seen="$($METRIC_SCRIPT last_seen)"

openclaw_running="$($METRIC_SCRIPT openclaw_running)"
openclaw_pid="$($METRIC_SCRIPT openclaw_pid)"
openclaw_mem_mb="$($METRIC_SCRIPT openclaw_memory_mb)"
kira_heartbeat="$($METRIC_SCRIPT heartbeat)"

omarchy_online="on"
kira_online="on"

# Omarchy entities
api_post "binary_sensor.omarchy_online" "{\"state\":\"${omarchy_online}\",\"attributes\":{\"friendly_name\":\"omarchy_online\",\"device_class\":\"connectivity\"}}"
api_post "sensor.omarchy_cpu_usage" "{\"state\":\"${omarchy_cpu}\",\"attributes\":{\"friendly_name\":\"omarchy_cpu_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.omarchy_memory_usage" "{\"state\":\"${omarchy_mem}\",\"attributes\":{\"friendly_name\":\"omarchy_memory_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.omarchy_disk_usage" "{\"state\":\"${omarchy_disk}\",\"attributes\":{\"friendly_name\":\"omarchy_disk_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.omarchy_gpu_usage" "{\"state\":\"${omarchy_gpu}\",\"attributes\":{\"friendly_name\":\"omarchy_gpu_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "binary_sensor.omarchy_tailscale_connected" "{\"state\":\"$( [[ \"$omarchy_tailscale\" == \"ON\" ]] && echo on || echo off )\",\"attributes\":{\"friendly_name\":\"omarchy_tailscale_connected\",\"device_class\":\"connectivity\"}}"
api_post "sensor.omarchy_last_seen" "{\"state\":\"${omarchy_last_seen}\",\"attributes\":{\"friendly_name\":\"omarchy_last_seen\",\"device_class\":\"timestamp\"}}"

# Kira/OpenClaw service entities
api_post "binary_sensor.kira_online" "{\"state\":\"${kira_online}\",\"attributes\":{\"friendly_name\":\"kira_online\",\"device_class\":\"connectivity\"}}"
api_post "binary_sensor.kira_openclaw_running" "{\"state\":\"$( [[ \"$openclaw_running\" == \"ON\" ]] && echo on || echo off )\",\"attributes\":{\"friendly_name\":\"kira_openclaw_running\",\"device_class\":\"running\"}}"
api_post "sensor.kira_cpu_usage" "{\"state\":\"${omarchy_cpu}\",\"attributes\":{\"friendly_name\":\"kira_cpu_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.kira_memory_usage" "{\"state\":\"${omarchy_mem}\",\"attributes\":{\"friendly_name\":\"kira_memory_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.kira_disk_usage" "{\"state\":\"${omarchy_disk}\",\"attributes\":{\"friendly_name\":\"kira_disk_usage\",\"unit_of_measurement\":\"%\",\"state_class\":\"measurement\"}}"
api_post "sensor.kira_openclaw_pid" "{\"state\":\"${openclaw_pid}\",\"attributes\":{\"friendly_name\":\"kira_openclaw_pid\"}}"
api_post "sensor.kira_openclaw_memory_mb" "{\"state\":\"${openclaw_mem_mb}\",\"attributes\":{\"friendly_name\":\"kira_openclaw_memory_mb\",\"unit_of_measurement\":\"MB\",\"state_class\":\"measurement\"}}"
api_post "sensor.kira_last_heartbeat" "{\"state\":\"${kira_heartbeat}\",\"attributes\":{\"friendly_name\":\"kira_last_heartbeat\",\"device_class\":\"timestamp\"}}"

echo "Pushed Omarchy/Kira telemetry to Home Assistant at $(date --iso-8601=seconds)"

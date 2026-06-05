#!/usr/bin/env bash
set -euo pipefail

metric="${1:-}"
service="${OPENCLAW_SERVICE_NAME:-openclaw-gateway.service}"

cpu_usage() {
  awk -v FS='[ ]+' '/^cpu / {u=$2+$4; t=$2+$4+$5; if (t>0) printf "%.1f\n", (u/t)*100; else print "0.0"}' /proc/stat
}

memory_usage() {
  awk '/MemTotal/ {t=$2} /MemAvailable/ {a=$2} END {if (t>0) printf "%.1f\n", ((t-a)/t)*100; else print "0.0"}' /proc/meminfo
}

disk_usage() {
  df -P / | awk 'NR==2 {gsub(/%/,"",$5); print $5+0}'
}

openclaw_pid() {
  local pid
  pid="$(systemctl --user show -p MainPID --value "$service" 2>/dev/null || echo 0)"
  if [[ -z "$pid" || "$pid" == "0" ]]; then
    echo 0
  else
    echo "$pid"
  fi
}

openclaw_running() {
  if systemctl --user is-active --quiet "$service"; then
    echo ON
  else
    echo OFF
  fi
}

openclaw_memory_mb() {
  local pid rss_kb
  pid="$(openclaw_pid)"
  if [[ "$pid" == "0" ]]; then
    echo 0
    return
  fi

  rss_kb="$(ps -o rss= -p "$pid" 2>/dev/null | awk '{print $1}' || true)"
  if [[ -z "$rss_kb" ]]; then
    echo 0
  else
    awk -v kb="$rss_kb" 'BEGIN {printf "%.1f\n", kb/1024}'
  fi
}

tailscale_connected() {
  if command -v tailscale >/dev/null 2>&1 && tailscale ip -4 >/dev/null 2>&1; then
    echo ON
  else
    echo OFF
  fi
}

heartbeat() {
  if systemctl --user is-active --quiet "$service"; then
    date --iso-8601=seconds
  else
    echo ""
  fi
}

last_seen() {
  date --iso-8601=seconds
}

case "$metric" in
  cpu)
    cpu_usage
    ;;
  memory)
    memory_usage
    ;;
  disk)
    disk_usage
    ;;
  gpu)
    # Placeholder until a stable Linux GPU probe is selected for Omarchy.
    echo 0
    ;;
  openclaw_running)
    openclaw_running
    ;;
  openclaw_pid)
    openclaw_pid
    ;;
  openclaw_memory_mb)
    openclaw_memory_mb
    ;;
  tailscale_connected)
    tailscale_connected
    ;;
  heartbeat)
    heartbeat
    ;;
  last_seen)
    last_seen
    ;;
  service_name)
    echo "$service"
    ;;
  *)
    echo "unknown metric: $metric" >&2
    exit 2
    ;;
esac

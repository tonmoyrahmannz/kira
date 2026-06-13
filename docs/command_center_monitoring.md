
# Rahman's Command Centre – Core Systems Monitoring

## Project Context
This README documents the first phase of building a **Home Infrastructure Command Centre** inside Home Assistant.  
The goal is to create a **single operational dashboard** that shows the health of all core systems in Rahman's home lab environment.

This work was performed with the help of **Kira (automation agent)** which modified Home Assistant configuration and dashboards.

---

# Architecture Overview

The monitoring architecture follows a **Machine Layer → Service Layer** model.

Omarchy Laptop
- OpenClaw Gateway (Kira) — retired 2026-06-13, migrated to Hermes
- Automation scripts
- Telemetry script

Mac Mini
- Home Assistant VM

NAS
- Storage services

Machines are monitored separately from services running on them.

---

# Dashboard: Rahman's Command Centre

A new section called **Core Systems** was added to the Home Assistant dashboard at URL path `rahman-command-centre` (display title: **Rahman's Command Centre**).

## Card Order

1. System Health (Home Assistant)
2. MacMini Health
3. NAS Overview
4. Kira Gateway Health
5. Omarchy Laptop Health

This establishes a consistent **infrastructure monitoring layer**.

---

# Core Systems Telemetry

## Home Assistant
Monitored using the `system_monitor` integration.

Metrics include:
- CPU usage
- Memory usage
- Disk usage
- Network throughput
- Load average
- Last boot time
- System updates

---

## Mac Mini

Sensors:
- macmini_cpu_usage
- macmini_gpu_usage
- macmini_memory_usage
- macmini_storage_usage

---

## NAS

Sensors:
- nas_online
- nas_total_usage
- nas_media_usage_percent
- nas_documents_usage_percent
- nas_backups_usage_percent
- nas_archive_usage_percent

A pie chart card visualizes storage distribution.

---

# Omarchy Laptop Monitoring

Sensors created:

- binary_sensor.omarchy_online
- sensor.omarchy_cpu_usage
- sensor.omarchy_memory_usage
- sensor.omarchy_disk_usage
- sensor.omarchy_gpu_usage (placeholder)
- binary_sensor.omarchy_tailscale_connected
- sensor.omarchy_last_seen

Metrics retrieved via SSH polling from Home Assistant.

---

# Kira Gateway Monitoring

Kira Gateway is implemented as the **Hermes Agent running on the Mac Mini**.

Systemd service detected:
hermes-gateway.service

Sensors:

- binary_sensor.kira_online
- binary_sensor.kira_openclaw_running
- sensor.kira_cpu_usage
- sensor.kira_memory_usage
- sensor.kira_disk_usage
- sensor.kira_openclaw_pid
- sensor.kira_openclaw_memory_mb
- sensor.kira_last_heartbeat

---

# Telemetry Implementation

Home Assistant collects Omarchy/Kira metrics using:

### Ping Sensor
Detect if Omarchy is reachable.

### Command Line Sensors
Executed via SSH from Home Assistant to Omarchy.

### Remote Script

/home/tonmoy/kira/scripts/omarchy_kira_metrics.sh

Provides:
- CPU usage
- Memory usage
- Disk usage
- Tailscale connectivity
- Kira/Hermes process state
- PID
- Memory usage
- Heartbeat timestamp

---

# Configuration Changes

Home Assistant package updated:

/config/packages/core_systems_placeholders.yaml

Placeholder entities were replaced with **live telemetry sensors**.

---

# Git Changes

Example commit:

491a26c – Wire Omarchy and Kira/Hermes core telemetry to live sensors

---

# Current Status

The dashboard now provides:

• Infrastructure health monitoring  
- Kira/Hermes service visibility  
• Remote system metrics for Omarchy  
• NAS storage visibility  
• Mac Mini resource monitoring  

This forms the **Core Systems monitoring layer**.

---

# Future Planned Improvements

## Phase 2 – Status Overview Row

Create a top status bar showing:

HA | MacMini | NAS | Omarchy | Hermes | Internet

with green / amber / red indicators.

---

## Phase 3 – Service Monitoring

Add cards for:

- Plex
- MQTT
- Zigbee
- Tailscale
- Network connectivity

---

## Phase 4 – Infrastructure Map

Internet
│
Router
│
MacMini → Home Assistant  
NAS  
Omarchy → Hermes  

---

# Operational Goal

Create a **home-scale NOC (Network Operations Center)** where all machines and services can be monitored from a single Home Assistant dashboard.

---

Maintainer:  
Tonmoy Rahman

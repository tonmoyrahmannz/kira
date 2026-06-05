# Rahman's Command Centre -- Home Infrastructure Dashboard Plan

## Overview

This document outlines a scalable Home Assistant dashboard architecture
to monitor and control the entire home infrastructure from a single
"God's Eye View". The goal is to build a mini **home NOC (Network
Operations Center)** inside Home Assistant.

The dashboard will provide real‑time visibility into: - Core
infrastructure systems - Compute nodes - Key services - Network health -
Future IoT device monitoring

This architecture is designed to grow over time and integrates well with
automation, alerts, and telemetry.

------------------------------------------------------------------------

# High Level Dashboard Layout

    Rahman's Command Centre
    -------------------------------------------------
    | Home Assistant | Mac Mini | NAS | Router |
    -------------------------------------------------
    | Kira Gateway | Omarchy Laptop | Network |
    -------------------------------------------------
    | Services: OpenClaw | Plex | MQTT | Zigbee |
    -------------------------------------------------

------------------------------------------------------------------------

# System Categories

## 1. Core Infrastructure

These systems run critical services.

Cards: - Home Assistant - Mac Mini (HA VM host) - NAS - Router / Gateway

Metrics to display: - Online / Offline - CPU usage - RAM usage - Disk
usage - System uptime - Temperature (optional)

------------------------------------------------------------------------

## 2. Compute Nodes

### Kira Gateway

Runs OpenClaw automation system.

Metrics: - OpenClaw process running - CPU usage - RAM usage - PID -
Browser worker count - Last heartbeat

Possible automations: - Alert if OpenClaw stops - Restart gateway
automatically - Telegram notification if offline

------------------------------------------------------------------------

### Omarchy Laptop

Metrics: - Online / Offline - CPU usage - RAM usage - Disk usage - GPU
usage (optional) - Tailscale connection state - SSH reachability

------------------------------------------------------------------------

# Service Layer

Examples: - OpenClaw Gateway - Home Assistant Supervisor - Plex Media
Server - MQTT Broker - Zigbee Network - Tailscale VPN

These cards monitor application-level health rather than system health.

Example metrics: - service running / stopped - port reachable -
container status - response time

------------------------------------------------------------------------

# Network Monitoring (Future Expansion)

Possible cards: - Internet connectivity - Router CPU / RAM - WiFi device
count - Tailscale nodes - DNS health

Possible metrics: - latency - packet loss - bandwidth - active devices

------------------------------------------------------------------------

# Dashboard Implementation Strategy

Recommended approach:

## Step 1 -- Create System Cards

One card per device:

-   Home Assistant
-   Mac Mini
-   NAS
-   Kira Gateway
-   Omarchy Laptop

Benefits: - scalable - easy to monitor - easy to automate alerts

------------------------------------------------------------------------

## Step 2 -- Add Service Health Checks

Monitor: - OpenClaw - Plex - MQTT - Zigbee - Tailscale

These can be built using: - command_line sensors - MQTT sensors - REST
sensors

------------------------------------------------------------------------

## Step 3 -- Implement MQTT Telemetry

Best long‑term architecture:

Each system publishes metrics like:

    home/kira/status
    home/kira/cpu
    home/kira/memory
    home/kira/heartbeat

Home Assistant subscribes and renders dashboard cards.

Advantages: - lightweight - scalable - real‑time updates

------------------------------------------------------------------------

# Example Home Assistant Card Layout

## System Card Example

    Kira Gateway

    Status: Online
    OpenClaw: Running
    CPU: 3%
    Memory: 800 MB
    Last Seen: 13:31

------------------------------------------------------------------------

# Recommended Dashboard Sections

## Core Systems

-   Home Assistant
-   Mac Mini
-   NAS
-   Router

## Compute Nodes

-   Kira Gateway
-   Omarchy Laptop

## Services

-   OpenClaw
-   Plex
-   MQTT
-   Zigbee

## Network

-   Internet health
-   WiFi status
-   Tailscale nodes

------------------------------------------------------------------------

# Future Expansion Ideas

## Full Infrastructure Map

Create a visual topology showing:

    Internet
       |
    Router
       |
    Switch
       |
    ---------------------------
    | Mac Mini | NAS | Laptop |
    ---------------------------
            |
          Home Assistant
            |
          Devices / IoT

This can be implemented using: - Picture elements cards - Mermaid
diagrams - Custom HA dashboards

------------------------------------------------------------------------

# Potential Automation Examples

### OpenClaw Failure Alert

If OpenClaw process stops:

-   Send Telegram alert
-   Attempt automatic restart
-   Mark system as degraded

### NAS Disk Warning

If disk usage \> 90%:

-   Send alert
-   highlight dashboard card

### Omarchy Laptop Offline

If unreachable for \>5 minutes:

-   change card color
-   send notification

------------------------------------------------------------------------

# Suggested Dashboard Name

Recommended name:

**Rahman's Command Centre**

Alternative ideas: - Home Ops Dashboard - Infrastructure Control -
Rahman NOC - System Command

------------------------------------------------------------------------

# Long Term Vision

Eventually this dashboard becomes a complete operational control center
for:

-   infrastructure monitoring
-   automation status
-   service health
-   network visibility
-   device management

The result is a **home-scale operations center similar to a data center
control dashboard**.

------------------------------------------------------------------------

# Integration with Kira

This document can also be used to generate automation prompts for
Kira/OpenClaw to:

-   deploy telemetry scripts
-   publish system metrics
-   create Home Assistant sensors
-   build dashboard cards
-   implement automated recovery workflows

------------------------------------------------------------------------

End of document.

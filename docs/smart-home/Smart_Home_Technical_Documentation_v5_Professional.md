
# Smart Home Infrastructure Architecture Document
## Enterprise Technical Specification (v5)

**Owner:** Tonmoy Rahman  
**Primary Residence Network:** 192.168.50.0/24  
**Router / Gateway:** 192.168.50.1  
**macOS Host (Mac Mini M1):** 192.168.50.208  
**Tailscale IP (Mac Mini):** 100.78.16.33  
**Primary Automation Platform:** Home Assistant OS (HAOS)  
**Deployment Model:** VMware Fusion (Apple Silicon ARM64)  
**Last Updated:** 2026-03-03

---
# 1. Executive Summary

This document defines the production-grade architecture of the residential smart home infrastructure.
The environment is designed using layered architecture principles, secure remote access controls, 
local-first integrations, and disaster recovery readiness.

The system provides:

- Native multicast (mDNS) support
- No Docker NAT dependencies
- No Homebridge middleware
- Secure global access via WireGuard (Tailscale)
- Documented failure recovery procedures
- Segmentation-ready network design

The architecture is classified as:

> **Production-Grade Residential Smart Infrastructure**

---
# 2. Architecture Overview (Layered Model)

## 2.1 Layer 1 – Physical Infrastructure
- Router / Gateway: 192.168.50.1
- Mac Mini (M1): 192.168.50.208
- Apple TV (Home Hub)
- Gree HVAC Controller: 192.168.50.188
- Neo Smart Blinds Controller: 192.168.50.224
- Wi-Fi Network: Tonmoy&Esha

## 2.2 Layer 2 – Virtualization Layer
- Hypervisor: VMware Fusion (Apple Silicon)
- Guest OS: HAOS ARM64
- Network Mode: Bridged (en0)
- VM Resource Allocation:
  - CPU: 2 cores
  - RAM: 4GB
  - Disk: 32GB
  - Auto-start: Enabled
  - Restart on failure: Enabled

## 2.3 Layer 3 – Application Layer
- Home Assistant Core
- Supervisor
- Add-on Framework
- Custom Components:
  - Gree Zone Control
  - Neo Smart Blinds

## 2.4 Layer 4 – Integration Layer
- Gree HVAC (TCP 7000, encrypted key)
- Neo Smart Blinds (TCP 8839, local-only)
- HomeKit Bridge (mDNS multicast)
- Apple TV acting as Home Hub

## 2.5 Layer 5 – Remote Access Layer
- Tailscale (WireGuard encrypted overlay network)
- Subnet routing enabled: 192.168.50.0/24
- macOS SSH enabled
- No public port forwarding

---
# 3. Local Network Topology

```
Internet
    |
[Router 192.168.50.1]
    |
+-- Mac Mini 192.168.50.208
|       |
|       +-- VMware Fusion
|              |
|              +-- HAOS VM 192.168.50.x:8123
|
+-- Gree Controller 192.168.50.188:7000
+-- Neo Blinds Controller 192.168.50.224:8839
+-- Apple TV (Home Hub)
```

---
# 4. Remote Access Topology

```
Remote Device
      |
   Tailscale
      |
Mac Mini (100.78.16.33)
      |
Subnet Route 192.168.50.0/24
      |
Home Assistant VM (192.168.50.x)
```

---
# 5. Service Communication Matrix

| Source | Destination | Protocol | Port | Encryption |
|--------|------------|----------|------|------------|
| HAOS | Gree | TCP | 7000 | Encrypted (Key Based) |
| HAOS | Neo Blinds | TCP | 8839 | Local TCP |
| HAOS | Apple TV | mDNS | 5353 | Secure HomeKit |
| Remote Device | Mac Mini | WireGuard | N/A | Encrypted |
| SSH Client | Mac Mini | SSH | 22 | Encrypted |

---
# 6. High Availability & Resilience

## 6.1 Single Points of Failure
- Mac Mini hardware
- Router (192.168.50.1)
- Power availability

## 6.2 Recommended Enhancements
- UPS for Router + Mac Mini
- Ethernet fallback instead of Wi-Fi
- Scheduled automated HA backups

---
# 7. Failure Mode & Impact Assessment

| Component | Failure Scenario | Impact | Recovery Time (Est.) |
|------------|-----------------|--------|----------------------|
| Router | Offline | Entire LAN down | 5–15 min |
| Mac Mini | Power loss | HA offline | 5 min |
| VMware | VM crash | HA unavailable | <2 min (auto restart) |
| HAOS | Corruption | Restore required | 20–30 min |
| Tailscale | Outage | Remote unavailable | Immediate local fallback |

---
# 8. RTO / RPO Targets

| Metric | Target |
|--------|--------|
| RTO (Recovery Time Objective) | < 30 minutes |
| RPO (Recovery Point Objective) | < 24 hours |
| Backup Frequency | Manual + Monthly |
| Backup Storage | Local HA snapshot |

---
# 9. Disaster Recovery Playbook

## Scenario A – HAOS Corruption
1. Deploy new HAOS ARM VM
2. Allocate 32GB disk
3. Restore Full Backup
4. Validate integrations
5. Reconfirm HomeKit pairing

## Scenario B – Mac Mini Hardware Failure
1. Replace hardware
2. Install VMware Fusion
3. Deploy HAOS ARM VM
4. Restore backup
5. Reconfigure Tailscale subnet routing

## Scenario C – Network Failure
1. Restart Router (192.168.50.1)
2. Confirm Mac Mini IP 192.168.50.208
3. Validate HAOS reachability

---
# 10. Network Segmentation Strategy (Future State)

Current: Flat LAN (192.168.50.0/24)

Recommended VLAN Model:

| VLAN | CIDR | Purpose |
|------|------|---------|
| VLAN 10 | 192.168.10.0/24 | Core Infrastructure |
| VLAN 20 | 192.168.20.0/24 | IoT Devices |
| VLAN 30 | 192.168.30.0/24 | Guest Network |
| VLAN 40 | 192.168.40.0/24 | Management |

Firewall Rules:
- IoT → Allow to HA only
- Guest → No LAN access
- HA → Internet outbound allowed

---
# 11. Automation Inventory (Structural Overview)

| Automation | Trigger | Action | Priority |
|------------|---------|--------|----------|
| Night Cooling | 22:00 | HVAC Cool Mode | Medium |
| Morning Blinds | Sunrise | Open Covers | Low |
| Away Mode | No Presence | HVAC Eco | High |

(Full export available within HA UI)

---
# 12. Entity Inventory (Core Entities)

Climate:
- climate.ac_mode
- climate.kitchen_and_living
- climate.study
- climate.guest
- climate.master_bedroom

Covers:
- cover.dining_blind_1
- cover.dining_blind_2
- cover.living_room_blind
- cover.master_bedroom_blind
- cover.sophies_blind
- cover.study_blind

---
# 13. Security Posture

- No public inbound ports exposed
- WireGuard encrypted remote tunnel
- Encrypted HVAC communication
- Local-only blinds integration
- Apple secure HomeKit pairing
- SSH limited to authenticated user

Security Classification: **Low Exposure – Private Network Only**

---
# 14. Governance & Change Control

Change Management Process:
1. Document change
2. Take full backup
3. Apply update
4. Validate integrations
5. Update change log

---
# 15. Change Log

| Date | Change | Impact |
|------|--------|--------|
| 2026-02 | Migrated Docker → HAOS VM | Improved mDNS |
| 2026-03 | Removed Homebridge | Simplified stack |
| 2026-03 | Implemented Tailscale | Secure remote access |
| 2026-03 | Enterprise Documentation v5 | Formalized architecture |

---
# 16. Operational Maturity Assessment

Current Tier: **Tier 3 – Structured Home Infrastructure**

Characteristics:
- Documented architecture
- Backup validated
- Secure remote access
- Failure scenarios documented
- Change tracking implemented

---
**End of Professional Architecture Specification v5**

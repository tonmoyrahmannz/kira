
# Gree Ducted Air‑Conditioning RF Zoning Architecture
**System Design & Technical Documentation**

---

# 1. System Overview

This is a **Gree ducted air‑conditioning system** with RF zoning and Wi‑Fi cloud control enabled via the **G‑Cloud ecosystem**.

The architecture enables independent room airflow control using wireless thermostats, a master RF hub, and motorised dampers coordinated through a wired zoning interface.

---

# 2. Devices and Models

## 1) Master RF / Zone Controller Hub
**Model:** ACSG1802  
**System Name:** Gree G‑Cloud Zone Controller C13 Wi‑Fi – F1 (Single)  
**Location:** Attic / roof space near ducted indoor unit  

### Functions
- Receives RF signals from wireless room remotes  
- Acts as the central zoning logic controller  
- Sends open/close commands to motorised dampers  
- Communicates with the ducted indoor HVAC unit  
- Interfaces with the zone control interface  
- Provides Wi‑Fi / cloud connectivity via G‑Cloud app  

### Connectivity
- RF antenna for remote communication  
- Damper control outputs  
- Communication bus to indoor unit  
- Link to zone interface controller  
- Wi‑Fi connection to home router  

---

## 2) Zone Control Interface
**Model:** LE60-13/GH  
**Location:** Wall, service area, or ceiling cavity  

### Functions
- Physical wiring hub for zoning system  
- Controls up to 8 motorised dampers  
- Interfaces with wired wall controllers  
- Relays zone status and commands  
- Communicates with master RF controller  
- Connects to ducted indoor unit via RS485 / HBS  

### Ports
- Zone Damper 1–8 outputs  
- RS485 communication port  
- HBS communication port  
- Wired controller ports  
- Wi‑Fi module port  
- Antenna port  

---

## 3) RF Wireless Room Controllers
**Model:** Various Gree RF thermostats/remotes  

### Functions
- Sense room temperature  
- Allow users to request heating/cooling  
- Send RF commands to master controller  
- Enable per‑zone on/off and airflow control  

**Signal Type:** RF wireless  

---

## 4) Motorised Zone Dampers
**Model:** Various (duct-installed)  

### Functions
- Open/close airflow to each zone  
- Controlled by zone interface  
- Enable independent temperature control per room  

---

# 3. Architecture Diagram

```
G‑Cloud App (Wi‑Fi / Internet)
            │
            ▼
ACSG1802 Master RF Hub
            │
   ┌────────┼────────┐
   │        │        │
 RF       Bus      Wi‑Fi
   │        │
   ▼        ▼
Room     LE60-13/GH Interface
Remotes        │
               ▼
        Motorised Dampers
               │
               ▼
        Ducted Indoor Unit
```

---

# 4. Device Relationship Map

| Layer | Device | Model | Dependency |
|------|---------|--------|------------|
| Cloud | G‑Cloud App | — | Optional |
| Master | ACSG1802 | Critical | Central logic |
| Interface | LE60-13/GH | Critical | Damper control |
| Sensors | RF Controllers | Operational | Zone demand |
| Actuators | Dampers | Critical | Airflow |
| Plant | Indoor Unit | Critical | Air supply |

---

# 5. Signal Flow

1. Room remote detects temperature or user input  
2. RF signal sent to ACSG1802 master controller  
3. Master calculates airflow demand  
4. Command sent to LE60-13/GH interface  
5. შესაბამის dampers open or close  
6. Indoor unit adjusts airflow delivery  
7. Wi‑Fi module syncs to G‑Cloud app  

---

# 6. Troubleshooting Dependency Flow

```
No Cooling in Zone
        │
        ├─ RF Remote Battery?
        ├─ RF Signal to ACSG1802?
        ├─ Zone Command Issued?
        ├─ LE60-13/GH Output Active?
        ├─ Damper Moving?
        └─ Indoor Unit Airflow OK?
```

---

# 7. Failure Impact Analysis

## ACSG1802 Offline
- No RF reception  
- No zoning logic  
- Dampers default state  
- Cloud control lost  
**Severity: Critical**

## LE60-13/GH Failure
- Dampers non-responsive  
- Zones stuck open/closed  
**Severity: High**

## RF Remote Failure
- Single zone affected  
**Severity: Low**

## Wi‑Fi Failure
- App offline only  
**Severity: Non‑critical**

---

# 8. Smart Home Integration

### Native
- G‑Cloud mobile app  
- Scheduling  
- Remote control  

### Indirect
- IR bridge integration  
- Home Assistant automation  
- Alexa / Google Home linking  

---

# 9. Upgrade Options

- Expand dampers (≤8 per interface)  
- Add wired thermostats  
- Static pressure sensors  
- Demand‑based fan control  

---

# 10. Commissioning Best Practices

### RF
- Avoid antenna obstruction  
- Maintain ≤20 m distance  

### Airflow
- Install bypass duct  
- Balance static pressure  

### Network
- Use 2.4 GHz Wi‑Fi  
- DHCP reservation recommended  

---

# 11. End‑to‑End Sequence

```
Temp Rise → RF Call → ACSG1802 Logic →
Damper Opens → Indoor Unit Runs →
Setpoint Reached → Damper Closes →
Status Sync to Cloud
```

---

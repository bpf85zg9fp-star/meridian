---
document_id: "RFQ-1000-SH-001"
title: "Meridian Estate Smart Home — KNX Automation Backbone"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Smart home tech recommendations"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$180,000–$240,000 (KNX hardware, programming, commissioning)"
primary_supplier: "KNX-certified integrator (SA)"
---

# RFQ-1000-SH-001 — KNX Automation Backbone

## Overview

KNX is the primary automation backbone for the Meridian Estate. It controls lighting, HVAC, blinds, access, pool, irrigation, security sensors, and all building services. All other automation platforms (Josh.ai, Basalte, Lutron) integrate into or sit above KNX.

---

## 1. Architecture

- **Protocol:** KNX Secure (IP + TP) — encrypted bus communication
- **Topology:** Dual-bus with independent fallback paths; critical zones on separate bus segments
- **Infrastructure:** KNX TP cable throughout (during construction phase); KNXnet/IP routing between building sections
- **Programming:** ETS6 (Engineering Tool Software) — all group addresses, scenes, and logic programmed by KNX-certified integrator
- **Digital twin feed:** KNX state data exported to WillowTwin / EcoDomus for live building performance monitoring

## 2. Controlled Systems

| Domain | KNX function |
|---|---|
| Lighting | On/off, dim, colour temperature (DALI2 via DALI Gateway Plus) |
| HVAC | Hydronic zone control, temperature setpoints, HRV triggers |
| Blinds / Motorised shades | Open/close/position via Lutron Palladiom motor integration |
| Access control | Gate, garage doors, entry door lock sequences |
| Pool and irrigation | Pump, heating, chemical dosing, Hydrawise zone control |
| Security | Sensor arming, mmWave trigger zones, alarm integration (Inner Range Integriti) |
| Fire mode | Automated drencher activation, ember shutter deployment, lockdown sequence, drone launch trigger |
| Energy | Load-shedding logic, EV charging schedules, solar surplus routing |
| AV | Scene triggers for Christie Eclipse, Trinnov, Naim CI zones |
| Scent / diffusers | Zone-based essential oil diffuser activation |

## 3. Key Integration Points

| System | Integration method |
|---|---|
| Josh.ai | KNX IP gateway — Josh.ai reads and writes KNX group addresses via local API |
| Basalte Lena | Native KNX TP bus device |
| Lutron HomeWorks QS | KNX-Lutron gateway for blind motor and lighting coordination |
| Gira DALI Gateway Plus | DALI2 lighting bus via KNX |
| Inner Range Integriti | KNX-Integriti integration module |
| 2N IP Style intercoms | KNX relay for gate/door unlock triggers |
| WillowTwin | KNX IP data export for digital twin modelling |

## 4. Scene Architecture

All scenes are programmed as KNX group objects and exposed to Josh.ai and Basalte Lena for control. Scene library includes (non-exhaustive):

- Wellness Morning, Movie Mode, Goodnight, Entertain, Guest Arrival
- Fire Mode (automated on CFS alert integration)
- Hi-Res Listening, Gaming, Work/Conference
- Pool Heating On, Irrigation Cycle, EV Charge Eco Mode

## 5. Programming Standards

- All group addresses to be documented in ETS6 project file and provided to Kevin on handover
- Scene logic to be version-controlled in repository (`/continuum/` directory TBC)
- Change management: any modification to KNX programming must be documented and approved by Kevin before implementation

## 6. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| KNX TP cabling (installed during construction) | $35,000 |
| KNX IP routers, power supplies, line couplers | $25,000 |
| DALI Gateway Plus (×2) | $6,000 |
| KNX-IP gateway modules | $8,000 |
| ETS6 programming and commissioning | $80,000–$120,000 |
| Testing and handover documentation | $15,000 |
| **Total** | **$169,000–$209,000** |

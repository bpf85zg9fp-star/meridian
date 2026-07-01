---
document_id: "RFQ-1000-SH-003"
title: "Meridian Estate Smart Home — Basalte Lena Control Panels"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-003 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Smart home tech recommendations"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$90,000–$120,000 (18+ units, hardware + programming)"
primary_supplier: "Basalte / KNX integrator"
---

# RFQ-1000-SH-003 — Basalte Lena Control Panels

## Overview

Basalte Lena is the primary touch-control interface throughout the Meridian Estate. Installed in every room including all bathrooms (18+ units minimum), it provides scene control, HVAC, blinds, lighting, AV, and building status at a glance. The Basalte ecosystem also includes Sentido switches and Ellie entry-point panels.

---

## 1. Products

| Product | Function | Placement |
|---|---|---|
| Basalte Lena | 4" touchscreen wall panel — scene control, HVAC, lighting, AV | All rooms including all bathrooms |
| Basalte Sentido | Capacitive touch switch | Supplementary switching in corridors and secondary spaces |
| Basalte Chopin | Mechanical keypad | Utility and service areas |
| Basalte Ellie | Entry panel with intercom | All garage entry points, entry hall |
| Basalte Mirrored panels | Integrated into bathroom vanity mirrors | Master ensuites |

## 2. Lena Panel Capability

- Scene activation (all KNX scenes)
- HVAC temperature and mode control (per zone)
- Blind / shade position control
- Lighting dimming and colour temperature
- AV zone control (source, volume)
- Building status dashboard (pool temp, gate status, solar SOC, alarm)
- Floor plan view option (full building awareness from any panel)
- Wake-on-motion: panel sleeps and wakes on proximity

## 3. Placement Matrix (minimum)

| Location | Units |
|---|---|
| Master bedroom + ensuite | 2 |
| 5 remaining bedrooms + ensuites | 10 |
| VIP guest suite | 2 |
| Main lounge | 1 |
| Kitchen | 1 |
| Theatre | 1 |
| Home office | 1 |
| Garage (each entry point) | 3 |
| Pool pavilion | 1 |
| Entry gallery | 1 |
| Estate Command Centre | 2 |
| **Minimum total** | **25** |

## 4. KNX Integration

- All Basalte panels are native KNX TP bus devices
- Group addresses programmed in ETS6 in conjunction with KNX backbone programming
- Basalte Home app provides remote access and panel configuration
- Panel UI customised per zone (e.g., theatre panel shows only AV + lighting scenes)

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| 25× Basalte Lena panels | $62,500 |
| 10× Basalte Sentido switches | $8,000 |
| 4× Basalte Ellie entry panels | $6,000 |
| Programming and UI customisation | $18,000–$35,000 |
| Installation | $8,000 |
| **Total** | **$102,500–$119,500** |

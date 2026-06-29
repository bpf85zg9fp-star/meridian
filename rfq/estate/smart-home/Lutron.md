---
document_id: "RFQ-1000-SH-004"
title: "Meridian Estate Smart Home — Lutron Lighting & Shading"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-004 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$120,000–$160,000"
primary_supplier: "Lutron AU distributor"
---

# RFQ-1000-SH-004 — Lutron Lighting & Shading

## Overview

Lutron provides the motorised shading (Palladiom) and circadian lighting control (Ketra + HomeWorks QS) layers for the Meridian Estate, fully integrated with KNX and Josh.ai.

---

## 1. Products

| Product | Function |
|---|---|
| Lutron Palladiom shades | Dual-layer motorised roller blinds — blackout + sheer per window |
| Lutron Sivoia QS motors | Wired motors for Palladiom shades; native HomeWorks QS integration |
| Lutron HomeWorks QS | Central shade processor; KNX gateway integration |
| Lutron Ketra | Tunable white RGBW luminaires for circadian and wellness lighting |

## 2. Palladiom Shading

- **Configuration:** Dual-layer per window — sheer layer for daytime privacy + blackout layer for sleep and theatre
- **Control:** Preset positions via HomeWorks QS; KNX group address triggers from Josh.ai and Basalte
- **Bedrooms:** All bedrooms have electrochromic glass (SageGlass/Halio) supplemented by Palladiom blackout layer for full darkness and BAL-FZ compliance
- **Theatre:** Shades are independently controlled — Movie Mode scene closes all theatre shades to 100% blackout
- **BAL-FZ shutters:** Separate fire shutter system (EBSA) is not Lutron — it is a dedicated fire-rated system triggered independently via KNX fire logic

## 3. Ketra Circadian Lighting

- **Function:** Automatically adjusts colour temperature (2700 K – 6500 K) and intensity throughout the day following natural circadian rhythm
- **Wellness mode:** Ketra integrated with HRV data and time-of-day to modify lighting spectrum; morning energising (cool white); evening wind-down (warm amber)
- **AI biometric sync:** Ketra colour temperature modulated based on HRV/stress curve data from occupant wearables (integration point for wellness AI layer)
- **Zones:** All primary living areas, bedrooms, wellness suite, and kitchen

## 4. Integration

| System | Integration |
|---|---|
| KNX | HomeWorks QS – KNX gateway for shade position and scene triggers |
| Josh.ai | Native Lutron – Josh.ai integration; voice shade control |
| Basalte Lena | Shade position control on every panel |
| DALI2 / KNX | Ketra luminaires controlled via DALI2 bus linked to KNX |

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Lutron Palladiom shades (all windows, dual-layer) | $75,000–$100,000 |
| Sivoia QS motors | Included above |
| HomeWorks QS processor + KNX gateway | $12,000 |
| Lutron Ketra luminaires (primary zones) | $20,000–$30,000 |
| Programming and commissioning | $13,000–$18,000 |
| **Total** | **$120,000–$160,000** |

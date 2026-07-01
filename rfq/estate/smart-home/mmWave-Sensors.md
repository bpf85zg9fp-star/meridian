---
document_id: "RFQ-1000-SH-005"
title: "Meridian Estate Smart Home — mmWave Presence & Fall Detection Sensors"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-005 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-23 — mmWave vs beam cutters"
  - "2025-08-20 — Smart home tech recommendations"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$35,000–$50,000"
primary_supplier: "Vendor TBD (Aqara / Tuya enterprise / Senzary / Microwave Sensor OEM via KNX integrator)"
---

# RFQ-1000-SH-005 — mmWave Presence & Fall Detection Sensors

## Decision: mmWave over Beam/PIR

Planning conversations evaluated mmWave 60 GHz sensors vs beam cutters and PIR sensors. Decision: enterprise mmWave throughout. Reasons:
- Detects stationary presence (seated, sleeping) — PIR and beam cutters require motion
- Fall detection capability — critical for elderly occupant (mum, late 60s) and children
- No false negatives from slow movement
- No physical beam infrastructure to install or align
- Sub-centimetre accuracy for occupancy automation

---

## 1. Specification

| Parameter | Specification |
|---|---|
| Technology | 60 GHz mmWave FMCW radar |
| Coverage per unit | 5–10 m radius depending on model; ceiling or wall mount |
| Functions | Presence detection, zone tracking, fall detection, respiration sensing (premium models) |
| Integration | KNX via dry contact or IP gateway; some models native KNX TP |
| False positive rate | Near-zero vs PIR/beam |

## 2. Deployment

- **Every occupied room:** One mmWave sensor per room minimum; larger rooms (theatre, open plan) may require two
- **Bathrooms:** All ensuites and main bathrooms — fall detection priority
- **Wellness suite:** Critical zone — float tank, sauna, cold plunge all monitored
- **Garage:** Vehicle presence and occupant detection
- **Outdoor pavilion:** Pool safety monitoring zone
- Estimated units: 35–45 across entire estate

## 3. KNX Integration

- Presence state exposed as KNX binary group address — triggers lighting, HVAC, and security scenes
- HVAC: room becomes “occupied” — setpoint tightens; room becomes “vacant” — setpoint relaxes
- Lighting: lights follow occupant through house without manual switching
- Security: armed mode treats unexpected presence as intrusion trigger
- Fall detection: emergency KNX trigger — alerts household and can trigger emergency call sequence

## 4. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| 40× mmWave sensors (supply) | $20,000–$32,000 |
| KNX gateway modules | $5,000 |
| Installation and commissioning | $8,000–$13,000 |
| **Total** | **$33,000–$50,000** |

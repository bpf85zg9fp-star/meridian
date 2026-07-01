---
document_id: "RFQ-1000-HT-008"
title: "Meridian Estate Home Theatre — ButtKicker & Crowson Tactile System"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-008 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$90,000–$110,000"
primary_supplier: "ButtKicker AU / Crowson import / AV Integrator"
---

# RFQ-1000-HT-008 — ButtKicker & Crowson Tactile System

## Overview

The Meridian Estate theatre employs a two-layer tactile system: ButtKicker BK Advance shakers in the floor/platform structure, and Crowson TES100 actuators integrated into the Cineak Fortuny seating. Together these provide full-body tactile immersion synchronised with the Christie Eclipse / Pro Audio Technology audio system.

---

## 1. ButtKicker BK Advance

| Parameter | Specification |
|---|---|
| Model | ButtKicker BK Advance |
| Quantity | 15 units |
| Function | Low-frequency tactile transducer; mounts to theatre platform/floor structure |
| Amplification | 6× BKA1000-N amplifiers (1,000 W each) |
| Frequency range | 8–20 Hz (infrasonic tactile) |

## 2. Crowson TES100 Actuators

| Parameter | Specification |
|---|---|
| Model | Crowson TES100 |
| Quantity | 15 units (one per Cineak Fortuny seat) |
| Function | Seat-mounted tactile actuator; transmits motion through seating frame to viewer |
| Frequency range | 5–50 Hz; designed specifically for cinema seating integration |
| Amplification | Dedicated Crowson amplifier rack |

## 3. Signal Routing

```
Trinnov Altitude32 (subwoofer / LFE output)
         ├────── LFC-24sm subwoofers (acoustic)
         └────── ButtKicker BK Advance (floor tactile)
                  └──── Crowson TES100 (seat tactile)
```

LFE signal split and fed to both acoustic subwoofers and both tactile layers simultaneously. Levels calibrated independently.

## 4. Platform Construction Note

ButtKicker BK Advance units mount to the theatre platform (raised seating structure). Platform must be engineered to transmit vibration efficiently without damping. Consult structural engineer and ButtKicker installation guidelines during theatre construction phase.

## 5. Integration

- **Trinnov Altitude32:** LFE channel routed to ButtKicker amplifiers
- **KNX/Josh.ai:** Scene control enables/disables tactile system (e.g., disabled for dialogue-heavy content)

## 6. Cost Estimate

| Item | Qty | Est. Each | Total Est. |
|---|---|---|---|
| ButtKicker BK Advance | 15 | $4,000 | $60,000 |
| BKA1000-N amplifiers | 6 | $2,000 | $12,000 |
| Crowson TES100 actuators | 15 | $800 | $12,000 |
| Crowson amplifier system | 1 | $6,000 | $6,000 |
| Installation and calibration | — | — | $8,000–$12,000 |
| **Total** | | | **$98,000–$102,000** |

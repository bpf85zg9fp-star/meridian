---
document_id: "RFQ-1000-HT-007"
title: "Meridian Estate Home Theatre — Cineak Fortuny Seating"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-007 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$80,000–$120,000"
primary_supplier: "Cineak / AV Integrator import"
---

# RFQ-1000-HT-007 — Cineak Fortuny Seating

## Specification

| Parameter | Specification |
|---|---|
| Model | Cineak Fortuny |
| Quantity | 15 seats |
| Recline | Full motorised electric recline |
| Motion | Full motion capability |
| Massage | Integrated massage modules |
| Heat | Heated seat and back |
| Tactile | Compatible with Crowson TES100 actuator integration (see ButtKicker-Crowson.md) |

## Layout

- 15 seats arranged in rows (row configuration to be determined with theatre designer based on room dimensions)
- All seats wired for power (recline motors, heat, massage, and Crowson actuators)
- Aisle clearance to meet AS 1428 accessible design principles where applicable
- Seat upholstery: dark premium leather (colour and finish to be confirmed by Kevin)

## Integration with Tactile System

Cineak Fortuny seats are specified to integrate with the Crowson TES100 actuator system. This requires:
- Crowson actuators physically mounted to seat frames during manufacture or retrofitted
- Crowson amplifier output routed to each actuator
- Calibration of tactile output levels with audio system

See `ButtKicker-Crowson.md` for full tactile system specification.

## KNX/Josh.ai Integration

- Seat recline position can be controlled via KNX scene: “Movie Start” → all seats recline to preferred position
- “End Movie” or “Intermission” → seats return to upright
- Individual seat controls via armrest panel

## Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| 15× Cineak Fortuny seats (full spec) | $80,000–$110,000 |
| Installation, wiring, integration | $8,000–$10,000 |
| **Total** | **$88,000–$120,000** |

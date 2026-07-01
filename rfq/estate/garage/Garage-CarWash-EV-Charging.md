---
document_id: "RFQ-1000-GAR-001"
title: "Meridian Estate Garage — Structure, Car Wash, EV Charging & Tech"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Garage"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-GAR-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-20 — Master RFQ review"
  - "2025-07-19 — Master RFQ Request"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$600,000–$750,000"
---

# RFQ-1000-GAR-001 — Garage, Car Wash, EV Charging & Tech

## 1. Structure

- **Capacity:** 10 vehicles — square grid (5 × 2)
- **Bay dimensions:** 6 m × 3.2 m each (oversized for Bentayga with roof accessories)
- **Ceiling height:** 3.8–4.2 m clear (mezzanine storage above)
- **Construction:** BAL-FZ compliant; fire-rated; insulated; ember-proof seals; PGH Blue Steel Flash + VMZinc Anthra Zinc exterior to match main residence

## 2. Doors — Silvelox Secur Plus

| Door | Location | Function |
|---|---|---|
| Entry | Main façade (left) | Vehicle entry from external driveway |
| Exit | Main façade (right) | Vehicle exit to driveway |
| Wash bay inner | Between containment bay and main garage | Opens automatically when WashTec dry cycle completes |

All three: Silvelox Secur Plus hinged doors, VMZinc Anthra Zinc finish. KNX/Josh.ai automated sequencing. UPS backup for all door systems.

## 3. Automated Car Wash Bay — WashTec SoftCare² Pro

| Parameter | Specification |
|---|---|
| Model | WashTec SoftCare² Pro |
| Type | Gantry-style — vehicle stationary, gantry moves over vehicle |
| Location | Sealed containment room immediately inside entry door |
| Water recycling | Underground filtration + collection tank; 80–90% water reuse |
| Automation | KNX “Vehicle Entry” scene triggers: entry door open → wash → rinse → dry → inner door opens |
| Finish | Dark waterproof acoustic panels; Anthra Zinc accent trims |
| Estimated cost | AUD $185,000–$225,000 + $35,000–$45,000 water recycling |

## 4. Bay Allocation

| Bay | Allocated vehicle |
|---|---|
| 1–2 | Bentley Continental GT |
| 3–4 | Bentley Bentayga |
| 5 | Triumph Rocket 3 + tool/storage zone |
| 6–10 | Flex (guests, additional vehicles) |

## 5. EV Charging — ABB Terra 75 kW DC

| Parameter | Specification |
|---|---|
| Model | ABB Terra 75 kW DC fast charger |
| Quantity | 10 — one per bay |
| Coverage | Uniform — every vehicle can charge in any bay |
| Service | 3-phase high-amp; dedicated transformer |
| Smart charging | KNX load-shedding: shifts to solar surplus; OCPP compliant |
| V2G option | Wallbox Quasar 2 bi-directional V2G on 2 chargers (optional) |
| Estimated cost | AUD $90,000 |

## 6. Garage Tech

- **Access control:** KNX biometric door controllers (Basalte Ellie at each entry point)
- **Surveillance:** 4× 4K thermal/LPR cameras (Mobotix/Nedap) at all entry/exit points
- **Vacuum:** Daycare central vacuum extension — hose ports + detailing connections throughout garage
- **Robot vacuum:** Ecovacs Deebot X9 Pro Omni with auto-empty dock; integrated into central vacuum network
- **Climate:** Dehumidification system for vehicle preservation; temperature-controlled
- **Storage:** Tesla Powerwall bank + DJI Drone Dock + tool storage wall in service spine at rear
- **Drone:** DJI Dock in service spine bay — automated estate perimeter patrol launch/recovery (see RFQ-1000-OUT-001)

## 7. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Garage structure (BAL-FZ, 10-bay, mezzanine) | $220,000–$280,000 |
| 3× Silvelox Secur Plus doors + automation | $45,000–$60,000 |
| WashTec SoftCare² Pro + water recycling | $220,000–$270,000 |
| ABB Terra 75 kW EV chargers (10×) | $90,000 |
| Basalte Ellie + KNX integration | $12,000–$18,000 |
| Surveillance cameras (4× 4K thermal/LPR) | $18,000–$25,000 |
| Central vacuum extension + Ecovacs robot | $8,000–$12,000 |
| Dehumidification + climate control | $15,000–$22,000 |
| DJI Dock installation + integration | $12,000–$18,000 |
| **Total** | **$640,000–$795,000** |

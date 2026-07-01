---
document_id: "RFQ-1000-HT-001"
title: "Meridian Estate Home Theatre — Christie Eclipse Projector"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-001 is provisional — extended sub-document convention pending A1 schema ratification."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-09-10 — Christie G3 demo scenes"
  - "2025-09-12 — Home theater upgrades recommendations"
  - "2025-07-19 — Master RFQ Request (theatre section)"
  - "2025-08-20 — Master RFQ review (RFQ-KV-2025-001, theatre upgrade)"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$840,000–$920,000 (projector, lens, mount, power infrastructure, cooling, commissioning)"
primary_supplier: "Technical Audio Group (Christie AU authorised dealer)"
---

# RFQ-1000-HT-001 — Christie Eclipse Projector

## Decision Context

The Christie Eclipse was selected over the Barco Thor+ (originally specified) following evaluation of HDR performance, contrast ratio, and theatre ambition. Kevin confirmed upgrade to Christie Eclipse for a zero-compromise private cinema. The Christie Eclipse represents the most advanced HDR-capable projector commercially available.

---

## 1. Projector Specification

| Parameter | Specification |
|---|---|
| Model | Christie Eclipse |
| Resolution | 4K (4096 × 2160) native |
| Technology | RGB dual-modulation laser — infinite contrast via dual light path |
| HDR | True HDR; full BT.2020 coverage; dual-modulation enables absolute black |
| Certification | DCI-certified |
| Luminance | Reference-grade — consult Christie/TAG for specific lumen spec |
| Dimensions | ~1100 × 600 × 320 mm |
| Weight | ~220–230 kg |
| Heat output | ~3.5 kW |
| Noise | ~50–55 dB — must be acoustically isolated |

## 2. Lens

- **Model:** Christie ILS4K 1.13–1.66:1 motorised lens kit
- Optimised for 4–9 m throw distance
- Motorised focus/zoom

## 3. Mounting

- Christie adjustable ceiling frame
- Vibration-isolated mount (Future Automation custom projector cradle)
- Service clearance: minimum 1 m rear and both sides
- Due to weight (~230 kg), structural engineering of ceiling mount point is required prior to installation

## 4. Power Infrastructure (Required)

- **Circuit:** Dedicated 3-phase 208–240 V input
- **ATS:** Automatic Transfer Switch for generator/UPS failover
- **UPS:** Furman F1500-UPS or Eaton 9PX 3-phase series
- **Conditioning:** IsoTek or Torus Power surge-protected clean power
- **KNX relay:** Controlled shutdown/power-on sequence via KNX logic

## 5. Cooling & Ventilation (Required)

- Minimum 3,000–4,000 W heat rejection capacity
- Dedicated HVAC extraction for projector bay
- Acoustic return plenum to prevent noise bleed into theatre
- Alternatively: projection room / equipment bay isolated from main theatre (recommended — moves all heat and noise sources out of listening environment)

## 6. AV Rack

- **Rack:** Middle Atlantic NetShelter FX fire-rated rack
- Located in dedicated adjacent equipment bay (not inside theatre)
- Houses Christie electronics, madVR Envy, KNX integration modules, UPS

## 7. Integration

| System | Integration |
|---|---|
| KNX | Relay control for power on/off; warm-up/cool-down state triggers scene logic |
| Josh.ai | Scene: “Start Movie” powers Christie; “End Session” triggers cool-down |
| Basalte Lena | Scene panel in theatre shows projector status |
| madVR Envy Extreme MK2 | Video signal source; full HDR tone mapping compatibility |
| Kaleidescape Strato V | Content source; Christie optimised for Kaleidescape 4K HDR output |
| Stewart Director's Choice | Confirm screen gain 1.1–1.3 for optimal contrast with Eclipse dual-modulation |

## 8. Notes

- Christie Eclipse is primarily a commercial projector. Few residential integrators in Australia have hands-on experience. Commissioning should be by Christie-authorised technician.
- madVR Envy Extreme MK2 compatibility is confirmed but less integrated than with Barco. Allow additional commissioning time.
- Comparison made during planning: Christie Eclipse vs Barco Thor+ — Eclipse wins on true HDR black depth; Thor+ easier to integrate residentially. Decision: Christie Eclipse for world-class black levels.

## 9. Cost Estimate

| Line Item | Estimated Cost (AUD) |
|---|---|
| Christie Eclipse projector | $700,000 |
| Christie ILS4K lens kit | $60,000 |
| Adjustable ceiling mount + vibration isolators | $15,000 |
| 3-phase power circuit + ATS | $20,000 |
| UPS + power conditioning | $17,500 |
| HVAC extraction upgrade | $32,500 |
| Fire-rated AV rack (Middle Atlantic FX) | $12,000 |
| KNX/Josh.ai integration module + programming | $7,500 |
| Installation, commissioning, Christie calibration | $30,000 |
| **Total** | **~$894,500** |

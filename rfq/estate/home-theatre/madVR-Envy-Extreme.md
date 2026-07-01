---
document_id: "RFQ-1000-HT-004"
title: "Meridian Estate Home Theatre — madVR Envy Extreme MK2 Video Processor"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-004 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-09-10 — Christie G3 demo scenes"
  - "2025-09-12 — Home theater upgrades recommendations"
  - "2025-07-19 — Master RFQ Request"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$18,000–$22,000"
primary_supplier: "AV Integrator / import"
---

# RFQ-1000-HT-004 — madVR Envy Extreme MK2

## Overview

The madVR Envy Extreme MK2 performs frame-by-frame dynamic HDR tone mapping between the Kaleidescape Strato V source and the Christie Eclipse projector. It is the critical link that allows the Christie Eclipse's dual-modulation HDR to be correctly driven from consumer-grade HDR content.

---

## 1. Specification

| Parameter | Specification |
|---|---|
| Model | madVR Envy Extreme MK2 |
| Function | 4K HDR video processing; dynamic tone mapping; frame-by-frame analysis |
| HDR formats | HDR10, HDR10+, Dolby Vision, HLG |
| Processing | Frame-by-frame content analysis; pixel-accurate tone mapping curves |
| Outputs | HDMI 2.1; compatible with Christie Eclipse input specifications |
| Noise reduction | AI-based video enhancement |

## 2. Signal Chain Position

```
Kaleidescape Strato V  →  madVR Envy Extreme MK2  →  Christie Eclipse
```

## 3. Christie Eclipse Compatibility Note

The madVR Envy Extreme MK2 is compatible with the Christie Eclipse but with less native integration than it has with Barco projectors. During commissioning:
- Confirm HDMI signal handshake between madVR output and Christie Eclipse input
- Calibrate tone mapping curves to Christie's dual-modulation characteristics
- Allow additional commissioning time (≈ 2–3 additional days vs Barco integration)

## 4. Silent Cooling Enclosure

The madVR Envy Extreme MK2 generates heat. In the equipment bay adjacent to the theatre, install a silent cooling enclosure (e.g. Middle Atlantic QuietCool) to prevent fan noise bleeding into the theatre environment.

## 5. Integration

- **KNX/Josh.ai:** Power on/off via KNX relay; boot time must be factored into theatre scene sequencing
- **Basalte Lena:** Status indicator in theatre control panel

## 6. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| madVR Envy Extreme MK2 | $15,000–$18,000 |
| Silent cooling enclosure (Middle Atlantic QuietCool) | $3,000–$4,000 |
| **Total** | **$18,000–$22,000** |

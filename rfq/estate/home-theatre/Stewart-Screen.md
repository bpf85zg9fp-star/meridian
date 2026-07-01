---
document_id: "RFQ-1000-HT-006"
title: "Meridian Estate Home Theatre — Stewart Director's Choice Screen"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-006 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$25,000–$35,000"
primary_supplier: "AV Integrator (Stewart Filmscreen distributor)"
---

# RFQ-1000-HT-006 — Stewart Director's Choice Screen

## Specification

| Parameter | Specification |
|---|---|
| Model | Stewart Filmscreen Director's Choice |
| Masking | 4-way motorised masking (top, bottom, left, right) |
| Mount | Fixed installation (not retractable) |
| Aspect ratio | Configurable via masking — accommodates 1.78:1, 1.85:1, 2.35:1, 2.40:1 and others |
| Surface | TBC with installer — confirm gain spec for Christie Eclipse |

## Screen Gain Note for Christie Eclipse

The Christie Eclipse uses dual-modulation laser to achieve infinite contrast. Screen gain affects perceived brightness and off-axis performance. For Christie Eclipse:
- Recommended gain: 1.1–1.3
- Matte white or StudioTek 100/130 surface options should be evaluated against throw distance and seating layout
- Confirm final screen surface with Christie-authorised integrator after seating plan is finalised

## 4-Way Masking

The 4-way motorised masking system enables:
- Full widescreen (2.35:1 / 2.40:1) for scope cinema content
- Standard (1.78:1 / 1.85:1) for TV and standard content
- Custom aspect ratios on demand
- KNX-triggered aspect ratio changes as part of content scenes (e.g., Kaleidescape metadata triggers masking preset)

## Integration

- **KNX/Josh.ai:** Masking preset tied to content metadata where possible
- **Kaleidescape API:** Content aspect ratio can trigger masking scene automatically

## Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Stewart Director's Choice screen (size TBC) | $20,000–$28,000 |
| Masking motor + controller | Included |
| Installation and alignment | $5,000–$7,000 |
| **Total** | **$25,000–$35,000** |

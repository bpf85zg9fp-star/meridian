---
document_id: "RFQ-1000-HT-009"
title: "Meridian Estate Home Theatre — Mozaex Poster Digital Marquee"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-009 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$30,000–$38,000 (both units installed)"
primary_supplier: "Mozaex dealer / AV Integrator import"
---

# RFQ-1000-HT-009 — Mozaex Poster Digital Marquee

## Overview

Two Mozaex Poster Digital Marquee units are specified for the Meridian Estate theatre entrance experience. These are portrait-format digital poster displays that replicate the cinematic foyer aesthetic and integrate with the Kaleidescape system to automatically display Now Playing artwork.

---

## 1. Units and Placement

| Unit | Location | Purpose |
|---|---|---|
| Marquee 1 | Outside theatre entrance — corridor/foyer wall | Announces currently playing film; sets mood on approach |
| Marquee 2 | Inside theatre — near snack bar or opposite seating entry | Now Playing display visible from seating; atmosphere |

## 2. Specification

| Parameter | Specification |
|---|---|
| Model | Mozaex Poster Digital Marquee |
| Screen size | 49–55" portrait format |
| Resolution | 4K |
| Enclosure | Dark acoustic millwork surround (custom joinery to match theatre interior) |
| Backlighting | RGBW LED halo behind frame — KNX/Josh.ai dimmable and colour-matched to movie palette |
| Connectivity | LAN / Wi-Fi; Kaleidescape API; KNX IP |

## 3. Kaleidescape API Integration

- Kaleidescape API provides Now Playing metadata (poster art, title, chapter) to both Mozaex units automatically
- When a film starts on the Kaleidescape Strato V, both marquees update simultaneously to the official poster art
- No manual curation required — fully automated
- During intermission or idle, marquees can display estate artwork or screensaver mode (rotates curated film art)

## 4. KNX / Josh.ai Integration

| Scene | Marquee behaviour |
|---|---|
| Movie Mode activated | RGBW halo activates; marquees update to Now Playing; brightness dims to atmospheric |
| End session / Goodnight | Marquees fade to black or estate logo screensaver |
| Guest arrival (theatre) | Marquees display welcome message or ambient art |
| Custom palette mode | RGBW colour syncs to dominant colour of current poster art |

## 5. Millwork Surround

- Custom dark stained timber or Anthra Zinc-finish joinery surround for each unit
- Flush wall-mounted; concealed cabling
- RGBW LED strip recessed into reveal behind marquee frame
- Finished to match theatre acoustic panel and entry door aesthetic

## 6. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| 2× Mozaex Poster Digital Marquee 49" | $18,000 |
| 2× Custom millwork surrounds | $7,000 |
| RGBW LED halo (both units) | $2,500 |
| Kaleidescape API + KNX integration | $3,000 |
| Installation and commissioning | $3,500 |
| **Total** | **$34,000** |

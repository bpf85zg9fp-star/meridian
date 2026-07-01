---
document_id: "RFQ-1000-HT-011"
title: "Meridian Estate Home Theatre — Christie Eclipse G3: Room, Lens & Projection Booth Engineering"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-30"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-011 is provisional. Expands RFQ-1000-HT-001 with detailed room/lens/booth engineering. Not a competing projector — this document assumes Christie Eclipse G3 throughout."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "002"
source_conversations:
  - "2025-11-20 — Christie vs Barco projectors"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
cross_reference: "RFQ-1000-HT-001 (Christie Eclipse core spec), RFQ-1000-HT-012 (Barco Heimdall+, evaluated not selected), RFQ-1000-HT-013 (Barco Thor+, conflicting reference — see manifest F-002)"
---

# RFQ-1000-HT-011 — Christie Eclipse G3: Room, Lens & Projection Booth Engineering

## Context

This conversation opens by confirming Christie Eclipse G3 as the already-selected projector ("you already selected the pinnacle") and proceeds to fully engineer the room, lens, and booth around it. Barco Heimdall+ is discussed only as a comparison point early in the conversation and is not adopted — see RFQ-1000-HT-012. No mention of "Barco Thor+" appears anywhere in this conversation.

---

## 1. Room Envelope (Finalised)

| Dimension | Value |
|---|---|
| Length (internal clear) | 10.5 m |
| Width | 7.0 m |
| Height (floor to underside of slab) | 3.4 m |

Sized specifically for the Kaleidescape → madVR Envy Extreme → Christie Eclipse G3 chain with 3 rows × 5 seats, Pro Audio Technology speaker array, and Atmos height channel clearance.

## 2. Screen & Seating Geometry

| Parameter | Value |
|---|---|
| Screen target | 200" diagonal, 2.39:1 (cinemascope) |
| Screen width | 4.686 m |
| Screen height | 1.961 m |
| Screen centre height (bottom at 0.6 m) | 1.580 m |
| Front row FOV target | ~36° (THX optimal) |
| Rear row FOV target | ≥30° (SMPTE minimum) |
| Row 1 eye distance from screen | 7.21 m |
| Row 2 eye distance from screen | 8.26 m |
| Row 3 eye distance from screen | 9.31 m |
| Row pitch | 1.05 m |
| Row 2 riser | +350–400 mm above Row 1 |
| Row 3 riser | +350–400 mm above Row 2 |
| Rear clearance (last row to rear wall) | 1.0–1.2 m |

## 3. Lens & Projector Placement

| Parameter | Recommendation |
|---|---|
| Lens | Christie ILS4 1.13–1.66:1 (High Brightness zoom) |
| Operating point | Mid-zoom ~1.5:1 |
| Resulting throw distance | ~7.03 m (projector ~3.47 m from rear wall in a 10.5 m room) |
| Mount | Ceiling-mounted, centred, lens axis at 1.580 m above floor (matches screen centre — avoids relying on extreme vertical lens shift) |
| Mount drop from 3.4 m ceiling | 1.820 m |
| Service clearance | 300–500 mm above hush box; 200–300 mm side clearance; maintenance hatch required |
| Long-throw alternative (if rear-wall mount required) | ILS4 1.95–3.26:1, throw ≥9.14 m |

## 4. Noise Management — Ceiling Mount Option

Christie Eclipse G3 rated noise: 45 dBA @ 1 m (typical), with most thermal/acoustic load offloaded to an external chiller.

### Modelled SPL by row (before/after hush-box attenuation)

| Scenario | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| No hush box | 49.9 dBA | 51.4 dBA | 41.3 dBA |
| Hush box −6 dB | 43.9 dBA | 45.4 dBA | 35.3 dBA |
| Hush box −10 dB | 39.9 dBA | 41.4 dBA | 31.3 dBA |
| Hush box −12 dB (practical target) | 37.9 dBA | 39.4 dBA | 29.3 dBA |
| Hush box −15 dB (ideal) | 34.9 dBA | 36.4 dBA | 26.3 dBA |

**Design target:** hush-box insertion loss ≥12 dB (goal 15 dB) across 500 Hz–4 kHz, measured post-installation. Chiller to be remoted to plant room regardless of hush-box outcome. Decoupled/isolated mount mandatory.

## 5. Projection Booth — Recommended Alternative to Ceiling Mount

A properly specified projection booth eliminates projector noise from the auditorium entirely and is the approach used in reference commercial cinemas (Dolby Cinema, IMAX GT). Picture quality is preserved **only** if the port window meets the following specification — incorrect glass will visibly degrade the image.

### Port Window Specification

| Parameter | Spec |
|---|---|
| Glass | Low-iron optically white glass (Schott B270, Pilkington Optiwhite, or Saint-Gobain Diamant equivalent) |
| Thickness | 6 mm |
| Coating | Dual-sided broadband anti-reflection (AR) coating, optical-grade (not architectural AR) |
| Transmission | ≥98% |
| Tilt | 5–7° (prevents internal reflection/ghosting back into lens) |
| Window size | Lens diameter × 3 (width and height) — avoids vignetting at zoom extremes |
| Frame | Black velvet-lined interior, matte black exterior |

**Do not use:** regular float glass (green tint), non-AR-coated glass, thick laminated safety glass, acrylic/polycarbonate. Any of these will measurably degrade contrast, sharpness, or introduce ghosting.

### Booth Structural Notes

| Item | Spec |
|---|---|
| Booth footprint | ~1.2–1.5 m depth × 1 m width × 1 m height above lens axis |
| Weight allowance | 100–200 kg (projector + optional in-booth chiller) |
| Thermal load | ~3–5 kW (laser head + electronics); maintain <35°C in booth |
| Video signal | Fibre recommended for 4K/HDR/laser HDR to booth; HDMI 2.1/SDI with active extenders as fallback |
| Fire/code | Booth walls to meet local fire rating; ducting per NCC compliance |

### Booth vs Ceiling Mount — Summary

| Factor | Ceiling Mount | Projection Booth |
|---|---|---|
| Noise in auditorium | Managed via hush box (12–15 dB target) | Eliminated entirely |
| Optical quality | N/A (no glass in path) | Neutral if AR glass spec followed — no loss |
| Throw distance | ~7.03 m (mid-zoom) | May increase; booth typically sits further back |
| Maintenance access | Ceiling hatch | Booth door — slightly less convenient but safer |

**Recommendation from source conversation:** projection booth is the superior approach given the estate's zero-compromise standard — removes noise risk entirely rather than managing it.

## 6. Outstanding RFQ Confirmations

- Final decision: ceiling mount with hush box vs projection booth — not locked in source
- Exact lens code (Christie projection calculator output) pending final screen offset confirmation
- Booth vs hush-box decision affects fibre/cable routing plan — downstream of this decision

## 7. Pipeline Status

| Stage | Status |
|---|---|
| L2A (Claude) | ✅ Extracted 2026-06-30 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-30 | Source: Batch 002, "Christie vs Barco projectors" (2025-11-20)*

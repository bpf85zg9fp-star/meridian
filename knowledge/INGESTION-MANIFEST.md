---
document_id: "KNOWLEDGE-MANIFEST-001"
title: "Meridian Knowledge Base — Ingestion Manifest"
version: "1.2"
status: "Active"
classification: "Infrastructure / Knowledge Management"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# Meridian Ingestion Manifest

Master tracking document for all 40 ChatGPT conversation export batches.

**Ingestion standard:** `standards/INGEST-STD-001.md`  
**Last updated:** 2026-06-29 by Claude (L2A)

---

## Batch Status Summary

| Batch | Conversations | Programme-relevant | Received | Extraction status |
|---|---|---|---|---|
| 000 | 100 | 66 | ✅ 2026-06-27 | ✅ Complete (25 docs) |
| 001 | 100 | 93 | ✅ 2026-06-29 | ✅ Complete (12 docs) |
| 002 | 100 | ~86 | ✅ 2026-06-29 | ⚠️ Priority items complete (13 docs); audit-series and governance-detail items pending — see below |
| 003–039 | — | — | ❌ Not received | — |

---

## ⚠️ Open Critical Findings — Require Kevin's Decision

| ID | Finding | Source | Status |
|---|---|---|---|
| F-001 | Competing RFQ numbering scheme (ChatGPT's internal 1–14 structure) discovered in Batch 002 "RFQs Overview and Breakdown" (2026-01-10). RFQ-1000+ retained as sole authoritative scheme; ChatGPT's numbering logged as source content only. | Batch 002 | Awaiting Kevin confirmation |
| F-002 | Home theatre projector conflict: Christie Eclipse G3 (compared, not conclusively selected, Nov 20) vs "Barco Thor+" (referenced as already-locked in Dec 2 / Jan 5 audit conversations). Conflicts with `rfq/estate/home-theatre/Christie-Eclipse.md` already in repository. | Batch 002 | Awaiting Kevin decision |
| F-003 | Theatre speaker specification conflict: Pro Audio Technology 32-speaker array (RFQ-1000-HT-005, established) vs Ascendo HALO + Wisdom Audio hybrid (explored in "Perlisten vs Focal Audio", Jan 3). | Batch 002 | Awaiting Kevin decision |
| F-004 | Tow vehicle changed: Bentley Bentayga (RFQ-1013, Batch 001) → Toyota LandCruiser 300 GR Sport (RFQ-1002-002, Batch 002). Trailer model also inconsistent: "Bruder EXP-8" (Batch 001) vs "Bruder EXP-12" (Batch 002). | Batch 001 → 002 | Awaiting Kevin confirmation |
| F-005 | Battery bank spec increased: 3× Tesla Powerwall 3 (RFQ-1000 §15) vs 9–12× Powerwall 3 (Batch 002 OPEX conversation, "scale-corrected"). | Batch 000 → 002 | Awaiting Kevin confirmation |

---

## RFQ-1000+ Register

| ID | Working title | Batch(es) | Status |
|---|---|---|---|
| RFQ-1000 | Meridian Estate — Master Smart Home Specification | 000, 001, 002 | ✅ Extracted (master + 15 sub-domain docs) |
| RFQ-1001 | Meridian Resort — Obsidian Hotel Concept | 000, 001 | ✅ Extracted |
| RFQ-1002 | Meridian Vehicles — Fleet Specification | 000, 001, 002 | ✅ Extracted (Bentley fleet + LandCruiser 300 GR Sport) |
| RFQ-1003 | Meridian Lifestyle — Fashion, Recreation, Memberships | 000 | ✅ Extracted |
| RFQ-1004 | Meridian Financial — Investment Strategy | 000 | ✅ Extracted |
| RFQ-1005 | Meridian Personal / Health / Family | 000 | ✅ Extracted |
| RFQ-1006 | Meridian Estate — Land Search and Site Selection | 000 | ✅ Extracted |
| RFQ-1007 | Meridian Marina — 55m Ultra-Luxury Expedition Yacht | 001, 002 | ✅ Extracted; autonomy/expedition detail from Batch 002 ("Yacht ownership opportunities") not yet merged — pending |
| RFQ-1008 | Meridian Aviation — Gulfstream G700 VVIP Completion | 001 | ✅ Extracted |
| RFQ-1009 | Meridian Vehicles — Custom Build | 001 | ✅ Extracted |
| RFQ-1010 | Meridian Resort — Hotel App Technology Stack & Security | 001, 002 | ✅ Extracted; Batch 002 "Hotel software recommendations" (autonomous-operations concept) not yet merged — pending |
| RFQ-1011 | Meridian Financial — Day One Cost & 5-Year Lifecycle Model | 001, 002 | ✅ Extracted; RFQ-1011-002 (Weekly OPEX) partial — water/internet/food sub-totals incomplete in source |
| RFQ-1012 | Meridian Resort — Hotel Staffing | 001 | ⏳ Reserved — not yet extracted |
| RFQ-1013 | Meridian Lifestyle — 435-Day Family Touring | 001, 002 | ⚠️ Needs update — tow vehicle changed (see F-004) |
| RFQ-1014 | Meridian Estate — Build Team, PM & Timeline | 002 | ✅ Extracted |
| RFQ-1015 | Meridian Estate — Operating Framework (Governance) | 002 | ✅ Extracted (summary level) |
| RFQ-1016–1017 | Unassigned | — | Available |
| RFQ-1018 | Meridian Estate — Quality Audit Series (materials/furniture/appliances/wardrobe/linen) | 002 | ⏳ Reserved — not yet extracted (5 source conversations, largely upgrade-suggestions on already-specified items) |
| RFQ-1019 | Meridian Estate — Colour & Brick Palette | 002 | ⏳ Reserved — not yet extracted |
| RFQ-1020 | Meridian Estate — De-Branding Framework | 002 | ⏳ Reserved — not yet extracted |
| RFQ-1021+ | TBD | — | Not assigned |

---

## Batch 002 — Detail

**Status file:** `knowledge/raw-exports/chatgpt/export-2026-06-27/BATCH-002-STATUS.md`  
**Date range:** 2025-11-16 to 2026-01-11  
**Documents committed:** 13 (BATCH-002-STATUS + 4 RFQ documents in first pass + RFQ-1015 + this manifest)  
**Explicitly pending within Batch 002** (lower priority — mostly refinements to already-specified items rather than new information):
- RFQ-1018: Materials audit, furniture audit, appliance audit, wardrobe audit (×2), linen audit — 5 source conversations
- RFQ-1019: Estate colour/brick palette (Kolumba brick selection detail)
- RFQ-1020: De-branding framework (full vessel/supplier detail)
- RFQ-1000-HT: Infrasonic bass tuning curve detail ("Infrasonic Bass Capability", Dec 28)
- RFQ-1007: Yacht autonomy/expedition systems detail ("Yacht ownership opportunities", Nov 17)
- RFQ-1010: Autonomous hotel operations concept ("Hotel software recommendations", Nov 29)
- RFQ-1014: UpKeep/ArcGIS/Trainual/Deputy licensing cost detail

**Kevin has indicated these pending items are acceptable to leave until the cleanup phase** given the "extract everything, organise later" instruction — logged here so nothing is lost track of.

---

## Known Cross-Agent Duplication (Not Yet Resolved)

Per Kevin's instruction (2026-06-29), duplicates between Claude and Grok's parallel ingestion are acceptable during the extraction phase:

- `Mozaex-Digital-Marquees.md` (Claude) vs `Mozaex-Digital-Marquee.md` (Grok)
- `Focal-Naim-CI-Audio.md` (Claude) vs `Focal-Naim-CI.md` (Grok)
- Smart-home backbone: Claude's combined `KNX-Josh-Basalte.md` vs Grok's split files
- Structure: Claude's `Cladding-Glazing-Bushfire-Energy.md` vs Grok's `Cladding-Materials.md`

Addressed in the cleanup/consolidation phase.

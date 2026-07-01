---
document_id: "KNOWLEDGE-MANIFEST-001"
title: "Meridian Knowledge Base — Ingestion Manifest"
version: "1.3"
status: "Active"
classification: "Infrastructure / Knowledge Management"
date: "2026-06-30"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# Meridian Ingestion Manifest

Master tracking document for all 40 ChatGPT conversation export batches.

**Ingestion standard:** `standards/INGEST-STD-001.md`  
**Last updated:** 2026-06-30 by Claude (L2A)

---

## Batch Status Summary

| Batch | Conversations | Programme-relevant | Received | Extraction status |
|---|---|---|---|---|
| 000 | 100 | 66 | ✅ 2026-06-27 | ✅ Complete (25 docs) |
| 001 | 100 | 93 | ✅ 2026-06-29 | ✅ Complete (12 docs) |
| 002 | 100 | ~86 | ✅ 2026-06-29 | ⚠️ Priority items complete (16 docs); audit-series/governance-detail items pending |
| 003–039 | — | — | ❌ Not received | — |

---

## Open Critical Findings

| ID | Finding | Status |
|---|---|---|
| F-001 | Competing RFQ numbering scheme (ChatGPT's internal 1–14 structure, Batch 002 "RFQs Overview and Breakdown") | ✅ **RESOLVED 2026-06-30** — Kevin confirmed: this was ChatGPT's own internal numbering only. RFQ-1000+ is the sole authoritative scheme repository-wide. |
| F-002 | Home theatre projector conflict: Christie Eclipse G3 vs "Barco Thor+" | ⚠️ **INVESTIGATED, NOT YET RESOLVED** — See detail below. All three projector threads (Christie Eclipse, Barco Heimdall+, Barco Thor+) now ingested per Kevin's instruction (2026-06-30). Genuine unresolved conflict remains — Kevin decision required. |
| F-003 | Theatre speaker conflict: Pro Audio Technology array vs Ascendo HALO + Wisdom Audio hybrid | Awaiting Kevin decision |
| F-004 | Tow vehicle changed: Bentayga → LandCruiser 300 GR Sport; trailer EXP-8 vs EXP-12 naming inconsistency | Awaiting Kevin confirmation |
| F-005 | Battery bank spec: 3× vs 9–12× Tesla Powerwall 3 | Awaiting Kevin confirmation |

### F-002 Detail — Projector Conflict (Updated 2026-06-30)

All three projector threads now documented:

| Document | Projector | Status |
|---|---|---|
| `rfq/estate/home-theatre/Christie-Eclipse.md` (RFQ-1000-HT-001) | Christie Eclipse G3 | Core spec — originally selected, from Batch 000 |
| `rfq/estate/home-theatre/Christie-Eclipse-Room-Lens-Booth.md` (RFQ-1000-HT-011) | Christie Eclipse G3 | Detailed room/lens/projection-booth engineering — new from Batch 002, Nov 20 conversation |
| `rfq/estate/home-theatre/Barco-Heimdall-Plus.md` (RFQ-1000-HT-012) | Barco Heimdall+ | Evaluated against Eclipse in the same Nov 20 conversation, explicitly **not selected** — reference record only |
| `rfq/estate/home-theatre/Barco-Thor-Plus.md` (RFQ-1000-HT-013) | Barco Thor+ | **Unresolved.** Referenced as an already-locked decision in three Dec/Jan audit conversations, but never actually compared or chosen in any conversation ingested so far. Confirmed via external verification to be a real Barco flagship product (32,000 lumens, 6P RGB laser) — not a naming error, not the same product as Heimdall+. One source indicates the Thor/Thor+ line may have been discontinued September 2025 (unconfirmed — Barco's own site still shows it as active). |

**Key finding:** the only conversation containing an actual technical projector comparison (Nov 20) evaluates Eclipse vs Heimdall+ and results in Eclipse being confirmed. Thor+ never appears there. Its later appearances (Dec 2, Dec 6, Jan 5) all pair it with the exact same downstream chain (Trinnov/madVR/Kaleidescape/Stewart) already established for Eclipse, with no visible decision point. Two working hypotheses are recorded in RFQ-1000-HT-013 §3 — either a genuine decision exists in a not-yet-ingested batch, or this is an L1 (ChatGPT) drafting substitution that was never actually decided. **Kevin's confirmation is required before the home theatre RFQ series can be finalised.** If Thor+ is confirmed as correct, RFQ-1000-HT-011's room/lens/booth engineering (built around Eclipse's specific optical/thermal characteristics) will need rework.

---

## RFQ-1000+ Register

| ID | Working title | Batch(es) | Status |
|---|---|---|---|
| RFQ-1000 | Meridian Estate — Master Smart Home Specification | 000, 001, 002 | ✅ Extracted (master + 18 sub-domain docs) |
| RFQ-1001 | Meridian Resort — Obsidian Hotel Concept | 000, 001 | ✅ Extracted |
| RFQ-1002 | Meridian Vehicles — Fleet Specification | 000, 001, 002 | ✅ Extracted |
| RFQ-1003 | Meridian Lifestyle | 000 | ✅ Extracted |
| RFQ-1004 | Meridian Financial — Investment Strategy | 000 | ✅ Extracted |
| RFQ-1005 | Meridian Personal / Health / Family | 000 | ✅ Extracted |
| RFQ-1006 | Meridian Estate — Land Search | 000 | ✅ Extracted |
| RFQ-1007 | Meridian Marina — Yacht | 001, 002 | ✅ Extracted; autonomy detail pending |
| RFQ-1008 | Meridian Aviation — Gulfstream G700 | 001 | ✅ Extracted |
| RFQ-1009 | Meridian Vehicles — Custom Build | 001 | ✅ Extracted |
| RFQ-1010 | Meridian Resort — Hotel App Tech Stack | 001, 002 | ✅ Extracted; autonomous-ops concept pending |
| RFQ-1011 | Meridian Financial — Day One Cost & Lifecycle | 001, 002 | ✅ Extracted; OPEX sub-totals partial |
| RFQ-1012 | Meridian Resort — Hotel Staffing | 001 | ⏳ Reserved |
| RFQ-1013 | Meridian Lifestyle — 435-Day Touring | 001, 002 | ⚠️ Needs update (F-004) |
| RFQ-1014 | Meridian Estate — Build Team, PM & Timeline | 002 | ✅ Extracted |
| RFQ-1015 | Meridian Estate — Operating Framework | 002 | ✅ Extracted (summary) |
| RFQ-1016–1017 | Unassigned | — | Available |
| RFQ-1018 | Meridian Estate — Quality Audit Series | 002 | ⏳ Reserved |
| RFQ-1019 | Meridian Estate — Colour & Brick Palette | 002 | ⏳ Reserved |
| RFQ-1020 | Meridian Estate — De-Branding Framework | 002 | ⏳ Reserved |
| RFQ-1021+ | TBD | — | Not assigned |

---

## Known Cross-Agent Duplication (Not Yet Resolved)

Per Kevin's instruction (2026-06-29), duplicates between Claude and Grok's parallel ingestion are acceptable during the extraction phase — addressed in the cleanup/consolidation phase.

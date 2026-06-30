---
document_id: "KNOWLEDGE-MANIFEST-001"
title: "Meridian Knowledge Base — Ingestion Manifest"
version: "1.1"
status: "Active"
classification: "Infrastructure / Knowledge Management"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# Meridian Ingestion Manifest

Master tracking document for all 40 ChatGPT conversation export batches. Update this file whenever a batch is received or an extraction is completed.

**Ingestion standard:** `standards/INGEST-STD-001.md`  
**Last updated:** 2026-06-29 by Claude (L2A)

---

## Batch Status Summary

| Batch | File | Conversations | Programme-relevant | Received | Extraction status |
|---|---|---|---|---|---|
| 000 | `conversations-000.json` | 100 | 66 | ✅ 2026-06-27 | ✅ Complete (25 docs) |
| 001 | `conversations-001.json` | 100 | 93 | ✅ 2026-06-29 | ✅ Complete (12 docs) |
| 002 | — | — | — | ❌ Not received | — |
| 003 | — | — | — | ❌ Not received | — |
| 004 | — | — | — | ❌ Not received | — |
| 005 | — | — | — | ❌ Not received | — |
| 006 | — | — | — | ❌ Not received | — |
| 007 | — | — | — | ❌ Not received | — |
| 008 | — | — | — | ❌ Not received | — |
| 009 | — | — | — | ❌ Not received | — |
| 010 | — | — | — | ❌ Not received | — |
| 011 | — | — | — | ❌ Not received | — |
| 012 | — | — | — | ❌ Not received | — |
| 013 | — | — | — | ❌ Not received | — |
| 014 | — | — | — | ❌ Not received | — |
| 015 | — | — | — | ❌ Not received | — |
| 016 | — | — | — | ❌ Not received | — |
| 017 | — | — | — | ❌ Not received | — |
| 018 | — | — | — | ❌ Not received | — |
| 019 | — | — | — | ❌ Not received | — |
| 020 | — | — | — | ❌ Not received | — |
| 021 | — | — | — | ❌ Not received | — |
| 022 | — | — | — | ❌ Not received | — |
| 023 | — | — | — | ❌ Not received | — |
| 024 | — | — | — | ❌ Not received | — |
| 025 | — | — | — | ❌ Not received | — |
| 026 | — | — | — | ❌ Not received | — |
| 027 | — | — | — | ❌ Not received | — |
| 028 | — | — | — | ❌ Not received | — |
| 029 | — | — | — | ❌ Not received | — |
| 030 | — | — | — | ❌ Not received | — |
| 031 | — | — | — | ❌ Not received | — |
| 032 | — | — | — | ❌ Not received | — |
| 033 | — | — | — | ❌ Not received | — |
| 034 | — | — | — | ❌ Not received | — |
| 035 | — | — | — | ❌ Not received | — |
| 036 | — | — | — | ❌ Not received | — |
| 037 | — | — | — | ❌ Not received | — |
| 038 | — | — | — | ❌ Not received | — |
| 039 | — | — | — | ❌ Not received | — |

**Note on completion status:** "Complete" means all priority/critical/high-priority source conversations have been extracted into rfq/ documents. Per Kevin's 2026-06-29 instruction, duplication with Grok's parallel ingestion is acceptable at this stage — consolidation happens in a later cleanup phase. A small number of lower-priority items within each batch (e.g. minor product recommendation threads) may not have individual extracted documents; these are captured in the BATCH-STATUS conversation inventory for that batch and can be revisited during cleanup if needed.

---

## RFQ-1000+ Register

All ecosystem artefacts extracted from the knowledge base are assigned IDs in the RFQ-1000+ range. IDs are reserved here before extraction begins.

| ID | Working title | Source batch(es) | Status |
|---|---|---|---|
| RFQ-1000 | Meridian Estate — Master Smart Home Specification | 000, 001 | ✅ Extracted (master + 13 sub-domain docs) |
| RFQ-1001 | Meridian Resort — Obsidian Hotel Concept | 000, 001 | ✅ Extracted (concept + tech stack + security) |
| RFQ-1002 | Meridian Vehicles — Fleet Specification | 000, 001 | ✅ Extracted (Bentley fleet) |
| RFQ-1003 | Meridian Lifestyle — Fashion, Recreation, Memberships | 000 | ✅ Extracted |
| RFQ-1004 | Meridian Financial — Investment Strategy | 000 | ✅ Extracted |
| RFQ-1005 | Meridian Personal / Health / Family | 000 | ✅ Extracted |
| RFQ-1006 | Meridian Estate — Land Search and Site Selection | 000 | ✅ Extracted |
| RFQ-1007 | Meridian Marina — 55m Ultra-Luxury Expedition Yacht | 001 | ✅ Extracted — **new domain** |
| RFQ-1008 | Meridian Aviation — Gulfstream G700 VVIP Completion | 001 | ✅ Extracted — **new domain** |
| RFQ-1009 | Meridian Vehicles — Custom Build (Project AURELION + Triumph Rocket 3 Stage-2) | 001 | ✅ Extracted |
| RFQ-1010 | Meridian Resort — Hotel App Technology Stack & Security | 001 | ✅ Extracted |
| RFQ-1011 | Meridian Financial — Day One Cost & 5-Year Lifecycle Model | 001 | ✅ Extracted — flagged for reconciliation with RFQ-1000 cost rollup |
| RFQ-1012 | Meridian Resort — Hotel Staffing (External vs Salary) | 001 | ⏳ Reserved — not yet extracted |
| RFQ-1013 | Meridian Lifestyle — 435-Day Family Touring (Bentayga + EXP-8) | 001 | ⚠️ Partial — final cost total and EXP-8 detail incomplete in source |
| RFQ-1014+ | TBD — assigned as extraction proceeds | TBD | Not assigned |

---

## Batch 000 — Detail

**Status file:** `knowledge/raw-exports/chatgpt/export-2026-06-27/BATCH-000-STATUS.md`  
**Date range of conversations:** 2025-07-10 to 2025-09-12  
**Primary source document:** `RFQ-KV-2025-001` (Master RFQ, 2025-08-20/21) → extraction target: RFQ-1000

## Batch 001 — Detail

**Status file:** `knowledge/raw-exports/chatgpt/export-2026-06-27/BATCH-001-STATUS.md`  
**Date range of conversations:** 2025-09-12 to 2025-11-14  
**New domains introduced:** Marina (yacht), Aviation (aircraft)  
**Largest single thread:** Hotel App Technology Stack (RFQ-1010) — spans 8+ source conversations on PMS, payments, POS, security, and staffing  
**Open items requiring follow-up:** RFQ-1011 hotel cost reconciliation; RFQ-1013 EXP-8 detail and final trip total; RFQ-1012 staffing model not yet extracted

---

## Known Cross-Agent Duplication (Not Yet Resolved)

Per Kevin's instruction (2026-06-29), duplicates between Claude and Grok's parallel ingestion are acceptable during the extraction phase. Known overlaps as of Batch 001:

- `Mozaex-Digital-Marquees.md` (Claude) vs `Mozaex-Digital-Marquee.md` (Grok)
- `Focal-Naim-CI-Audio.md` (Claude) vs `Focal-Naim-CI.md` (Grok)
- Smart-home backbone: Claude's combined `KNX-Josh-Basalte.md` vs Grok's split `KNX-Backbone.md` / `Josh-ai.md` / `Basalte-Lena.md` / `Lutron.md` / `mmWave-Sensors.md`
- Structure: Claude's `Cladding-Glazing-Bushfire-Energy.md` vs Grok's `Cladding-Materials.md`

These will be addressed in the cleanup/consolidation phase per Kevin's direction.

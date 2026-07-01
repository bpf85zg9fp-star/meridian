---
document_id: "RFQ-1000-HVAC-001"
title: "Meridian Estate — Air & Water Filtration Systems"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / HVAC"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HVAC-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "001"
source_conversations:
  - "2025-09-13 — Air and water filtration"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "~$11,000 air + water filtration equipment (excl. install/plumbing)"
---

# RFQ-1000-HVAC-001 — Air & Water Filtration Systems

This document supersedes the brief filtration references in RFQ-1000-STR-001 §7 with full system detail from Batch 001.

## 1. Air Filtration — 4-Stage Whole-Estate System

| Stage | System | Model | Function | Unit Price (AUD) | Qty | Total (AUD) |
|---|---|---|---|---|---|---|
| 1 | Core ventilation/pre-filter | Zehnder ComfoAir Q600 | Heat/energy recovery ventilation with high-efficiency pre-filters | $5,108.25 | 1 | $5,108.25 |
| 2 | Fine particulate | Camfil Absolute™ V HEPA H14 | EN1822 H14 certified, ≥99.995% efficiency (cleanroom/hospital grade) | $300.00 | 4 | $1,200.00 |
| 3 | Gas & odour/VOC | Purafil PuraGrid® V | Activated carbon modules — VOCs, formaldehyde, urban pollution | $500.00 | 4 | $2,000.00 |
| 4 | Sterilisation | UV Resources RLM Xtreme UV-C | 254nm UV-C, HVAC coil/airstream disinfection | $1,200.00 | 1 | $1,200.00 |
| Control | Monitoring | Zehnder ComfoControl + Airthings View Plus IAQ monitors | Estate-wide real-time monitoring, KNX/Basalte integration | $1,000.00 | 1 | $1,000.00 |
| **Air filtration total** | | | | | | **$10,508.25** |

## 2. Water Filtration — Whole-Estate System

| Stage | System | Model | Function | Unit Price (AUD) | Qty | Total (AUD) |
|---|---|---|---|---|---|---|
| 1 | Sediment | Pentair Big Blue 20" 1 Micron | Heavy-duty sediment pre-filter | $288.99 | 2 | $577.98 |
| 2 | Activated carbon | Pentair CBC-10 Carbon Block | 0.5 micron — chlorine/VOC/taste/odour | $31.35 | 2 | $62.70 |
| 3 | Advanced filtration | AquaMetix AMB/10 | Chloramines, fluoride, heavy metals, VOCs | ~$129 | — | — |
| POE disinfection | UV | VIQUA / Trojan UVMax (VH-410 class) | Whole-house UV disinfection for tank/rainwater supply | — | 1 | — |

## 3. System Architecture Notes

- Core ventilation integrates with Zehnder ComfoAir Q600 already specified in RFQ-1000 §4 (HVAC section) — this document adds the staged filtration cartridges to that base unit rather than replacing it
- KNX/Basalte integration for Airthings IAQ monitors confirmed consistent with estate automation backbone (RFQ-1000-SH-001)
- Point-of-use (POU) reverse osmosis + remineraliser recommended additionally for kitchen and espresso machine taps (not itemised in the equipment total above)

## 4. Local Installation & Maintenance Providers (Adelaide)

| Provider | Specialty |
|---|---|
| Adelaide Air Systems | Air treatment systems, compressors, filtration installation |
| SA Compressed Air | Air compressor/filtration servicing |
| Adelaide Dust & Fume Control | HEPA filtration, fume extraction |
| Hydro X Plumbing | Water filter installation/servicing across Adelaide |

**Note:** source conversation flagged that these providers' specific experience with the exact recommended models (Zehnder, Camfil, Purafil, VIQUA, Pentair, AquaMetix) was not confirmed — direct consultation and reference checks recommended before engagement.

## 5. Pipeline Status

| Stage | Status |
|---|---|
| L1 (ChatGPT) | ⚠️ Not yet formatted as standalone artefact |
| L2A (Claude) | ✅ Extracted 2026-06-29 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 001, "Air and water filtration" (2025-09-13)*

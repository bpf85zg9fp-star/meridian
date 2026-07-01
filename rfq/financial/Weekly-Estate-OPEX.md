---
document_id: "RFQ-1011-002"
title: "Meridian Financial — Weekly Estate Operating Expenditure (OPEX)"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Financial"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1011-002 is provisional. Addendum to RFQ-1011-001 (Day One Cost & 5-Year Lifecycle)."
parent_rfq: "RFQ-1011"
reviewed_by: "Claude (L2A)"
source_batch: "002"
source_conversations:
  - "2025-11-26 — Weekly estate expenses"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
disclaimer: "AI-generated planning estimates only, not professional financial advice. Requires qualified adviser review."
---

# RFQ-1011-002 — Weekly Estate Operating Expenditure (OPEX)

## Context

This conversation produced a full weekly/annual OPEX enumeration, explicitly formatted by the source as an "RFQ-ready section." It should be read alongside RFQ-1011-001 §4 (5-Year Operational & Replacement Costs), which this document supersedes in granularity for the utilities/consumables categories.

## 1. Baseline SA Household Reference Points (used as starting comparison)

| Item | Typical SA household |
|---|---|
| Electricity | ~AU $352/quarter (~$117/month) |
| Water | ~AU $200/quarter (~$67/month) |
| Council rates | ~AU $2,000–$2,200/year (~$38–$42/week) |
| Garden maintenance | ~AU $300–$600+/month |

Estate costs are expected to significantly exceed these baselines given scale (pool + pavilion + sauna, large lawns, underground irrigation, 10-vehicle garage, 24/7 HVAC, full smart-home automation, central vacuum, pet systems, outdoor kitchen).

## 2. Solar + Battery Mitigation

Given the scale-corrected battery requirement (**9–12 Tesla Powerwall 3 units** + **30–40 kW solar** — revised up from the 3-Powerwall figure in RFQ-1000 §15), solar/battery will offset:

- **Daytime loads:** irrigation, garden lighting, EV charging (midday), pool pumps/sanitation, partial HVAC, NAS/PoE/cameras/LPR, LaundryJet, central vacuum, robot mower/vacuum charging, pet wash station, outdoor kitchen refrigeration
- **Evening/night loads (battery-covered when sufficiently charged):** core overnight HVAC, PoE infrastructure, security, smart lighting, bedroom usage, theatre basics (excl. projection), kitchen refrigeration, scheduled pumps/filtration

**Note:** this revises the RFQ-1000 §15 battery bank spec (3× Powerwall 3) upward to 9–12 units — flagged for reconciliation.

## 3. Weekly OPEX — RFQ-Ready Section (as drafted in source)

### 3.1 Electricity (post-solar + multiple Powerwall 3 units)
Covers: estate-scale HVAC, pool/pavilion/sauna, server rack, outdoor kitchen refrigeration, Sub-Zero loads, robotic systems, theatre ventilation + Eclipse/Thor+ projector usage.  
**Cost: AU $120–$250/week**

### 3.2 Water & Sewerage
Covers: lawn irrigation (buried dripper), garden/planting irrigation, rainwater system top-up.  
*(Full figure not completed in source conversation before it ended — flagged for follow-up.)*

### 3.3 Internet
Multi-gigabit plan pricing requested at true 10Gb+ tier — source conversation was mid-response (pulling current AU 10Gb+ plan pricing) when it ended. **Not captured — flagged for follow-up.**

### 3.4 Food & Beverage
Full weekly food/drink cost modelling for estate-standard consumption was requested but the conversation ended before the itemised figure was presented. **Not captured — flagged for follow-up.**

## 4. Outstanding Items

This conversation was rich but ended mid-calculation on several sub-totals. The following require a follow-up pass against the raw source conversation to extract exact figures:
- Full water & sewerage weekly cost
- 10Gb+ internet plan pricing (AU market)
- Weekly food & beverage cost at estate standard
- A consolidated weekly/annual grand total

## 5. Cross-Reference

This should be reconciled with RFQ-1011-001 (Day One Cost & 5-Year Lifecycle), which already contains a $594,000–$1,052,000/year Year-1 operational estimate at a coarser granularity. The two documents currently do not share a common methodology and should be merged during the cleanup phase.

## 6. Pipeline Status

| Stage | Status |
|---|---|
| L2A (Claude) | ⚠️ Partial extraction — several sub-totals incomplete in source |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 002, "Weekly estate expenses" (2025-11-26)*

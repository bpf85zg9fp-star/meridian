---
document_id: "RFQ-1000-SH-002"
title: "Meridian Estate Smart Home — Access Control & Smart Locks"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-002 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-21 — Best smart locks luxury"
  - "2025-08-20 — Smart home tech recommendations"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$80,000–$110,000"
---

# RFQ-1000-SH-002 — Access Control & Smart Locks

## Architecture

Two-track solution for different door categories:

| Track | Product | Application |
|---|---|---|
| Primary (perimeter + main entry) | SALTO Neo Cylinder + KS Cloud | Main entry, garage entries, service door, gate — enterprise-grade, KNX-native, audit trail |
| Secondary (interior / aesthetic) | Level Lock+ Connect or SALTO XS4 | Interior doors where minimal visual presence preferred — Matter/HomeKit bridge to Basalte |

## 1. Primary — SALTO Neo Cylinder + KS Cloud

| Parameter | Specification |
|---|---|
| Model | SALTO Neo Cylinder |
| Platform | SALTO KS Cloud |
| Access methods | BLE, NFC/RFID, PIN, physical key fallback |
| Integration | KNX via SALTO gateway; 2N IP Style intercom; Josh.ai |
| Audit trail | Full access log in cloud; remote unlock; time-based access schedules |
| Security | Enterprise-grade wireless encrypted |
| Use case | All perimeter doors; garage entry/exit; service entries |

Confirmed selection over Yale Luna Pro+ and Lockly Visage following evaluation — SALTO offers superior enterprise integration, KNX compatibility, and Australian installer support.

## 2. Intercom — 2N IP Style

| Parameter | Specification |
|---|---|
| Model | 2N IP Style |
| Display | 10" touchscreen |
| Camera | 5 MP wide-angle |
| Features | Facial recognition, QR code, LPR plate recognition, PIN, fob |
| Rating | IP65 — suitable for all external positions; rain hood for fully exposed gates |
| Integration | KNX, Josh.ai, Inner Range Integriti, HomeKit |
| Quantity | All entry points and gates |
| Supplier | CSM / Anixter / Hills Ltd (AU) |

## 3. Vehicle Gate

- **Gate operator:** FAAC automatic — KNX relay-controlled
- **LPR:** Nedap ANPR license plate recognition — integrated with 2N IP Style
- **Scene:** Vehicle detected → Kaleidescape-style gate-open trigger → garage wash-bay door sequence begins (see RFQ-1000-GAR-001)

## 4. Inner Range Integriti Platform

- Australian-made enterprise security and access platform
- Grade A1 rated
- Integrates: 2N IP Style intercoms, SALTO access, surveillance cameras, KNX alarm inputs
- Single pane of glass for all security events
- Back-to-base monitoring ready: Chubb or Wilson Security Grade A1

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| SALTO Neo Cylinder + KS Cloud (all doors) | $25,000–$35,000 |
| 2N IP Style intercoms + rain hoods (all entry points) | $18,000–$25,000 |
| FAAC gate operator + Nedap ANPR LPR | $12,000–$18,000 |
| Inner Range Integriti platform + programming | $20,000–$28,000 |
| Installation and integration | $8,000–$12,000 |
| **Total** | **$83,000–$118,000** |

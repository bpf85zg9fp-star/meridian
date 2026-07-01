---
document_id: "RFQ-1014-001"
title: "Meridian Estate — Build Team, Project Management & Timeline"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Project Management"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1014-001 is provisional. New RFQ domain."
parent_rfq: "RFQ-1014"
reviewed_by: "Claude (L2A)"
source_batch: "002"
source_conversations:
  - "2025-11-27 — Estate home team recommendations"
  - "2025-11-27 — Staff recommendations estate home"
  - "2025-12-02 — Estate home timeline"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
---

# RFQ-1014-001 — Build Team, Project Management & Timeline

## 1. Recommended Project Management Structure (Three-Layer)

| Layer | Recommended | Role |
|---|---|---|
| National PM (oversight/audit) | RLB — Rider Levett Bucknall Australia | Independent national-tier oversight; validates local builder costings; audits quality/timeline/supply chain/scope creep; national procurement (Christie/Barco, Apple ecosystem, specialty plant); does NOT recommend trades |
| Local PM (day-to-day) | Build Project Management SA or BCA Projects Adelaide (later revised from initial EPIC Projects & Consulting recommendation) | On-site daily/weekly presence; trade coordination and sequencing; quality control; verifies RFQ specifications executed exactly; can recommend trades but builder should choose, local PM supervises |
| Engineering PM (technical disciplines only) | Mott MacDonald / Wavetrain-class firms | Hydronics, HVAC engineering, 10G network infrastructure, cinema acoustic isolation, structural/power load specialists — recommends own vetted teams for these disciplines only |

**Note on evolution:** the initial recommendation (EPIC Projects + Savills PM + WGA engineering + Finesse Built) was superseded once the brief escalated from "high-end custom home" to "commercial-grade ultra-luxury estate" (theatre, hydronics, robotics, coolroom, 10G, pool grotto, LaundryJet, Lutron, full infrastructure stack). Finesse Built specifically was flagged as excellent for $1.5M–$4M luxury homes but not matched to the escalated scope.

## 2. Realistic Construction Timeline

**Total: 30–42 months** (zero-compromise, zero-defect, Day-1 fully operational standard — not a "move in while trades finish" approach)

| Phase | Duration | Kevin's on-site presence |
|---|---|---|
| Design, planning & engineering | 6–10 months | Moderate–high; week-long sessions every 1–2 months for major design milestones |
| Construction start → rough-in | 12–18 months | Low–moderate; ~1 week/month first 12 months, then every 2–3 weeks approaching drywall/insulation |
| Internal fit-out, millwork, custom systems | 6–10 months | High; theatre/AV calibration, automation, cabinetry, stonework, lighting all require direct approval |

## 3. Household Staff & Operations Infrastructure

### 3.1 New Infrastructure Recommended (Not Previously Specified)

| Addition | Purpose |
|---|---|
| Estate Operations Room (staff hub) | Adjacent to laundry/service corridor; Basalte Ellie panel, 2N intercom, staff lockers, digital whiteboard, iPad charging, uniform staging |
| Second Deep Storage Room | Seasonal decor, spare filters (Zehnder/water/HVAC), spare smart devices, spare LED drivers, irrigation parts, robot mower consumables |
| Contractor Access Centre | Discreet trade/vendor entrance — key lockers, sign-in iPad with NDA workflow, temporary Wi-Fi, boot wash + PPE station |
| Secure Vendor Staging Area | Delivery holding area — cameras, fridge, lockable shelving, QR labelling |
| Technical Shop Room | Staff-only technical workspace |
| Estate Operations Wing | Consolidates the above into a single new major RFQ section (drafted in source as "Section 48") |

### 3.2 Operations Software Stack

| System | Role | Recommended |
|---|---|---|
| CMMS (maintenance) | Work orders, preventive maintenance scheduling, asset tracking | UpKeep (chosen over Limble — better fit for residential/hospitality-style workflow vs Limble's industrial focus) |
| Indoor GIS | Searchable interactive estate map — tap "irrigation valve 3B", get pin + navigation | ArcGIS Indoors (Esri) |
| SOP/training | Converts product manuals into step-by-step staff SOPs, auto-scheduled via UpKeep | Trainual |
| Staff rostering | GPS-secured clock-in/out, leave requests, AU award compliance | Deputy |
| Access/sign-in | NDA workflow, safety briefings | Sine Pro or Envoy |

**Integration logic:** Deputy manages WHEN staff work; Trainual manages HOW; UpKeep manages WHAT needs maintenance; ArcGIS Indoors shows WHERE. Sensors (vibration, runtime, temperature, humidity, VOC) feed UpKeep automatically — largely eliminating manual staff data entry.

### 3.3 Estate-Wide Sensor Categories (for CMMS integration)
Whole-estate environmental (temp/humidity/VOC/CO₂/noise), mechanical/plant room (vibration/runtime), hydronics/HVAC, electrical/power, water/irrigation/pool, kitchen/pantry/coolroom/laundry, theatre/AV/IT/rack room, garage/car wash/workshop, bedrooms/bathrooms/living, safety/security, pet systems.

## 4. Cost & Coordination Notes

- National PM does not recommend trades — pure oversight/audit function
- Local PM may recommend trades but for a project of this scale, better practice is: builder chooses trades, local PM supervises, national PM audits
- Engineering PM only recommends/requires trades for highly specialised technical disciplines

## 5. Outstanding RFQ Confirmations

- Final selection between EPIC/Savills/WGA (original) vs RLB/Build Project Management SA/BCA/Mott MacDonald (revised) not locked — source shows evolution but no final confirmed team
- UpKeep, ArcGIS Indoors, Trainual, Deputy licensing costs itemised in source but not fully captured in this extraction pass — flagged for follow-up (RFQ-1018 series)

## 6. Pipeline Status

| Stage | Status |
|---|---|
| L2A (Claude) | ✅ Extracted 2026-06-29 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 002, three conversations 2025-11-27 to 2025-12-02*

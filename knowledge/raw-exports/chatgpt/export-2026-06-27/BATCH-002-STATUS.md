---
document_id: "KNOWLEDGE-BATCH-002"
title: "Ingestion Batch 002 — ChatGPT Export (uploaded 2026-06-29, second copy)"
version: "1.0"
status: "Raw received — classification complete — priority extraction complete, audit-series extraction pending"
classification: "Infrastructure / Knowledge Management"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# Ingestion Batch 002 — Status

**Source file:** `conversations-002.json`  
**Date range:** 2025-11-16 to 2026-01-11  
**Total conversations:** 100  
**Programme-relevant (estimate):** ~86  
**Not programme-relevant:** personal/family items (self-defence advice, Christmas gifts for boys, playlists, pet names, Family Draw System, festive menus) — not extracted, noted only

---

## ⚠️ Critical Findings — Requires Kevin's Decision

### F-001 (Critical) — Competing RFQ numbering scheme discovered in source
The 2026-01-10 conversation "RFQs Overview and Breakdown" shows ChatGPT consolidating all estate discussion into its own internal structure: **1 Master Estate RFQ + 14 numbered subordinate RFQs** (e.g. "3. Home Theatre Reference RFQ", "10. Vehicle Fleet RFQ", "11. Resort/Hotel RFQ", "13. Estate Pantry, Coolroom & Provisions RFQ", "14. Estate Wardrobe, Closet & Personal Effects RFQ"). This numbering is **internal to that ChatGPT thread only** and has no relationship to the repository's RFQ-1000+ ecosystem numbering.  
**Treatment applied:** RFQ-1000+ remains the sole authoritative numbering per Kevin's standing instruction (2026-06-28). ChatGPT's 1–14 structure is logged as source content only, not adopted as a parallel scheme.  
**Decision needed:** Confirm this treatment, or advise if any mapping/cross-reference to ChatGPT's internal numbering is wanted.

### F-002 (Critical) — Source material self-contradicts on theatre projector selection
- 2025-11-20 "Christie vs Barco projectors": extensive technical comparison of Christie Eclipse G3 vs Barco Heimdall+ — no definitive selection recorded; conversation continues assuming an Eclipse G3 build (room dimensions, screen, lens, booth all specified around Eclipse)
- 2025-12-02 "Estate quality audit" and 2026-01-05 "Estate Quality Enhancement Audit": both refer to **"Barco Thor+"** as the already-locked projector ("KEEP — no substitutes recommended"), alongside Trinnov, madVR Envy, Kaleidescape
- This is neither of the two projectors actually compared on Nov 20, and conflicts with `rfq/estate/home-theatre/Christie-Eclipse.md` already committed to this repository from Batch 000
**Decision needed:** Which projector is actually specified — Christie Eclipse (G3), Barco Thor+, or Barco Heimdall? The full room/screen/booth design work from Nov 20 (see RFQ-1000-HT-011 below) was built around Eclipse G3 dimensions and will need re-validation if the projector changes.

---

## Processing Status

| Step | Status |
|---|---|
| File received | ✅ 2026-06-29 |
| Total conversation count | ✅ 100 confirmed |
| Classification | ✅ Complete |
| Critical findings identified | ✅ F-001, F-002 above |
| High-priority extraction | ✅ Complete (8 documents) |
| Audit-series extraction (materials/furniture/appliances/wardrobe/linen) | ⏳ Pending — lower marginal value (mostly upgrade suggestions on already-specified items); flagged for follow-up |
| Estate de-branding framework (full detail) | ⏳ Pending |
| Estate colour/brick palette (full detail) | ⏳ Pending |
| Staffing systems detail (UpKeep/ArcGIS/Trainual/Deputy) | ⏳ Pending |
| Hotel autonomous-operations detail | ⏳ Pending |

---

## Conversation Inventory — All 100

| Date | Title | Domain | Target | Priority |
|---|---|---|---|---|
| 2025-11-16 | Air conditioning vent recommendations | Estate HVAC | RFQ-1000-HVAC | Low |
| 2025-11-17 | Yacht ownership opportunities | Marina | RFQ-1007 | ⭐ High |
| 2025-11-18 | POS-triggered slideshow setup | Resort Tech | RFQ-1010 | Low |
| 2025-11-18 | Mobile plan recommendations | Lifestyle/Tech | RFQ-1003 | Low |
| 2025-11-20 | Christie vs Barco projectors | Estate Home Theatre | RFQ-1000-HT | ⭐ Critical (F-002) |
| 2025-11-21 | Vacuum Wars robot vacuums | Estate | RFQ-1000 | Low |
| 2025-11-22 | Off-road camper upgrades | Vehicles | RFQ-1002 | Medium |
| 2025-11-23 | KNX camera support features | Estate Smart Home | RFQ-1000-SH | Low |
| 2025-11-24 | D&D starter set recommendations | Lifestyle/Family | — | Low |
| 2025-11-25 | Luxury D&D Experience Tips | Lifestyle/Family | — | Low |
| 2025-11-25 | Motorbike garage entry solution | Estate Garage | RFQ-1000-GAR | Low |
| 2025-11-26 | Weekly estate expenses | Financial | RFQ-1011 | ⭐ Critical |
| 2025-11-26 | Luxury food and drink recommendations | Lifestyle | RFQ-1003 | Low |
| 2025-11-26 | Soil treatment recommendations | Estate Outdoor | RFQ-1000-OUT | Low |
| 2025-11-26 | Rain garden definition | Estate Outdoor | RFQ-1000-OUT | Low |
| 2025-11-26 | Apple Music visual setup | Estate AV | RFQ-1000-AV | Low |
| 2025-11-27 | Kris Kringle gift ideas | Lifestyle | — | Low |
| 2025-11-27 | Estate home team recommendations | Estate/PM | RFQ-1014 | ⭐ High |
| 2025-11-27 | Toolbox recommendations for estate | Estate | RFQ-1000 | Low |
| 2025-11-27 | Staff recommendations estate home | Estate Operations | RFQ-1014 | ⭐ High |
| 2025-11-28 | Quiet hand dryer solutions | Estate Bathrooms | RFQ-1000-BTH | Low |
| 2025-11-29 | Hotel software recommendations | Resort Tech | RFQ-1010 | High |
| 2025-11-29 | Rubbish vacuum systems | Estate | RFQ-1000 | Low |
| 2025-11-29 | Ultra-luxury Christmas decor | Lifestyle | — | Low |
| 2025-11-30 | Teeth whitening tips | Health/Family | — | Low |
| 2025-11-30 | Facial waxing for men | Health/Family | — | Low |
| 2025-12-02 | Bentley and Triumph complaints | Vehicles | RFQ-1002 | High |
| 2025-12-02 | Estate quality audit | Estate | RFQ-1018 | High — contains F-002 |
| 2025-12-02 | Estate home timeline | Estate/PM | RFQ-1014 | ⭐ High |
| 2025-12-02 | Estate voice strategy | Estate Smart Home | RFQ-1000-SH | Medium |
| 2025-12-02 | Toilet sensing integration | Estate Bathrooms | RFQ-1000-BTH | Low |
| 2025-12-03 | Ultra-luxury vehicle recommendations | Vehicles | RFQ-1002 | Low |
| 2025-12-03 | Luxury wardrobe upgrades | Lifestyle Fashion | RFQ-1003 | Medium |
| 2025-12-04 | Wardrobe audit recommendations | Lifestyle Fashion | RFQ-1018 | Medium |
| 2025-12-04 | Luxury wardrobe audit | Lifestyle Fashion | RFQ-1018 | Medium |
| 2025-12-05 | Ultra-luxury linen audit | Estate Bedrooms | RFQ-1018 | Medium |
| 2025-12-06 | Hot water system solutions | Estate HVAC | RFQ-1000-HVAC | Low |
| 2025-12-06 | Furniture quality audit | Estate Living | RFQ-1018 | Medium |
| 2025-12-06 | Audit of estate materials | Estate Structure | RFQ-1018 | Medium |
| 2025-12-06 | Ultra-luxury appliance audit | Estate Kitchen | RFQ-1018 | Medium |
| 2025-12-08 | Plumbed pet waterer audit | Estate Pet Suite | RFQ-1000 | Low |
| 2025-12-09 | Hotel trolley recommendations | Resort | RFQ-1001 | Low |
| 2025-12-09 | Self defence techniques advice | Personal | — | — |
| 2025-12-10 | Vuly recommendation assessment | Estate/Family | RFQ-1000 | Low |
| 2025-12-10 | Luxury modern sword options | Lifestyle | RFQ-1003 | Low |
| 2025-12-11 | Estate luxury recommendations | Estate | RFQ-1000 | Low |
| 2025-12-12 | Luxury sliding door recommendations | Estate Structure | RFQ-1000-STR | Low |
| 2025-12-12 | Weed whacking robot alternatives | Estate Outdoor | RFQ-1000-OUT | Low |
| 2025-12-13 | AI for vehicles fashion diet | General | — | Low |
| 2025-12-14 | Ultra-luxury light show | Estate Outdoor | RFQ-1000-OUT | Low |
| 2025-12-19 | Washing custom Bentley tips | Vehicles | RFQ-1002 | Low |
| 2025-12-20 | Efficient estate engineering | Estate | RFQ-1000 | Low |
| 2025-12-21 | Luxury carpet and stone flooring | Estate Structure | RFQ-1000-STR | Low |
| 2025-12-21 | Christmas ham recommendation | Lifestyle | — | — |
| 2025-12-23 | Christmas Movies for AV | Estate AV | — | — |
| 2025-12-24 | Christmas Gifts for Boys | Family | — | — |
| 2025-12-26 | Industrial Metal Techno Playlist | Lifestyle | — | — |
| 2025-12-26 | Industrial Photography Request | — | — | — |
| 2025-12-26 | Luxury Cat Toy Recommendations | Estate Pet | RFQ-1000 | Low |
| 2025-12-26 | Estate Laundry Design | Estate Bathrooms | RFQ-1000-BTH | Low |
| 2025-12-28 | Infrasonic Bass Capability | Estate Home Theatre | RFQ-1000-HT | High |
| 2025-12-28 | Bentley Upgrades and Alternatives | Vehicles | RFQ-1002 | High |
| 2025-12-31 | Wheel Recommendation Landcruiser Bruder | Vehicles — NEW: LC300 | RFQ-1002 | ⭐ Critical |
| 2025-12-31 | Colour Synergy Landcruiser Bruder | Vehicles | RFQ-1002 | Low |
| 2025-12-31 | Pest Control for Estates | Estate | RFQ-1000 | Low |
| 2025-12-31 | Toyota Bruder Accessories Tips | Vehicles | RFQ-1002 | Medium |
| 2025-12-31 | Diesel Recommendation for LC300 | Vehicles | RFQ-1002 | Medium |
| 2025-12-31 | NYE Celebration Ideas Adelaide | Lifestyle | — | — |
| 2025-12-31 | Estate Birthday Celebration Ideas | Family | — | — |
| 2025-12-31 | Easter Celebration at Estate | Family | — | — |
| 2025-12-31 | Estate Home Music Suggestions | Lifestyle | — | — |
| 2026-01-02 | Estate Lounge Room Design | Estate Living | RFQ-1000-LIV | Low |
| 2026-01-02 | Alcohol Tasting Bar Design | Estate Kitchen/Bar | RFQ-1000-KIT | Medium |
| 2026-01-02 | Estate Space Recommendations | Estate | RFQ-1000 | Low |
| 2026-01-03 | Perlisten vs Focal Audio | Estate AV | RFQ-1000-AV | ⭐ High |
| 2026-01-03 | Ultra-Luxury Dolby Atmos Speakers | Estate Home Theatre | RFQ-1000-HT | High |
| 2026-01-04 | Dakar Rally Viewing Tips | Lifestyle | — | — |
| 2026-01-05 | Interim Property Recommendations | Estate/Land | RFQ-1006 | Medium |
| 2026-01-05 | Estate Quality Enhancement Audit | Estate | RFQ-1018 | High — contains F-002 |
| 2026-01-05 | Estate Clothing & Footwear Audit | Lifestyle Fashion | RFQ-1018 | Medium |
| 2026-01-05 | Estate-Level Wardrobe Plan | Lifestyle Fashion | RFQ-1003 | Medium |
| 2026-01-05 | Landcruiser GX Sport Recommendation | Vehicles | RFQ-1002 | ⭐ High |
| 2026-01-06 | Estate De-Branding Framework | Estate Governance | RFQ-1020 | Medium |
| 2026-01-06 | Estate Clothing Maintenance Team | Estate Operations | RFQ-1014 | Low |
| 2026-01-06 | Kaleidescape Immersive Audio Titles | Estate AV | RFQ-1000-HT | Low |
| 2026-01-06 | Pool Design Recommendations | Estate Outdoor | RFQ-1000-OUT | Medium |
| 2026-01-06 | Studying Wealth Preservation | Financial | RFQ-1004 | Medium |
| 2026-01-06 | Estate Living Book Recommendations | Lifestyle | — | — |
| 2026-01-07 | Australian Estate Design | Estate | RFQ-1000 | Low |
| 2026-01-08 | Living the Estate Life | Estate/Lifestyle | RFQ-1000 | Low |
| 2026-01-08 | H&L POS Till Float | Resort Tech | RFQ-1010 | Low |
| 2026-01-08 | Home Schooling Recommendation | Health/Family | RFQ-1005 | Low |
| 2026-01-08 | Digital Asset Storage System | Estate Tech | RFQ-1000-SH | Low |
| 2026-01-09 | Family Draw System | Family | — | — |
| 2026-01-09 | Funeral and Wedding Attire | Lifestyle Fashion | RFQ-1003 | Low |
| 2026-01-10 | RFQs Overview and Breakdown | Governance | — | ⭐ Critical (F-001) |
| 2026-01-10 | Estate Operating Framework | Governance | RFQ-1015 | ⭐ High |
| 2026-01-10 | Estate Pet Name Suggestions | Family | — | — |
| 2026-01-11 | Loyalty Club Recommendations | Financial | RFQ-1004 | Medium |
| 2026-01-11 | Kitchen Utensil Organisation | Estate Kitchen | RFQ-1000-KIT | Low |

---

## RFQ ID Assignments — Batch 002 New Reservations

| ID | Domain | Status |
|---|---|---|
| RFQ-1014 | Estate — Build Team, Project Management & Timeline | ✅ Extracted |
| RFQ-1015 | Estate — Operating Framework / Governance Charter | ✅ Extracted (summary) |
| RFQ-1018 | Estate — Quality Audit Series (materials/furniture/appliances/wardrobe/linen) | ⏳ Reserved — not yet extracted |
| RFQ-1020 | Estate — De-Branding Framework | ⏳ Reserved — not yet extracted |

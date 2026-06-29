---
document_id: "RFQ-1000-STR-001"
title: "Meridian Estate Structure — Cladding, Glazing, Bushfire & Energy"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Structure"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-STR-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-07-20 — Ultra Luxury Smart Home"
  - "2025-07-22 — RFQ Consolidation"
  - "2025-08-21 — Front door recommendation"
  - "2025-08-21 — Match flooring and bricks"
  - "2025-08-23 — mmWave vs beam cutters"
  - "2025-08-24 — Home recommendations for resilience"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$1,200,000–$1,500,000"
---

# RFQ-1000-STR-001 — Structure, Cladding, Glazing & Bushfire

## 1. Architectural Type

- Single-level slab construction; RSJ-framed
- Earth-bermed wings for theatre, wellness, and service areas
- Internal courtyard/lightwell with motorised skylights
- Room-within-room home theatre: concrete floating floor + full acoustic shell

## 2. External Cladding & Materiality

| Element | Specification |
|---|---|
| Primary walls | PGH Blue Steel Flash Metallic — solid double brick (120 mm internal + 120 mm external; cavity) |
| Roof | VMZinc Anthra Zinc standing seam — BAL-FZ rated |
| Non-brick external | VMZinc Anthra Zinc flat panel / standing seam cladding |
| Soffits & fascias | VMZinc Anthra Zinc |
| Pavilion cladding | VMZinc Anthra Zinc (matches main residence) |
| Interior Anthra Zinc accents | Theatre entry doors, feature wall reveals, stair balustrades |

**Colour coherence note:** PGH Blue Steel Flash Metallic brick + VMZinc Anthra Zinc pairing confirmed during planning as achieving the desired dark, luxurious aesthetic without jarring contrast. Flooring (natural stone/porcelain in wet zones; Karndean Korlok in living areas) to be selected to complement this palette.

## 3. Glazing

| Type | Specification |
|---|---|
| Standard glazing | Triple-glazed; BAL-FZ rated; thermally broken aluminium or steel frames; neutral Low-E tint; Schüco / Reynaers / AWS |
| Smart glass | SageGlass or Halio electrochromic in all bedrooms and home theatre — instant blackout + privacy on demand |
| Standard cost | AUD $1,500–$2,000/m² |
| Electrochromic cost | AUD $2,500–$3,000/m² |

## 4. Flooring

| Zone | Material |
|---|---|
| Kitchen, bathrooms, mudroom, outdoor paths | Porcelain or natural stone |
| Living and games areas | Karndean Korlok or wool carpet |
| Garage and walkways | Polished concrete |
| Lawns | Sir Walter Buffalo turf (robot-mower compatible) |
| All wet zones | Hydronic underfloor heating/cooling |

## 5. Bushfire Protection — BAL-FZ Envelope

| System | Specification | Estimated Cost (AUD) |
|---|---|---|
| BAL-FZ rated envelope | Double brick, fire-rated roofing, ember-proof gutter/vent mesh (Embertec) | $350,000 |
| Ember-attack shutters | EBSA automatic deployment over all glazing on fire threat | $120,000 |
| Perimeter drenching | Stainless roof + perimeter misting; underground tank + electric primary + diesel backup pump | $180,000 |
| 100,000 L fire tank + dual pumps | Underground tank; Davey/Grundfos; diesel backup | $95,000 |
| CFS/KNX smart integration | KNX/Josh.ai fire-mode triggers; auto: drenchers, shutters, lockdown, drone launch | $18,000 |
| Total bushfire package | | $735,000–$857,000 |

**APZ:** 50 m managed cleared buffer around all structures; maintained continuously by Mammotion Luba AWD 10000X fleet.

## 6. Solar & Energy

| System | Specification |
|---|---|
| Roof solar | Mono-crystalline high-efficiency panels (≥22%) |
| Ground array | Bifacial panels (east lawn; tilted for winter sun) |
| Pavilion | Optional perovskite-glass BIPV shingles |
| Primary battery | 3× Tesla Powerwall 3 (grid-tied + blackout islanding) |
| Supplemental battery | 2× EcoFlow Ocean Pro 10 kWh (AI-controlled indoor UPS-grade) |
| Hydrogen backup | LAVO / Enapter — 1-week off-grid autonomy target |
| Smart energy management | KNX load-shedding; Solar Analytics Gateway; scene charging modes; Basalte Lena dashboards |
| VPP | Optional Virtual Power Plant participation |

## 7. HVAC & Environmental

| System | Specification |
|---|---|
| Hydronic | Underfloor heating/cooling (Stiebel or Rehau chiller); zoned manifolds |
| Supplementary AC | Ducted inverter zones as required |
| ERV | Zehnder ComfoAir Q600 — CO₂ sensor-triggered (>900 ppm) |
| Air quality | CO₂, PM2.5, VOCs, humidity sensors in every occupied room |
| PCM thermal mass | Phase-change material in slab and north-facing walls (15–19% HVAC saving) |
| Geothermal | HVAC loops for wellness suite and theatre |
| Greywater | GreySmart 500 L surge tanks; filtered reuse for toilets and irrigation |
| Scent | Whole-home essential oil diffusion via HVAC; KNX/Josh.ai controlled |

## 8. Network Infrastructure

| System | Specification |
|---|---|
| Primary WAN | NBN Enterprise Ethernet 10 Gbps — mandatory |
| Backup WAN | Starlink Business — mandatory satellite redundancy; auto-failover |
| SD-WAN | Peplink aggregator — dual-link failover |
| Core switching | UniFi 10GbE + Cisco Meraki/Pakedge Layer 3 (VLANs, QoS) |
| Wi-Fi | Enterprise Wi-Fi 6E — Juniper Mist or Aruba mesh |
| Cabling | Cat6A structured + fibre-optic backbone; 10G/40G |
| NAS/Server | Synology RS3621xs+; fireproof vault with KNX-integrated thermal alerts |

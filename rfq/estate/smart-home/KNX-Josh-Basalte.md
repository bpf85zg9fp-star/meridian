---
document_id: "RFQ-1000-SH-001"
title: "Meridian Estate Smart Home — KNX, Josh.ai & Basalte Lena Backbone"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Smart Home"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-SH-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-20 — Smart home tech recommendations"
  - "2025-08-21 — Best smart locks luxury"
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$420,000–$500,000"
---

# RFQ-1000-SH-001 — KNX, Josh.ai & Basalte Lena Backbone

## Architecture Summary

Three-layer stack confirmed as world-class for ultra-luxury residential in Australia:

| Layer | System | Role |
|---|---|---|
| Infrastructure | KNX Secure IP (dual-bus fallback) | Backbone: lighting, HVAC, blinds, access, pool, security, irrigation |
| Interface | Basalte Lena (18+ units) | Wall control in every room including all bathrooms |
| Intelligence | Josh.ai Core + Nano mics | Natural language voice; AI scene orchestration; local processing |

## 1. KNX

- **Standard:** ISO/IEC 14543 — open international building automation standard; formally adopted AU/NZ
- **Architecture:** Dual-bus twisted-pair + KNX IP backbone; TP + IP hybrid for resilience
- **Security:** KNX Secure (encrypted) — mandatory for all new installations
- **Scope:** Lighting (all zones), HVAC zone control, motorised blinds, access control relays, pool/irrigation circuits, energy monitoring, security sensor inputs, garage door control
- **Fallback:** If IP backbone fails, TP bus maintains all local automation independently
- **Installer base:** Wide in Australia — certified KNX integrators available in SA

## 2. Basalte Lena

- **Model:** Basalte Lena — Basalte's flagship wall panel
- **Display:** 10.1" full-HD touchscreen; OLED-quality; proximity and ambient light sensor; multi-touch
- **Features:** Integrated intercom/video doorbell feed, camera preview, microphone; Basalte Home app integration
- **Finish:** Premium metal/glass; designed for flush architectural installation
- **Quantity:** 18+ units — every room including all bathrooms, garage, entry, outdoor pavilion (covered)
- **Roles per zone:**
  - Living/dining/kitchen: lighting scenes, blind position, HVAC setpoint, AV scene launch, security arm
  - Bedrooms: sleep scenes, wake scenes, blackout blind, temperature, do-not-disturb
  - Bathrooms: shower temperature (where applicable), towel rail, exhaust fan, mirror light, music zone
  - Theatre: scene recall, volume display, projector status
  - Garage: door status, EV charger status, wash bay state
  - Pool pavilion: pool temperature, lighting, AV zone, gate status

## 3. Josh.ai

- **Product:** Josh Core (central processor) + Josh Nano (room microphones, every zone)
- **Processing:** On-premise — no cloud dependency for command execution; privacy-first
- **Capability:** Multi-command natural language (e.g. "Josh, start the movie, dim to 10%, close the blinds and set temperature to 21")
- **Integrations:** KNX, Lutron, Basalte, Sonos, Naim CI, Kaleidescape, Apple TV, security panels
- **Scene logic:** Josh.ai orchestrates complex multi-system scenes that KNX alone cannot execute across different protocols
- **Key scenes:** Movie Mode, Wellness Morning, Goodnight, Entertain, Fire Mode, Hi-Res Listening, Guest Arrival

## 4. Supporting Systems

### 4.1 Presence Sensing
- **Steinel True Presence KNX** mmWave sensors — every room
- Detects micro-motion (breathing, typing) — eliminates false vacancy triggers
- Outputs: presence/absence, brightness, humidity, CO₂, VOCs, temperature
- Native KNX integration — feeds HVAC, lighting, and scene logic directly

### 4.2 Environmental Sensing
- **Thermokon KNX multi-sensors** (dedicated flush-mounted temperature/humidity/CO₂/VOC/light probes) in each zone — separate from Steinel for HVAC accuracy
- Lena's integrated temp sensor used as UI display / backup only

### 4.3 Lighting Control
- **Lutron HomeWorks QSX + Ketra** — tunable white/RGBW architectural lighting; museum-grade dimming; DALI2 via Gira DALI Gateway Plus for extended zones
- **Lutron Palladiom Sivoia QS** motorised blinds — wired motors; dual-layer blackout/sheer; native HomeWorks QS and Josh.ai integration

### 4.4 Automatic Sliding Doors
- **TORMAX iMotion 2301** — Swiss, hospital-grade, near-silent; sensor-driven; KNX-integrable
- Covers all internal sliding door transitions (living/outdoor, butler's pantry, bedroom wings)

### 4.5 Power Points & Plates
- **ZETR trimless systems** — flush, invisible in all living/bedroom/circulation zones
- **Hager Silhouette** slim plates where plate preferred (skirting, service areas)
- All USB-C PD outlets: Legrand Excel Life 60W (study, islands, guest rooms)

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| KNX infrastructure (bus cabling, actuators, gateways, programming) | $120,000–$150,000 |
| Josh.ai Core + Nano units (18+) + programming | $35,000–$45,000 |
| Basalte Lena panels (18+) + Basalte Home server + programming | $90,000–$110,000 |
| Steinel True Presence KNX sensors (18+ rooms) | $25,000–$35,000 |
| Thermokon KNX multi-sensors | $12,000–$18,000 |
| Lutron HomeWorks QSX + Ketra + DALI2 | $80,000–$95,000 |
| Lutron Palladiom Sivoia QS motorised blinds (all zones) | $45,000–$60,000 |
| TORMAX iMotion 2301 sliding door operators | $15,000–$20,000 |
| ZETR / Hager / Legrand power point fitout | $18,000–$25,000 |
| **Total** | **$440,000–$558,000** |

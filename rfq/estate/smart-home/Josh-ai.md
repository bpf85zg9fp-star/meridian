---
document_id: "RFQ-1000-SH-002"
title: "Meridian Estate Smart Home — Josh.ai Voice Control"
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
  - "2025-07-19 — Master RFQ Request"
  - "2025-08-20 — Smart home tech recommendations"
  - "2025-08-20 — Master RFQ review"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$45,000–$60,000"
primary_supplier: "Josh.ai / AV Integrator"
---

# RFQ-1000-SH-002 — Josh.ai Voice Control

## Overview

Josh.ai is the AI voice control and scene orchestration layer for the Meridian Estate. It sits above KNX and provides natural language control, room-aware intelligence, and privacy-first local processing. Selected over Amazon Alexa and Google Home for its luxury residential focus, local-first architecture, and superior integration depth.

---

## 1. Hardware

| Device | Placement | Function |
|---|---|---|
| Josh.ai Core | Server rack (equipment bay) | Central AI brain; KNX gateway; API hub |
| Josh.ai Nano | Every room | Wake word detection; room-aware context; always-on local processing |

Number of Nano units: approximately 20–25 (one per room/zone across all bedrooms, living areas, theatre, office, kitchen, bathrooms, garage, outdoor pavilion).

## 2. Key Capabilities

- **Natural language:** Understands complex commands — “Turn on the movie” launches the full Movie Mode KNX scene
- **Room awareness:** Knows which room you’re in; “Turn off the lights” affects only the current room
- **Privacy-first:** All processing local; no audio uploaded to cloud servers
- **Scene orchestration:** Custom scenes trigger multiple KNX group addresses simultaneously
- **Panic override:** “Josh, fire mode” triggers the full Fire Mode emergency sequence
- **Guest mode:** Simplified voice commands for guests; restricted access to security functions

## 3. Integration

| System | Integration |
|---|---|
| KNX | Native KNX IP gateway; reads/writes all group addresses |
| Basalte Lena | Complementary — Basalte provides touch; Josh provides voice |
| Kaleidescape | IP control; “Play [film title]” |
| Christie Eclipse | Scene relay via KNX |
| Trinnov Altitude32 | IP control for volume and input |
| Naim CI | IP control for zone audio |
| Roon Nucleus+ | Roon API for music playback |
| Lutron HomeWorks QS | Native Josh.ai – Lutron integration |
| 2N IP Style | Door/gate intercom relay |
| Apple HomeKit | HomeKit bridge for iPhone/iPad native control |

## 4. Selected Voice Scenes

| Command | Action |
|---|---|
| “Good morning” | Hydronic warm, HRV cycle, blinds open, citrus diffuser, soft playlist |
| “Start the movie” | Lights dim, shades close, Christie power-on, Kaleidescape launch, seats recline |
| “Goodnight” | Gate close, locks engage, mmWave arm, lights off, HVAC night mode |
| “We have guests” | Entry lighting on, gate open, pool ambient, outdoor audio on |
| “Fire mode” | Drenchers, ember shutters, lockdown, drone launch, satellite comms |
| “Hi-res listening session” | Mac Mini wake, DAC on, Naim amp on, warm light, cedar diffuser |

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Josh.ai Core | $8,000 |
| 22× Josh.ai Nano | $22,000 |
| Programming and scene configuration | $12,000–$25,000 |
| Integration testing | $3,000–$5,000 |
| **Total** | **$45,000–$60,000** |

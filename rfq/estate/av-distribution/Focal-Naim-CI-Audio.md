---
document_id: "RFQ-1000-AV-001"
title: "Meridian Estate AV Distribution — Whole-Home Audio (Focal/Naim CI)"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / AV Distribution"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-AV-001 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-07 — Tier 5 audiophile system"
  - "2025-08-10 — Amplifier power and speaker compatibility"
  - "2025-09-02 — Kaleidescape video and music quality"
  - "2025-09-12 — Home theater upgrades recommendations"
  - "2025-08-20 — Smart home tech recommendations"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$350,000–$450,000"
---

# RFQ-1000-AV-001 — Whole-Home Audio (Focal/Naim CI)

## Selection Rationale

Focal 1000 Utopia in-wall/ceiling paired with Naim CI amplification is the confirmed Tier 5 selection for whole-home distributed audio. Both brands are owned by VerVent Audio Group and are engineered for synergy. This pairing is considered the highest-end residential distributed audio combination on the market.

Basalte Asano was evaluated and rejected for whole-home use: sonically inferior to Naim CI, though its KNX-native integration is strong. Asano is retained as an option for secondary service zones only.

## 1. Speakers — Focal 1000 Utopia Series

| Zone type | Model | Application |
|---|---|---|
| Primary living zones | Focal 1000 Utopia IW6 / IW8 in-wall | Main lounge, dining, kitchen, hallways |
| Ceiling zones | Focal 1000 Utopia IC8 / IC6 in-ceiling | Bedrooms, bathrooms, office, library |
| Design-sensitive zones | Amina Mobius invisible speakers | Bathrooms, dressing suites — zero visual impact |
| Outdoor | Focal Littora OD 108 (garden/landscape) | Estate grounds, pool approach, BBQ area |
| Pool pavilion | Focal OD Stone 8 / OD Sat 5 + OD Sub 12 | Weatherproof outdoor premium audio |
| Underwater | Clark Synthesis AQ339 | Pool — tactile underwater audio |

## 2. Amplification — Naim CI Series

| Model | Channels | Application |
|---|---|---|
| Naim CI-Uniti 102 | 2-channel streamer/amp | Primary living zones — streaming + amplification per zone |
| Naim CI-NAP 108 | 8-channel power amp | Multi-room centralised amplification for bedrooms/bathrooms |
| Naim CI-NAP 101 | Mono amp | Subwoofer and outdoor zone amplification |

All Naim CI units rack-mounted in central AV room. VLAN-separated AV network for low-latency streaming.

## 3. Hi-Res Apple Music Zone

Apple Mac Mini M2 (fanless Akasa Turing chassis) → USB-C → Matrix Element X2 / Linn Selekt DSM DAC → XLR balanced → Naim CI-Uniti 102 line input. Enables bit-perfect 24-bit/192 kHz ALAC playback from Apple Music. Dedicated audio circuit with IsoTek/Torus Power conditioning. Josh.ai scene: "Hi-Res Listening Session."

## 4. Music Server & Streaming

- **Roon Nucleus+** — centralised music library; Roon Ready zones throughout
- **Sources:** Apple Music (ALAC lossless), Qobuz (hi-res streaming), TIDAL (lossless MQA)
- **Kaleidescape Strato C** units at key distributed display zones for premium video/music

## 5. Video Distribution — SDVoE

SDVoE 10GbE over fibre backbone confirmed as mandatory for lossless 4K/8K video distribution. Zero-latency switching. NETGEAR M4300/M4500 SDVoE-certified switching fabric. Encoders/decoders at each source and display location. See RFQ-1000-NET-001 for network infrastructure.

## 6. Display Strategy by Zone

| Zone | Display | Use |
|---|---|---|
| Theatre | Christie Eclipse + Stewart screen | Reference cinema |
| Main lounge | LG OLED G4/M4 Signature 83"+ | Primary family |
| Bedrooms | Samsung The Frame 55"–65" | Art + TV |
| Bar/lounge | Meural Canvas II 27" | Ambient art |
| Kitchen | Samsung The Frame 32" | Art + recipe |
| Office | LG OLED 42" or Apple Studio Display | Work + media |
| Kids | LG OLED 55" or Samsung Serif | Family viewing |
| Pool pavilion | Samsung Terrace (weatherproof) | Outdoor TV |
| Hallways/entry | Meural Canvas II | Digital art |
| Feature (optional) | LG Transparent OLED | Art centrepiece |

## 7. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Focal 1000 Utopia in-wall/ceiling (all zones) | $120,000–$160,000 |
| Amina Mobius invisible speakers (bathrooms/dressing) | $20,000–$28,000 |
| Focal Littora / OD Stone outdoor speakers | $25,000–$35,000 |
| Clark Synthesis AQ339 pool underwater | $4,000–$6,000 |
| Naim CI amplification stack | $45,000–$65,000 |
| Apple Mac Mini M2 + DAC (hi-res zone) | $8,000–$12,000 |
| Roon Nucleus+ | $3,500–$5,000 |
| Meural Canvas II units (6+) | $12,000–$18,000 |
| SDVoE encoders/decoders + switching | $55,000–$75,000 |
| Display units (all zones per strategy above) | $80,000–$110,000 |
| Installation and commissioning | $25,000–$35,000 |
| **Total** | **$397,500–$549,000** |

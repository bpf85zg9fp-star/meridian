---
document_id: "RFQ-1000-HT-003"
title: "Meridian Estate Home Theatre — Kaleidescape Media Server & Players"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-003 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request"
  - "2025-09-02 — Kaleidescape video and music quality"
  - "2025-09-10 — Christie G3 demo scenes"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$55,000–$75,000"
primary_supplier: "Kaleidescape AU / AV Integrator"
---

# RFQ-1000-HT-003 — Kaleidescape Media Server & Players

## Overview

Kaleidescape is the preferred content delivery platform for Meridian Estate theatre. It delivers proprietary lossless video (up to 4K HDR with Dolby Atmos and DTS:X) with no streaming compression. Evaluated and selected over Apple TV, Zappiti, and all streaming alternatives for image quality.

---

## 1. Server

| Parameter | Specification |
|---|---|
| Model | Kaleidescape Terra Prime SSD |
| Storage | 123 TB SSD |
| Function | Central movie library; stores full lossless 4K HDR disc rips |
| Connection | 10GbE to AV rack; connects to all Strato players |

## 2. Players

| Zone | Model | Use |
|---|---|---|
| Main theatre | Kaleidescape Strato V | Full 4K HDR; Dolby Vision; Dolby Atmos; feeds madVR Envy Extreme MK2 |
| Distributed zones | Kaleidescape Strato C | Key display zones requiring premium video; e.g. master bedroom, lounge |

## 3. Key Advantages Over Streaming

- Lossless video: no compression artifacts
- Instant start: no buffering
- Full Dolby Vision and Dolby Atmos bit-rate (not streaming-limited)
- Deterministic playback: always the same output regardless of network conditions
- Movie metadata: auto-populates poster art (used by Mozaex digital marquees)

## 4. Integration

| System | Integration |
|---|---|
| Kaleidescape API | Provides Now Playing metadata to Mozaex digital marquees (poster art, title) |
| KNX / Josh.ai | IP control; playback start/stop triggers movie scene; voice: “Play The Dark Knight” |
| Christie Eclipse | Primary video output from Strato V; 4K HDR chain confirmed |
| madVR Envy Extreme MK2 | Strato V → madVR for HDR tone mapping before Christie Eclipse |
| Trinnov Altitude32 | Audio output from Strato V → Altitude32 for decoding and processing |

## 5. Content Quality

Kaleidescape supports:
- 4K Blu-ray (DCI 4K with full HDR10 and Dolby Vision)
- Dolby Atmos up to full bit-rate (Atmos TrueHD)
- DTS:X Master Audio
- Christie Eclipse commissioning should include Kaleidescape as the primary test source

## 6. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Terra Prime SSD 123 TB | $35,000–$45,000 |
| Strato V (theatre) | $10,000–$12,000 |
| Strato C units (×2 distributed zones) | $8,000–$12,000 |
| Installation and configuration | $5,000 |
| **Total** | **$58,000–$74,000** |

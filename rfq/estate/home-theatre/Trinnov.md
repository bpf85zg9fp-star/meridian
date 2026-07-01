---
document_id: "RFQ-1000-HT-002"
title: "Meridian Estate Home Theatre — Trinnov Audio Processing & Amplification"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / Home Theatre"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-HT-002 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-07-19 — Master RFQ Request (audio section)"
  - "2025-08-07 — Tier 5 audiophile system"
  - "2025-08-10 — Amplifier power and speaker compatibility"
  - "2025-09-12 — Home theater upgrades recommendations"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$110,000"
primary_supplier: "Trinnov AU distributor"
---

# RFQ-1000-HT-002 — Trinnov Audio Processing & Amplification

## Overview

Trinnov is the gold standard for residential cinema audio processing. The Altitude32 performs real-time 3D acoustics modelling and speaker calibration. Paired with the Amplitude16 for high-channel power amplification, it drives the full Pro Audio Technology speaker array.

---

## 1. Trinnov Altitude32 Processor

| Parameter | Specification |
|---|---|
| Model | Trinnov Altitude32 |
| Channels | 32 channels of audio processing |
| Function | 3D room correction, speaker calibration, Dolby Atmos/DTS:X decoding, bass management |
| Connectivity | Accepts HDMI, AES/EBU, analogue inputs from madVR / Kaleidescape chain |
| Calibration | Proprietary 3D microphone system; real-time acoustic correction per speaker position |
| Integration | KNX, RS-232, IP control for Josh.ai and Basalte scenes |

## 2. Trinnov Amplitude16

| Parameter | Specification |
|---|---|
| Model | Trinnov Amplitude16 |
| Channels | 16 channels |
| Power | High-output Class D; check with Trinnov for exact W/channel specification |
| Design | Rack-mounted; pairs natively with Altitude32 |

## 3. Signal Chain Position

```
Kaleidescape Strato V
        ↓ (4K HDR)
madVR Envy Extreme MK2  (HDR tone mapping)
        ↓ (audio extracted pre/post processing)
Trinnov Altitude32      (decode + 3D room correction)
        ↓
Trinnov Amplitude16     (amplification)
        +
Pro Audio Technology amps (supplementary amplification for subwoofer array)
        ↓
Pro Audio Technology speaker array
```

## 4. Speaker Compatibility

The Altitude32 calibrates directly to the Pro Audio Technology S-2215sm / SCRS-25ica / LFC-24sm array. All speaker positions, delays, and levels are programmed into Trinnov's 3D model. Trinnov calibration microphone measurement positions to be agreed with installer.

## 5. Integration

- **KNX/Josh.ai:** IP-controlled; power on/off and input selection tied to theatre scenes
- **Basalte Lena:** Scene recall for volume and input mode
- **Christie Eclipse:** Audio and video scenes coordinated via KNX scene logic

## 6. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Trinnov Altitude32 | $75,000 |
| Trinnov Amplitude16 | $35,000 |
| **Total** | **$110,000** |

---
document_id: "RFQ-1000-AV-002"
title: "Meridian Estate AV Distribution — Hi-Res Apple Music Pathway"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Estate / AV Distribution"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1000-AV-002 is provisional."
parent_rfq: "RFQ-1000"
reviewed_by: "Claude (L2A)"
source_batch: "000"
source_conversations:
  - "2025-08-07 — Tier 5 audiophile system"
  - "2025-08-10 — Amplifier power and speaker compatibility"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "$18,000–$28,000"
primary_supplier: "AV Integrator"
---

# RFQ-1000-AV-002 — Hi-Res Apple Music Pathway

## Overview

A dedicated signal chain enables bit-perfect 24-bit/192 kHz ALAC playback from Apple Music into the estate’s high-end audio system — bypassing Roon’s resampling for the purist listening zone.

---

## 1. Signal Chain

```
Apple Mac Mini M2 (fanless Akasa Turing FX chassis)
        ↓ (USB-C / USB 3.0)
Matrix Element X2 or Linn Selekt DSM (DAC)
        ↓ (XLR balanced analogue)
Naim CI-Uniti 102 line input (dedicated listening zone)
        ↓
Focal Utopia 1000 CI in-wall (stereo pair — dedicated hi-res zone)
```

## 2. Components

| Component | Purpose | Notes |
|---|---|---|
| Apple Mac Mini M2 | Apple Music ALAC playback source | Fanless Akasa Turing FX chassis — silent operation critical |
| Matrix Element X2 or Linn Selekt DSM | Reference DAC; USB input; XLR balanced output | Linn preferred for Naim synergy |
| IsoTek Aquarius or Torus Power isolation transformer | Clean power for audio chain | Dedicated audio circuit; balanced isolation |
| Naim CI-Uniti 102 | Line-in amplification for dedicated zone | Receives XLR balanced from DAC |

## 3. Josh.ai Scene

Scene: “Hi-Res Listening Session”
- Wakes Mac Mini via network magic packet
- Activates DAC via USB enumeration / relay
- Sets Naim CI-Uniti 102 to DAC input
- Dims lighting to warm 2,700 K
- Activates cedar diffuser
- Closes room shades

## 4. Why Separate from Roon

Roon can resample audio during DSP processing. For purist Apple Music hi-res playback at full 24-bit/192 kHz without any resampling, the dedicated Mac Mini → DAC → Naim chain bypasses Roon entirely. Both paths (Roon and direct) are available to Kevin.

## 5. Cost Estimate

| Item | Estimated Cost (AUD) |
|---|---|
| Apple Mac Mini M2 + Akasa Turing FX | $2,500 |
| Matrix Element X2 or Linn Selekt DSM DAC | $8,000–$15,000 |
| IsoTek / Torus Power isolation transformer | $3,500–$5,000 |
| XLR cabling + installation | $1,500 |
| Josh.ai scene programming | $1,500 |
| **Total** | **$17,000–$25,000** |

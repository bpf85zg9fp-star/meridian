---
document_id: "RFQ-1009-001"
title: "Meridian Vehicles — Project AURELION Bespoke Hybrid Grand Tourer"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Vehicles / Custom"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1009-001 is provisional."
parent_rfq: "RFQ-1009"
reviewed_by: "Claude (L2A)"
source_batch: "001"
source_conversations:
  - "2025-10-15 — Build a new car"
  - "2025-10-16 — Vehicle build recommendations"
  - "2025-10-20 — Apple CarPlay Ultra setup"
  - "2025-10-20 — Post car external view"
  - "2025-10-20 — CVT and 1000hp capability"
  - "2025-10-21 — Sunroof recommendations for car"
  - "2025-10-22 — Chassis recommendation for hybrid"
  - "2025-10-22 — Transparent AR HUD"
  - "2025-11-07 — Car design render request"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
---

# RFQ-1009-001 — Project AURELION: Bespoke Hybrid Grand Tourer

## Concept

A one-off, road-legal, ultra-luxury two-seat hybrid V12 grand tourer, ADR-compliant for South Australian registration. Philosophy: "everyday usability meets private-jet luxury and Koenigsegg-level engineering." Exterior direction settled as a Camaro × Bentley Continental hybrid aesthetic — muscular haunches, long bonnet, low roofline, right-hand drive.

**Target outputs:** 0–100 km/h <2.5s | Top speed 350+ km/h | EV-only range 80–100 km | Curb weight <1,700 kg

---

## 1. Concept & Design Team

| Role | Recommended |
|---|---|
| Lead design studio | CALLUM Designs (UK) — Ian Callum's studio |
| Aero & surfacing support | Italdesign — CFD optimisation, Class A surfacing |
| Design tools | Autodesk Alias, VRED; Varjo XR-4 VR full-scale review; Siemens Star-CCM+ CFD; Hexagon 3D scanning |

## 2. Engineering & Powertrain

| System | Specification |
|---|---|
| Engine | Handbuilt twin-turbo V12, hybrid-assisted |
| Electric system | Dual independent e-motors (front + rear), torque vectoring |
| Combined output | Target 1,000+ hp |
| Battery | Solid-state, 70 kWh, ~80–100 km EV range |
| Charging | 800V architecture; 350 kW DC fast-charge + 22 kW AC |
| Transmission | CVT-style seamless hybrid unit / 8-speed dual-clutch — shiftless transitions targeted |
| Drive | AWD with dynamic torque distribution; selectable RWD mode |

## 3. Chassis & Dynamics

- Carbon-titanium monocoque with integrated battery modules for low centre of gravity
- Active hydropneumatic suspension with AI-based predictive damping (forward radar + HD map data)
- Four-wheel steering with adaptive geometry
- Carbon-ceramic brakes, brake-by-wire with regenerative blending
- Adaptive exhaust valve system with electronically tunable resonance chamber (cabin acoustic balance)

## 4. Engineering Partners

| Partner | Role |
|---|---|
| Multimatic (UK/Canada) | Carbon monocoque, suspension, complete vehicle assembly |
| Cosworth (UK) | Hybrid V12 powertrain integration and calibration |
| Williams Advanced Engineering (UK) | Battery and thermal systems |

## 5. Autonomy & Driving Intelligence

- Target Level 4 autonomy (hands-off in defined zones) — noted as not currently ADR-approved at Level 4/5 in Australia; build to Level 2/3 functional spec with future-upgrade path
- Sensor suite: 6× HD LiDAR, 8× radar, 12× vision cameras, 4× ultrasonic arrays
- Transparent AR HUD integrated into windscreen for navigation and performance metrics

## 6. Apple CarPlay Ultra Integration — Hi-Res Audio Architecture

The car itself becomes the hi-res Apple Music playback device, not the iPhone:

| Stage | Function | Hardware |
|---|---|---|
| 1. Handshake | NFC + UWB authentication on MagSafe dock | Custom MagSafe pad |
| 2. Context transfer | Apple Music session state (song, timestamp) handed to car | CarPlay Extended architecture |
| 3. Stream redirection | Car's Apple-licensed compute fetches ALAC 24-bit/192kHz directly from Apple's CDN (not Bluetooth) | In-car Apple SoC (A16/A17-class) |
| 4. Output | Native hi-res PCM via internal USB-C/I²S to DAC cluster | Weiss/dCS/Trinnov chain |

**Dolby Atmos:** Supported via Apple-licensed Dolby decoder in the in-car compute module — discrete multi-channel PCM output (5.1.2/7.1.4), not downmixed stereo.

**MagSafe docks:** Primary at centre console (angled, sculptural); secondary in passenger compartment soft-close drawer; wireless charging pockets in door armrests for watch/AirPods.

## 7. Boutique Automotive Audio — Reference Build Spec

Design principle: car as playback device. CarPlay Extended supplies playback context; Apple-licensed compute fetches master files; lossless digital stream feeds studio-grade DAC cluster → boutique amplifiers → custom transducers.

| Subsystem | Vendor | Notes |
|---|---|---|
| Master clock | Mutec REF10 SE120 (adapted to 12V automotive rail) | Ultra-low jitter, critical for hi-res fidelity |
| DAC/converter cluster | Weiss Engineering DAC502 or dCS Lina | Studio-reference grade |
| DSP/spatial processing | Trinnov Audio or Helix DSP ULTRA | Room correction, time-alignment, Atmos spatial tuning |
| Amplification (automotive-native) | Mosconi Pro series (Gladen DSP Ultra) | Zero-Ohm architecture, 32-bit/384kHz DAC stages, -118dB noise floor |
| Amplification (voicing layer) | Naim Automotive / Burmester custom | Hybrid approach: Mosconi for power, Naim/Burmester for tonal voicing |
| Transducers | Accuton Automotive (ceramic/diamond) + Focal Utopia M | Reference imaging and clarity |

**Spec requirement:** PCM ≤24-bit/192kHz native support (stereo and multichannel); native Dolby TrueHD decoding with discrete 7.1.4 PCM output; minimum 12 discrete channels to DAC/DSP chain (14–16 recommended for headroom); time-alignment precision ≤0.5ms per channel; automotive ruggedisation −40°C to +85°C.

## 8. Local Integration Partner

United Auto Engineering (Adelaide) — ADR/SA compliance, prototyping, integration of heavy/thermal/EMC systems; coordinates with international vendors.

## 9. Sunroof & Glazing

Electrochromic smart glass sunroof specified (consistent with estate glazing standard — SageGlass/Halio family) for instant tint control without mechanical shading.

## 10. Outstanding RFQ Confirmations

- Final shipyard-equivalent build partner (coachbuilder) not yet confirmed — candidates discussed: Pininfarina, GFG Style, Touring Superleggera
- Exterior render finalisation pending (Camaro × Bentley Continental hybrid design, "Obsidian Graphite" colourway specified)
- Full ADR certification pathway and timeline not yet scoped

## 11. Pipeline Status

| Stage | Status |
|---|---|
| L1 (ChatGPT) | ⚠️ Not yet formatted as standalone artefact |
| L2A (Claude) | ✅ Extracted 2026-06-29 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 001, multiple conversations 2025-10-15 to 2025-11-07*

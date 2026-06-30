---
document_id: "RFQ-1010-002"
title: "Meridian Resort — Hotel App Cyber-Security Architecture"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Resort / Security"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1010-002 is provisional."
parent_rfq: "RFQ-1010"
reviewed_by: "Claude (L2A)"
source_batch: "001"
source_conversations:
  - "2025-10-31 — Hotel app security plan"
  - "2025-11-01 — Hotel payment options"
  - "2025-09-12 — Underage access prevention strategy"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
---

# RFQ-1010-002 — Hotel App Cyber-Security Architecture

## 1. Core Architecture — Zero-Trust Foundation

**Objective:** Assume breach, verify everything, trust nothing by default.

- NIST SP 800-207 aligned architecture — micro-segmented app layers (frontend, API, database, identity, analytics)
- Principle of least privilege across every service, employee, and subsystem
- Encrypted service mesh — mutual TLS (mTLS) between all internal microservices
- Runtime Application Self-Protection (RASP) integrated into backend code — detects/blocks SQLi, XSS, code injection in real time
- Cloud-native isolation — dedicated VPCs, private subnets, NACLs per environment (dev/staging/production)

## 2. Identity & Access Management

- FIDO2/WebAuthn MFA — hardware-based and biometric second factors (Face ID, Touch ID, YubiKey, passkeys)
- Passwordless login — guests authenticate via device-bound passkeys, eliminating credential theft risk
- Session binding — cryptographically bound to device fingerprint and IP reputation score
- Adaptive authentication — risk-based logic (suspicious device triggers biometric + SMS fallback)
- OAuth 2.1 / OpenID Connect for loyalty, POS, booking system integrations
- SAML 2.0 for staff systems — unified secure sign-on

## 3. Vendor-Agnostic Product Shortlist

| Category | Recommended Platforms |
|---|---|
| Identity & Authentication | Okta Workforce + Customer Identity Cloud, Ping Identity, Auth0 Enterprise, ForgeRock |
| Hardware Security Modules | Thales Luna, AWS CloudHSM, Entrust nShield |
| App & API Protection | Akamai App & API Protector, Cloudflare Enterprise WAF, Imperva API Security |
| Mobile App Security | Zimperium, NowSecure, Appdome (code obfuscation, runtime protection, SSL pinning) |
| Endpoint & Device Trust | CrowdStrike Falcon, SentinelOne Singularity, Microsoft Defender for Business Premium |
| SIEM / Security Ops | Splunk Enterprise Security, Google Chronicle, Exabeam Fusion, Elastic Security |
| Zero-Trust Network Access | Zscaler Private Access, Cloudflare Access, Tailscale, Perimeter 81 |
| Secrets Management | HashiCorp Vault, 1Password Business Secrets Automation |
| Compliance Automation | Drata, Vanta, Tugboat Logic (SOC 2 / ISO 27001 / GDPR) |

## 4. Total Integration Map

| Domain | Integrated Components | Security Layer |
|---|---|---|
| Hotel App (iOS/Android/Web) | Booking, mobile key, messaging, dining, loyalty, in-room control | FIDO2 identity, mTLS, API Gateway, WAF, app hardening |
| PMS | Central reservation, guest profiles, billing, housekeeping | AES-256 encrypted DB, IAM SSO, RASP, HSM-managed keys |
| POS & Retail | Restaurants, bar, bottleshop, spa, boutique | PCI DSS 4.0 tokenisation, dynamic CVV, fraud-scoring AI |
| Loyalty & Guest Identity | Profiles, preferences, rewards | OAuth 2.1, adaptive MFA, data minimisation, privacy dashboard |
| AI Concierge & Messaging | Natural-language concierge, staff comms | End-to-end encryption (Signal protocol), AI content moderation |
| Building Management/IoT | Lighting, HVAC, elevators, sensors, blinds | Isolated VLANs, NAC (Cisco ISE/Aruba ClearPass) |

## 5. Underage Access Prevention

Specific controls flagged for bar, bottleshop, and age-restricted facility access:

- Age verification at registration tied to government ID hash (same identity anchor system as guest barring — see RFQ-1010-001 §4)
- POS-level enforcement — age flag checked before any age-restricted sale completes
- Linked to room/group profile so minors in a family group cannot circumvent via shared room charge

## 6. Payment Security (Cross-Reference)

Payment-specific security (PCI DSS scope, tokenisation, multi-method fraud protection) detailed in RFQ-1010-001 §2–3. Full integration with Adyen/Stripe tokenisation confirmed compatible with this zero-trust framework.

## 7. Outstanding RFQ Confirmations

- Final identity platform (Okta vs Ping vs Auth0 vs ForgeRock) not locked — vendor-agnostic per source conversation, final selection via integrator RFP
- SIEM platform not finalised

## 8. Pipeline Status

| Stage | Status |
|---|---|
| L1 (ChatGPT) | ⚠️ Not yet formatted as standalone artefact |
| L2A (Claude) | ✅ Extracted 2026-06-29 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 001, "Hotel app security plan" (2025-10-31) and related*

---
document_id: "RFQ-1010-001"
title: "Meridian Resort — Hotel App Technology Stack & Architecture"
version: "0.1"
status: "Draft"
classification: "Ecosystem / Resort / Technology"
date: "2026-06-29"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID RFQ-1010-001 is provisional."
parent_rfq: "RFQ-1010"
reviewed_by: "Claude (L2A)"
source_batch: "001"
source_conversations:
  - "2025-11-02 — Hotel app software stack"
  - "2025-10-13 — Loaded vs Deputy comparison"
  - "2025-10-09 — Lightspeed p2p inquiry"
  - "2025-10-30 — Loyalty system recommendation"
  - "2025-10-30 — Hotel chat client recommendations"
  - "2025-11-14 — Linux recommendation for hotel"
kevin_authorisation: "Estate Principal authorised direct rfq/ posting bypassing drafts/ lifecycle (2026-06-28)"
estimated_cost_aud: "Initial: $650,000–$1,200,000 (Year 1) | Ongoing: $300,000–$500,000+ p.a."
---

# RFQ-1010-001 — Hotel App Technology Stack & Architecture

## Architecture Principles

API-first, microservices architecture. Cloud-native with infrastructure-as-code (Terraform). Event streaming (Kafka/cloud pub-sub) for near-real-time ops. OAuth2/OpenID Connect security by default, PCI DSS scope minimisation via tokenisation. Headless frontends — website, mobile app, and staff consoles consume the same APIs. Integration hub/middleware translates between PMS, channel managers, POS, locks, and device protocols.

---

## 1. Core Stack — Final Recommended Combination

| Category | Selected Vendor | Rationale |
|---|---|---|
| **PMS** | Oracle OPERA Cloud (enterprise) or Mews (boutique-fast-deploy alternative) | OPERA: enterprise-grade, deep integration with Lightspeed/NetSuite/Stripe/Crestron. Mews: open API marketplace, faster deployment |
| **Channel Manager / CRS** | SiteMinder | Market-leading; thousands of OTA/GDS integrations; real-time inventory |
| **Payments** | Stripe (primary) + Adyen (evaluated alternative) | Both support Amex, Diners, multi-currency, split-tender/composite transactions |
| **Crypto payments** | CoinGate (primary) or BitPay/NOWPayments | Native multi-coin support; auto-convert to AUD to remove volatility exposure |
| **Mobile Key / Room Access** | OpenKey | 50+ PMS integrations; proven BLE/NFC/Wallet SDK |
| **Guest App / In-Room Experience** | INTELITY | End-to-end guest experience platform purpose-built for luxury properties |
| **POS (F&B/Bottleshop/Retail)** | Lightspeed Restaurant (K-Series) or Oracle Simphony | Lightspeed: strong APAC presence, multi-outlet, good inventory. Simphony: deeper OPERA integration |
| **Guest CRM/CDP** | Salesforce Hospitality Cloud or Revinate | Unified guest profile across stays, preferences, spend |
| **Accounting/ERP** | NetSuite (Oracle) | Full ERP-grade, multi-entity, native OPERA/Lightspeed/Stripe integration; used by Marriott/Hyatt/Four Seasons at corporate level |
| **In-room automation** | Crestron | Unified control layer with mature hospitality APIs (vs KNX, which needs heavier middleware for app-level integration) — see §7 |

## 2. Payments — Multi-Method Architecture

Must support: Visa, Mastercard, American Express, Diners Club, UnionPay, JCB, Apple Pay, Google Pay, and cryptocurrency (BTC, ETH, minimum one stablecoin USDC/USDT) with optional auto-convert to AUD.

### Composite Tender / Split Settlement

A single folio transaction can be funded from multiple sources simultaneously (e.g. $300 room charge split: $150 Amex + $50 Diners + $100 crypto + $50 cash) — recorded as one unified transaction ID with sub-tenders. Adyen and Stripe both support split-tender APIs; partial authorisations per method; crypto via partner integration (Coinbase Commerce/BitPay).

### Group / Shared Tab Architecture

```
Group Account
 ├── Guest A (Bar tab)
 ├── Guest B (Restaurant meal)
 ├── Guest C (Spa treatment)
 └── Guest D (Room minibar + bottleshop preorder)
All linked to ONE unified payment token (e.g. corporate Amex, crypto wallet, or virtual card)
with ONE master pre-authorisation and real-time per-guest spend visibility.
```

PMS (OPERA/Mews) creates a shared group ledger; POS syncs every item in real time; app lets each guest view/contribute their share with split-by-item, split-by-ratio, or hybrid payment methods.

### Refund Architecture

Every purchase recorded as a master transaction with linked sub-payments (each with unique reference ID). Refunds route automatically to original payment source (card → card, crypto → wallet, cash → recorded on-property refund). Group accounts apply refunds proportionally to each guest's contribution, with host override option.

## 3. Pricing Matrix — Payment Processing (Indicative, AU Market)

| Item | Estimate |
|---|---|
| Card processing (Visa/Mastercard) | 0.75%–1.0% per transaction |
| Card processing (American Express) | ~1.0%–1.5% |
| Card processing (Diners Club) | Similar to Amex + 0.10–0.30% premium (negotiate) |
| Online/card-not-present | +0.1–0.5% above standard rate |
| Pre-auth/tokenisation infrastructure | $500–$2,000/month fixed service fee |
| Crypto gateway setup | $5,000–$20,000 + 0.5–1.5% per transaction |
| Hardware/terminals | $300–$1,000 per terminal |

## 4. Guest Restriction / Barring System

Centralised, multi-identifier guest control with real-time broadcast to all outlets:

**Identity anchors:** government ID/passport (hashed reference), phone/email (app login verification), payment method token (Stripe/CoinGate flagged), device fingerprint/app instance ID, loyalty/CRM ID.

**Workflow:** Staff flags guest in PMS with scope (bar/restaurant/bottleshop/spa/full property), duration (temporary/permanent), and reason. PMS pushes flag via webhook to all POS terminals, guest app, and Crestron room automation if access-related. POS checks flag on every transaction attempt before allowing sale.

**Granular per-guest enforcement within groups:** a single barred member's restriction does not affect other group members' shared tab — PMS isolates the barred profile at transaction level while keeping group folio fully functional for others.

**Automated notification:** push notification (primary channel, tied to verified profile) + email/SMS (formal record) + kiosk warning at check-in. Read-receipt tracking and policy acknowledgement available as compliance options.

## 5. Operations Software

### Staff Scheduling — Loaded vs Deputy

| Feature | Loaded | Deputy |
|---|---|---|
| Core purpose | Hospitality operations hub — rostering + inventory/goods/recipes/cost of goods + real-time financial visibility | Workforce/labour management — rostering, time/attendance, compliance, forecasting |
| Inventory/recipe management | ✅ Built-in | ✅ Not focused on this |
| Labour/roster strength | Part of broader suite | ✅ Very strong — scheduling, forecasting, shift swaps, leave management |

**Recommendation:** Loaded for kitchen/F&B cost-of-goods integration; Deputy if labour compliance/forecasting is the dominant need. Final selection depends on whether food-cost control or workforce compliance is the higher operational priority — flagged for Kevin's decision.

### POS Reference

Lightspeed evaluated for p2p (peer-to-peer/payment) capability — confirmed compatible with multi-outlet hospitality requirements.

## 6. Loyalty & Chat Systems

- **Loyalty:** to be integrated via Salesforce Hospitality Cloud or dedicated hospitality loyalty platform — specific vendor not yet finalised in source conversation
- **Guest chat client:** in-app messaging integrated into INTELITY guest experience platform; AI concierge layer for natural-language requests

## 7. In-Room Automation — Crestron vs KNX

| Aspect | Crestron | KNX |
|---|---|---|
| Architecture | Proprietary, centralised/hybrid processor-based | Open, decentralised fieldbus (ISO/IEC 14543) |
| Cloud support | Native (Crestron XiO Cloud) | Largely on-prem; needs third-party bridge |
| Hospitality integrations | Deep — Mews, OPERA, Infor PMS; OpenKey; Intelity/Control4 guest tablets | Fewer direct hospitality integrations; needs heavier middleware |
| App integration | Unified SDKs (SIMPL, Crestron Home, CH5/HTML5, REST, MQTT) | ETS configuration only; third-party gateways required |

**Decision:** Crestron selected for the hotel (guest-facing, app-unified requirement) — distinct from the Meridian Estate's KNX backbone (private residence, no guest-facing app requirement). This is an intentional architecture divergence between Estate (RFQ-1000) and Resort (RFQ-1001) domains, noted for governance awareness.

## 8. Server Infrastructure

Linux (distribution TBC — Ubuntu Server or RHEL evaluated) recommended as the hotel's backend server OS for cost, security patching cadence, and open-source middleware compatibility with the Kafka/microservices architecture.

## 9. Cost Estimate

| Cost Type | Estimate (AUD) | Notes |
|---|---|---|
| Initial licensing & setup (Year 1) | $650,000–$1,200,000 | PMS, POS, payments, CRM, IoT/Crestron, integrations, hardware, training |
| Ongoing annual (licences + support + transactions) | $300,000–$500,000+ p.a. | Subscription renewals, support, payment gateway fees, analytics, increments |

## 10. Synchronisation Architecture

Each platform is authoritative for one domain (PMS for guests, NetSuite for stock/finance, Lightspeed for POS activity), eliminating manual reconciliation:

| Layer | Sync Mechanism |
|---|---|
| PMS (master ledger) | All other systems reference via API |
| POS ↔ PMS | Two-way certified interface, real-time |
| Payments | Unified tokens, nightly automated reconciliation |
| Inventory (POS ↔ NetSuite) | Shared product catalogue, live stock sync |
| CRM | Webhook-based, only fires after PMS confirms transaction/stay (prevents ghost entries) |

## 11. Outstanding RFQ Confirmations

- Final PMS decision (OPERA Cloud vs Mews) not locked — trade-off is enterprise scale vs deployment speed
- Final payments processor (Stripe vs Adyen) not locked
- Loaded vs Deputy decision pending Kevin's operational priority
- Linux distribution not finalised

## 12. Pipeline Status

| Stage | Status |
|---|---|
| L1 (ChatGPT) | ⚠️ Not yet formatted as standalone artefact |
| L2A (Claude) | ✅ Extracted 2026-06-29 |
| L2B / L3 / Kevin | ❌ Not yet |

*Extracted by Claude (L2A) — 2026-06-29 | Source: Batch 001, multiple conversations 2025-10-09 to 2025-11-14*

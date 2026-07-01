---
document_id: "INGEST-STD-001"
title: "Meridian Knowledge Base — Conversation Export Ingestion Standard"
version: "1.1"
status: "Draft"
classification: "Infrastructure / Standards"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID INGEST-STD-001 is provisional pending formal standards namespace ratification in A1 schema."
---

# INGEST-STD-001 — Conversation Export Ingestion Standard

## Amendment History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-06-28 | Claude (L2A) | Initial standard |
| 1.1 | 2026-06-28 | Claude (L2A) | Pipeline architecture updated per Kevin instruction: Grok parallel ingestion; Copilot/Codex review layer; direct rfq/ posting authorised |

---

## 1. Purpose

This standard governs the ingestion of ChatGPT conversation export files into the Meridian Knowledge Base and the extraction and formatting of programme artefacts from those exports into the `rfq/` directory tree.

---

## 2. Pipeline Architecture (v1.1)

```
ChatGPT conversation exports (40 files)
        ↓ treated as L1 raw drafts
        ↓
┌────────────────────────┐
│ Claude (L2A) + Grok   │  ←─ parallel review + amend
└────────────────────────┘
        ↓ valid A1-compliant documents
        ↓
  rfq/<domain>/<subdomain>/
        ↓
 GitHub Copilot + Codex  ←─ when configured
        ↓
     Grok (L3)           ←─ consolidation + adjudication
        ↓
     Kevin               ←─ final approval
```

**Kevin-authorised deviation from RFQ-0100:** Validated documents are posted directly to `rfq/` subdirectories (not routed through `drafts/` lifecycle). Reason: ChatGPT conversation exports are treated as L1 raw drafts; Claude and Grok perform the review-and-amend function that normally separates L1 from rfq/ promotion. All documents must carry a `kevin_authorisation` field in frontmatter.

---

## 3. Scope

Applies to all 40 ChatGPT JSON conversation export files provided by the Estate Principal (Batches 000–039). Applies to all ingesting agents: Claude (L2A), Grok, GitHub Copilot, GitHub Codex.

---

## 4. Ingesting Agents

| Agent | Role |
|---|---|
| Claude (L2A) | Independent reviewer — review, amend, and post to rfq/ |
| Grok | Parallel ingestion — same scope as Claude; also consolidation/adjudication (L3) |
| GitHub Copilot | Code and document review when connected |
| GitHub Codex | Extended code/document review when connected |
| Kevin | Estate Principal — sole final approval authority |

**Coordination rule:** Claude and Grok should not duplicate documents. Before creating a document, agents should check the `rfq/` tree for an existing file on the same topic. If a file exists, create a `REV-L2A-` or `REV-L3-` review artefact rather than a duplicate document.

---

## 5. rfq/ Directory Structure

All extracted documents go to `rfq/` subdirectories reflecting domain and topic:

```
rfq/
  estate/
    home-theatre/          # Theatre projector, audio, processing, seating, screens
    smart-home/            # KNX, Josh.ai, Basalte, mmWave, Lutron
    av-distribution/       # Whole-home audio and video (Focal, Naim CI, displays)
    kitchen/               # Appliances, tapware, butler's pantry, bar, wine
    bathrooms/             # Tapware, toilets, wellness, body dryers
    bedrooms/              # Beds, dressing suites, linen
    living/                # Lounge, games, office, additional rooms
    structure/             # Cladding, glazing, roofing, bushfire protection
    hvac/                  # Hydronic, HVAC, ventilation, air quality
    garage/                # Structure, doors, EV charging, car wash
    outdoor/               # Pool, pavilion, outdoor kitchen, landscape
    security/              # Access control, surveillance, safe room
    energy/                # Solar, battery, hydrogen, smart energy
    network/               # Connectivity, infrastructure, NAS
    wellness/              # Dedicated wellness suite, sauna, cold plunge
  resort/
    hotel/                 # Obsidian Hotel concept
    bar/                   # Hotel bar
    hospitality/           # Hotel operations, storage, tech
  vehicles/
    bentley/               # Continental GT, Bentayga
    motorcycles/           # Triumph Rocket 3, Harley
    ev/                    # EV fleet selection
  lifestyle/
    fashion/               # Wardrobe, clothing, accessories
    memberships/           # Australia-wide memberships
    recreation/            # Camping, leisure, music
    dining/                # Restaurants, food
  health-family/
    nutrition/             # Meal planning, supplements, family health
    wellness/              # Personal wellness
  financial/
    investment/            # Investment strategy
  land/
    site-selection/        # Forest Range lot, land search
```

---

## 6. Knowledge Base Directory (Raw Intake)

The `knowledge/` directory remains the raw intake and archive layer. It does NOT contain governance artefacts. See `knowledge/README.md`.

---

## 7. Conversation Classification

Every conversation in a batch must be classified to a domain and subdomain per the `rfq/` tree above. See `knowledge/raw-exports/chatgpt/export-2026-06-27/BATCH-000-STATUS.md` for Batch 000 classifications.

---

## 8. Document Standards

Every document posted to `rfq/` must:

1. Have A1-compliant YAML frontmatter (all required fields present)
2. Carry `status: "Draft"` unless Kevin has approved
3. Include `kevin_authorisation` field confirming Estate Principal authorised direct rfq/ posting
4. Include `source_batch` and `source_conversations` fields
5. Include `reviewed_by` field naming the ingesting agent
6. Be in Australian English
7. Reference the source conversation content accurately
8. Not include personally identifiable information that Kevin has not approved for repository storage

---

## 9. Document ID Convention for Sub-Domain Documents

The A1 schema pattern `^(RFQ|RIP|...)-\d{4}$` does not accommodate sub-document IDs. Pending A1 schema extension, use the following provisional convention:

- Sub-domain documents within `rfq/estate/home-theatre/` etc. carry a `document_id` in the format `RFQ-1000-[DOMAIN-CODE]-[SEQ]`, e.g. `RFQ-1000-HT-001`
- These are explicitly flagged as provisional in the `note` frontmatter field
- All IDs must be registered in `knowledge/INGESTION-MANIFEST.md` (§ RFQ-1000+ Register)

---

## 10. Workflow Per Batch

1. Agent receives export file
2. Check `knowledge/INGESTION-MANIFEST.md` for batch number and existing extractions
3. Create/update `knowledge/raw-exports/chatgpt/export-<date>/BATCH-NNN-STATUS.md`
4. Classify all conversations per §7
5. Check `rfq/` tree for existing documents on same topics before creating new ones
6. Extract, review, and amend content into A1-compliant documents
7. Commit to `draft/chatgpt-ingest-<date>` branch (or agent's own ingest branch)
8. Update `INGESTION-MANIFEST.md` § RFQ-1000+ Register with any new document IDs

---

## 11. Rules for All Agents

**Do:**
- Check for existing rfq/ documents before creating new ones
- Use A1-compliant frontmatter with all required fields
- Include `kevin_authorisation` field on every document
- Register all document IDs in INGESTION-MANIFEST
- Flag provisional document IDs with `note` field
- Coordinate with other agents via INGESTION-MANIFEST

**Do not:**
- Duplicate an existing rfq/ document
- Post raw conversation content without review and amendment
- Invent specifications not present in the source conversations
- Include personal health, family, or financial information Kevin has not approved
- Commit directly to `main` without Kevin review

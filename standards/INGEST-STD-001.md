---
document_id: "INGEST-STD-001"
title: "Meridian Knowledge Base — Conversation Export Ingestion Standard"
version: "1.0"
status: "Draft"
classification: "Infrastructure / Standards"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
note: "Document ID INGEST-STD-001 is provisional pending formal standards namespace ratification in A1 schema."
---

# INGEST-STD-001 — Conversation Export Ingestion Standard

## 1. Purpose

This standard governs the ingestion of ChatGPT conversation export JSON files into the Meridian Knowledge Base and the extraction of A1-compliant governance artefacts from those exports into the formal programme pipeline.

---

## 2. Scope

Applies to all ChatGPT JSON conversation export files provided by the Estate Principal. Currently 40 files are expected (batches 000–039). This standard applies to all pipeline agents (L1 ChatGPT, L2A Claude, L2B Gemini, L3 Grok) performing ingestion or extraction work.

---

## 3. Directory Structure

The `knowledge/` directory is the authoritative intake and archive layer. It sits outside the governance artefact namespaces (`rfq/`, `rip/`, `drafts/`, `reviews/`).

```
knowledge/
  README.md
  INGESTION-MANIFEST.md                          ← Master tracker for all 40 batches
  raw-exports/
    chatgpt/
      export-<YYYY-MM-DD>/
        BATCH-NNN-STATUS.md                      ← Required for every batch
        [conversations-NNN.json]                 ← Optional — see §5
```

Extracted artefacts are placed in:
```
drafts/<document_id>/<document_id>.md            ← Per RFQ-0100 §6
```
On branches named `draft/<document_id>`.

---

## 4. Batch Numbering

Each conversation export file is assigned a three-digit batch number matching its filename suffix:
- `conversations-000.json` → Batch 000
- `conversations-001.json` → Batch 001
- (etc.)

Batch numbers are tracked in `knowledge/INGESTION-MANIFEST.md`.

---

## 5. Raw Export Handling

Raw JSON exports **should not** be committed to the repository by default because:
- Files are typically 20–50 MB (exceeds standard GitHub API limits)
- Files contain personal, health, and family content not appropriate for repository storage

A `BATCH-NNN-STATUS.md` file **must** be committed for every batch regardless of whether the raw JSON is committed. If raw JSON commitment is required for audit purposes, use Git LFS.

---

## 6. Conversation Classification

Every conversation in a batch must be assigned to one of the following domains:

| Domain | Description | RFQ-1000+ target range |
|---|---|---|
| Estate | Smart home, fit-out, fixtures, outdoor, security, technology systems | RFQ-1000 (sub-RFQs as needed) |
| Resort / Hospitality | Hotel, bar, guest experience, accommodation | RFQ-1001 |
| Aviation | Airfield, aircraft operations | TBD |
| Marina | Watercraft, marina facilities | TBD |
| Village | Infrastructure, logistics | TBD |
| Farm / Agricultural | Farming operations, land management | TBD |
| Vehicles | Fleet, upgrades, audio, modifications | RFQ-1002 |
| Lifestyle | Fashion, memberships, accessories, food, recreation, arts | RFQ-1003 |
| Personal / Health / Family | Wellness, children, family, nutrition | RFQ-1005 |
| Financial | Investment strategy, asset allocation, wealth management | RFQ-1004 |
| Generational Governance | Family office, succession, trust, estate planning | TBD |
| Estate — Land | Site search, lot evaluation, location strategy | RFQ-1006 |
| Pre-Meridian / Irrelevant | Content predating programme or entirely off-topic | No extraction — archive note only |

---

## 7. Document ID Assignment (RFQ-1000+ Range)

All ecosystem artefacts extracted from the knowledge base use the **RFQ-1000+** range:

| Range | Scope |
|---|---|
| RFQ-0001 – RFQ-0999 | Meridian governance and infrastructure |
| **RFQ-1000+** | **Meridian ecosystem — all programme domain artefacts** |

**Reserved IDs (do not reassign):**
- RFQ-1000 — Meridian Estate, Master Smart Home Specification
- RFQ-1001 — Meridian Resort, Obsidian Hotel Concept
- RFQ-1002 — Meridian Vehicles, Fleet Specification
- RFQ-1003 — Meridian Lifestyle
- RFQ-1004 — Meridian Financial
- RFQ-1005 — Meridian Personal / Health / Family
- RFQ-1006 — Meridian Estate, Land Search and Site Selection

All other IDs from RFQ-1007 upward are assigned sequentially as extraction proceeds. New assignments are registered in `knowledge/INGESTION-MANIFEST.md` (§ RFQ-1000+ Register) before extraction begins.

---

## 8. Extraction Requirements

Extracted artefacts must:
1. Have valid A1-compliant YAML frontmatter per `schemas/meridian-a1-markdown-artefact-standard.yaml v1.1`
2. Carry `status: "Draft"`
3. Include a `source` frontmatter field referencing source batch(es) and conversation titles
4. Carry `programme: "Meridian"`
5. Be committed to `drafts/<document_id>/<document_id>.md`
6. Be registered in `knowledge/INGESTION-MANIFEST.md`
7. Be committed on a branch named `draft/<document_id>`

Extracted artefacts must **not** be committed directly to `rfq/`, `rip/`, or any other promoted namespace. They must enter the `drafts/` lifecycle and proceed through the L1→L2A→L2B→L3→Kevin pipeline.

---

## 9. Ingestion Workflow

### For each new batch file received:

1. Identify batch number from filename
2. Create `knowledge/raw-exports/chatgpt/export-<date>/BATCH-NNN-STATUS.md`
3. Count all conversations; record in BATCH-STATUS
4. Classify every conversation per §6 table
5. Update `knowledge/INGESTION-MANIFEST.md` batch row
6. Identify any new RFQ IDs required; register in INGESTION-MANIFEST § RFQ-1000+ Register
7. Extract highest-priority artefacts (⭐ Critical first)
8. Commit BATCH-STATUS and INGESTION-MANIFEST updates to `draft/chatgpt-ingest-<date>` branch
9. Commit each extracted artefact to its own `draft/<document_id>` branch

### Priority order for extraction:

1. Documents already referenced by ID in other governance artefacts
2. ⭐ Critical priority conversations (master/consolidated RFQs)
3. High priority by domain, in the order: Estate → Resort → Vehicles → Financial → Lifestyle → Health → Other

---

## 10. Rules for All Agents

**Do:**
- Follow this standard in full before committing anything to the repository
- Check `INGESTION-MANIFEST.md` before assigning new RFQ-1000+ IDs
- Create BATCH-STATUS files for every batch received
- Use A1-compliant frontmatter on every extracted document
- Commit extracted artefacts on separate `draft/<document_id>` branches

**Do not:**
- Invent document IDs not registered in INGESTION-MANIFEST
- Use non-numeric or descriptive document ID segments (e.g. `RFQ-ESTATE-KITCHEN` is invalid)
- Create files in `rfq/` directly from ingested content
- Create non-standard directories outside the defined structure
- Commit raw JSON exports without Estate Principal authorisation
- Reference standards that do not exist
- Create stub files without frontmatter and register them as completed artefacts

---

## 11. Amendment History

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-06-28 | Claude (L2A) | Initial standard — replaces non-compliant STD-CHAT-INGEST-0001 stub |

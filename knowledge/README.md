---
document_id: "KNOWLEDGE-README-001"
title: "Meridian Knowledge Base — Directory Guide"
version: "1.0"
status: "Active"
classification: "Infrastructure / Knowledge Management"
date: "2026-06-28"
programme: "Meridian"
author: "Claude (L2A Independent Reviewer)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
---

# Meridian Knowledge Base

The `/knowledge/` directory is the designated repository for raw source materials from which Meridian governance artefacts and programme intelligence are derived. It is **not** a governance namespace — it is a controlled intake and archive layer that feeds the formal artefact pipeline.

---

## Directory Structure

```
knowledge/
  README.md                                      # This file
  INGESTION-MANIFEST.md                          # Master tracker — all 40 batches
  raw-exports/
    chatgpt/
      export-<YYYY-MM-DD>/
        BATCH-NNN-STATUS.md                      # Per-batch inventory and status
        [conversations-NNN.json]                 # Raw JSON (see INGEST-STD-001 §5)
```

---

## Scope

The knowledge base covers **all Meridian programme domains**:

| Domain | Examples |
|---|---|
| Estate | Smart home, fit-out, fixtures, outdoor, technology systems |
| Resort / Hospitality | Hotel concept, bar, guest experience |
| Aviation | Airfield, aircraft |
| Marina | Watercraft, marina facilities |
| Village | Logistics, infrastructure |
| Farm / Agricultural | Farming operations |
| Vehicles | Fleet, upgrades, modifications |
| Lifestyle | Fashion, memberships, accessories, food, recreation |
| Personal / Health / Family | Wellness, family planning, health |
| Financial | Investment strategy, asset allocation |
| Generational Governance | Family office, succession, trust structures |

---

## Ingestion Standard

All ingestion work must follow **`standards/INGEST-STD-001.md`**.

What an ingesting agent should do when it receives a new file:
1. Open `knowledge/INGESTION-MANIFEST.md` and confirm the batch number
2. Create `knowledge/raw-exports/chatgpt/export-<date>/BATCH-NNN-STATUS.md`
3. Classify all conversations per INGEST-STD-001 §6
4. Update INGESTION-MANIFEST with batch summary
5. Extract priority artefacts per §8 and §9

---

## Document ID Ranges

| Range | Scope |
|---|---|
| RFQ-0001 – RFQ-0999 | Meridian governance and infrastructure RFQs |
| **RFQ-1000+** | **Meridian ecosystem RFQs** — all programme domain artefacts extracted from the knowledge base |

ID assignment for RFQ-1000+ is tracked in `INGESTION-MANIFEST.md` (§ RFQ-1000+ Register).

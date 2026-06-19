---
document_id: "REPO-CANONICAL-MAP-001"
title: "Meridian Repository Canonical Map & Authority Graph"
version: "1.0"
status: "draft"
date: "2026-06-19"
programme: "Meridian"
author: "ChatGPT (Layer 1 Governance Drafting Role)"
review_stage: "Layer 1 draft"
yaml_schema: "Meridian A1 Markdown Artefact Standard"
tags:
  - "repository"
  - "governance"
  - "canonical-map"
  - "architecture"
---

# Meridian Repository Canonical Map & Authority Graph

## 1. Purpose
This document defines the canonical structural map, authority precedence model, and dependency relationships for the Meridian repository. It establishes a single interpretive framework for resolving ambiguity across RFQ, RIP, Continuum, and supporting layers.

---

## 2. Repository Inventory (Observed State)
Based on verified repository state and governance documentation:

### 2.1 Top-Level Domains
- `/rfq/` — Requirements and Framework Standards (multi-domain)
- `/rip/` — Protocols and process interchange standards
- `/repo/` — Repository implementation artefacts and system-level definitions
- `/reviews/` — Multi-layer review artefacts
- `/continuum/` — Automation and orchestration layer
- `/schemas/` — YAML/frontmatter and validation schemas
- `/templates/` — Approved document templates
- `/archive/` — Deprecated or superseded artefacts
- `/.github/` — CI/CD, workflows, and GitHub-native automation

### 2.2 RFQ Domain Structure
- estate
- farm
- village
- resort
- marina
- aviation

---

## 3. Authority Precedence Model (Critical Rule Set)

Authority is strictly hierarchical to prevent semantic conflict:

### Level 0 — Repository Control Plane
- `.github/` workflows
- CI validation gates

### Level 1 — Canonical Standards
- `/schemas/`
- `/templates/`

### Level 2 — Governance Definition Layer
- `/rip/` (process rules, execution pipelines)
- `/repo/` (system definition rules)

### Level 3 — Requirements Layer
- `/rfq/` (domain requirements)

### Level 4 — Execution Layer
- `/continuum/` (automation runtime behaviour)

### Rule
Lower levels MUST NOT override higher levels under any condition.

---

## 4. Dependency Graph (Logical Model)

```
schemas ─┐
         ├──> rfq ─────┐
templates┘              │
                        ├──> rip ────┐
                        │            │
                        ├──> repo ───┼──> continuum
                        │            │
.github (control) ──────┘            │
                                     ▼
                                 execution
```

---

## 5. Redundancy & Drift Analysis

### 5.1 Observed Overlaps
- RFQ and RIP both influence process semantics
- Continuum currently spans multiple architectural responsibilities

### 5.2 Risk Classification
- HIGH: ambiguous authority between RFQ and RIP
- MEDIUM: Continuum structural overloading
- LOW: template/schema coupling ambiguity

### 5.3 Required Correction Principle
Each governance concept must have exactly one authoritative home directory.

---

## 6. Canonical Routing Rules

All system interpretation MUST follow this resolution order:

1. `.github/` execution constraints
2. `/schemas/` validation constraints
3. `/rip/` process logic
4. `/repo/` system definitions
5. `/rfq/` requirements interpretation
6. `/continuum/` runtime execution

If conflicts occur, higher precedence overrides lower precedence.

---

## 7. Registry Index (Canonical Contract)

### 7.1 RFQ Registry
- RFQ-0100 (Repository Bootstrap Standard)
- RFQ-0000 (Master Charter)

### 7.2 RIP Registry
- RIP-003A (Review Grid Pipeline Standard)

### 7.3 Continuum Registry
- Continuum core (unsegmented — requires modular decomposition)

---

## 8. System Observations

### 8.1 Strengths
- Clear domain segmentation in RFQ layer
- Early-stage governance standardisation present
- Multi-layer review architecture defined

### 8.2 Structural Gaps
- No explicit dependency enforcement engine
- No canonical index of all artefacts
- Continuum layer is under-specified as a monolithic construct

---

## 9. Conclusion
The repository is structurally coherent but requires strict enforcement of authority hierarchy and decomposition of Continuum into bounded execution modules to eliminate semantic overlap.

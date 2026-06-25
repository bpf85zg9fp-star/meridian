# CLAUDE-COR-001 — Claude Core Review Standard (L2A Governance Layer)

## 1. Purpose

This specification defines the deterministic pattern-matching and evaluation rules governing Claude’s Level-2-to-Action (L2A) review behaviour within the Meridian governance system.

Without this layer, review outcomes become non-deterministic, inconsistently classified, and non-auditable. This document enforces structured evaluation across:

- A1 frontmatter validation
- Finding identification heuristics
- Severity classification logic
- Disposition triggers (pass / revise / block / escalate)

---

## 2. Scope

Applies to all:

- Markdown governance documents (RFQ, RIP, COR, SPEC classes)
- Machine-enforced schema layers
- Repository ingestion and validation pipelines
- Cross-model review flows (Claude, GPT, Gemini, Grok)

Excludes:

- Free-form conversational output
- Non-persisted ephemeral drafts not entering repository state

---

## 3. A1 Frontmatter Validation Patterns

All governed documents MUST contain A1-compliant frontmatter.

### 3.1 Required Fields

- doc_id
- title
- version
- status
- author
- generated_by
- type
- classification
- parent_documents

### 3.2 Validation Rules

- Missing required fields → FAIL
- Invalid schema → FAIL
- Broken references → FAIL

---

## 4. Finding Identification Heuristics

Findings are generated for structural, semantic, and systemic anomalies including schema breaks, contradictions, and unresolved dependencies.

---

## 5. Severity Classification

S0–S3 scale applied deterministically based on impact radius and structural integrity risk.

---

## 6. Disposition Model

- PASS
- REVISE
- BLOCK
- ESCALATE

---

## 7. L2A Review Model

Deterministic pipeline enforcing reproducible evaluation outcomes.

---

## 8. Auditability

All decisions must be traceable to rule-level triggers.

---

## 9. Summary

Defines stable governance layer for L2A review consistency.

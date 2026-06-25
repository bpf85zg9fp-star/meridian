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

```yaml
doc_id: string
    # Unique identifier, immutable once issued
title: string
    # Human-readable canonical name
version: string
    # Semver or monotonic revision
status: draft|active|deprecated|superseded
author: string
generated_by: string
    # System or agent provenance
type: string
    # schema category (rfq, rip, cor, spec, etc.)
classification: string
    # system-core | system-edge | user-space | external
parent_documents: list[string]
```

### 3.2 Validation Rules

A document FAILS A1 validation if:

- Any required field is missing
- `doc_id` is non-unique within repository scope
- `version` decreases relative to existing canonical version
- `status` is outside enumerated set
- `parent_documents` references non-existent or unresolved nodes

### 3.3 Structural Integrity Checks

- YAML must be parseable (strict mode)
- No duplicate keys
- No inline unescaped special characters in identifiers
- UTF-8 encoding enforced

---

## 4. Finding Identification Heuristics

A “finding” is any detected deviation, risk, inconsistency, or structural anomaly.

### 4.1 Detection Triggers

A finding is generated when any of the following are observed:

#### Structural Triggers
- Missing or malformed A1 frontmatter
- Broken schema alignment (JSON/YAML mismatch)
- Undefined cross-reference target

#### Semantic Triggers
- Conflicting version statements across linked docs
- Contradictory requirements within same domain block
- Ambiguous constraint definitions (“best”, “optimal”, “future-proof” without bounds)

#### Systemic Triggers
- Circular dependency in `parent_documents`
- Unresolved external references (e.g. connectors, APIs, repos)
- Cross-model disagreement without reconciliation layer

---

## 5. Severity Classification Rules

Findings MUST be assigned one of four severity levels.

| Level | Label   | Definition |
|------|--------|------------|
| S0   | Informational | No functional impact, observational only |
| S1   | Minor | Local inconsistency, no downstream breakage |
| S2   | Major | Structural or schema violation affecting validity |
| S3   | Critical | Systemic failure risk, prevents correct interpretation or execution |

### 5.2 Escalation Heuristics

- Multiple S1 findings in same subsystem → promote to S2
- Any A1 failure → minimum S2
- Any circular dependency → S3
- Any unresolved schema dependency → S3

---

## 6. Disposition Triggers

Allowed dispositions:
- PASS
- REVISE
- BLOCK
- ESCALATE

### Logic
- PASS: zero S2/S3, all checks pass
- REVISE: only S1 issues
- BLOCK: any S3 or invalid schema
- ESCALATE: cross-model conflict or unresolved external dependency

---

## 7. L2A Review Behaviour Model

1. Parse document
2. Validate A1
3. Extract structure
4. Apply heuristics
5. Assign severity
6. Aggregate
7. Determine disposition

Constraints:
- deterministic evaluation only
- no suppression of S3 findings
- reproducibility required

---

## 8. Auditability Requirements

- deterministic finding IDs
- rule provenance trace
- severity justification
- final disposition log

---

## 9. Version Control Behaviour

- major changes require new CLAUDE-COR-xxx ID
- no backward compatibility guarantee
- deprecation must be explicit

---

## 10. Summary

Defines deterministic L2A governance layer for consistent review behaviour across Meridian system.

# DRAFTS INDEX — Meridian Governance Registry

## Branch
`draft/tool-audit-20260623`

## Purpose
This file provides the authoritative registry of all in-flight A1 artefacts within the `/drafts/` namespace.
It functions as the state layer between specification (RFQ/RIP) and review promotion (`/reviews/`).

---

## Draft Lifecycle States

| State | Description |
|------|------------|
| scaffold | Initial creation, not validated |
| active | Under development on working branch |
| staged | Passed schema validation, ready for review promotion |
| blocked | Fails validation or dependency checks |
| promoted | Merged into `/reviews/` pipeline |

---

## Active Drafts

| Document ID | Path | Type | State | Dependency |
|------------|------|------|-------|------------|
| TOOL-AUDIT-001 | drafts/TOOL-AUDIT-001.md | structural audit | active | RFQ-0100 |

---

## Governance Rules

1. All new artefacts MUST be registered here before promotion eligibility.
2. No draft may bypass schema validation (`A1 schema`).
3. RFQ-linked artifacts require explicit dependency mapping.
4. No direct promotion to `/reviews/` without CI verification gate.

---

## System Interpretation Layer

This registry acts as:
- A deterministic state machine input for CI
- A dependency resolution anchor for RFQ → RIP → Schema chain
- A staging boundary enforcing controlled artefact evolution

---

## Notes
This index is machine-readable and intended for enforcement tooling, not human documentation alone.

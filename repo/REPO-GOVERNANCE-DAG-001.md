# REPO-GOVERNANCE-DAG-001 — Governance Dependency Graph

## Branch
`draft/tool-audit-20260623`

---

## Abstract
This document defines the machine-enforceable governance DAG for the Meridian repository.
It formalises relationships between RFQ specifications, RIP extensions, schema contracts, and CI enforcement.

---

## Core DAG Layers

### L0 — Specification Layer
- RFQ-0100.md (system baseline requirements)

### L1 — Protocol Extension Layer
- RIP-003A
- RIP-003C

### L2 — Schema Contract Layer
- meridian-a1-markdown-artefact-standard.yaml

### L3 — Artifact Layer
- /drafts/* (in-flight A1 artefacts)

### L4 — Review Layer
- /reviews/* (final validation gate, external to current draft permissions)

### L5 — CI Enforcement Layer
- scripts/validate_contract.py
- .github/workflows/governance-compiler.yml

---

## Directed Edges (Hard Constraints)

1. RFQ-0100 → RIP-* (extension dependency)
2. RIP-* → Schema (A1 compliance required)
3. Schema → Drafts (all artifacts MUST validate against schema before entry)
4. Drafts → CI (mandatory validation gate)
5. CI → Reviews (promotion only on full pass)

---

## State Transition Rules

| Transition | Condition |
|------------|----------|
| RFQ → RIP | requirement decomposition approved |
| RIP → Schema | contract definition finalized |
| Schema → Draft | schema validation passes |
| Draft → CI | artifact complete + indexed in /drafts |
| CI → Review | all checks pass + DAG integrity confirmed |

---

## Enforcement Semantics

- The DAG is **acyclic by design**.
- Any detected cycle invalidates repository state.
- All transitions are event-sourced via CI pipeline logs.

---

## Future Extensions

Planned additions:
- Automated DAG validator module in `/scripts/`
- Event-sourced state ledger (append-only)
- Graph visualization exporter for CI dashboards

---

## Notes
This file is intended to become the canonical enforcement definition for governance execution tooling.

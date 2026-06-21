# Meridian Expanded Governance Changelog

This document supplements `CHANGELOG.md` and provides a full, structured record of recent architectural changes introduced to the Meridian governance system.

It is intended for later consolidation into the canonical changelog.

---

## 1. Event-Sourced Governance Introduction

### Added
- **RIP-003B — Governance Event Sourcing & State Machine Layer**
  - Introduced immutable event log model
  - Defined canonical state machine transitions
  - Enabled deterministic replay of governance decisions
  - Introduced RTM linkage constraints (Requirement → Event → Decision)

---

## 2. Enforcement Layer Implementation

### Added
- GitHub Actions CI pipelines:
  - `.github/workflows/meridian-ci.yml`
  - `.github/workflows/meridian-ci-enforcement.yml`

### Features introduced:
- Blocking enforcement mode for governance validation
- RFQ ↔ RIP contract validation gate
- Schema enforcement gate (frontmatter validation)
- RTM graph engine execution during CI

---

## 3. Validation Subsystems

### Added scripts:

#### RFQ → RIP Contract Validator
- `scripts/validate_contract.py`
- Ensures:
  - RFQ-0100 presence
  - RIP-003A / RIP-003B presence
  - Cross-document consistency

#### Schema Enforcement Gate
- `scripts/validate_schemas.py`
- Enforces:
  - Required frontmatter fields
  - Structural markdown compliance

#### RTM Graph Engine
- `scripts/rtm_graph.py`
- Builds:
  - Requirement nodes
  - Event nodes
  - Directed traceability edges
- Outputs:
  - `rtm_graph.json`

---

## 4. System Architecture Transition

### Phase progression:

1. Documentation System
   - RFQ + RIP as static definitions

2. Structured Governance System
   - RIP-003A workflow orchestration

3. Event-Sourced Governance System
   - RIP-003B introduces deterministic event model

4. Enforcement-Grade Governance System (CURRENT)
   - CI validation gates
   - RTM graph enforcement
   - Blocking pipeline execution

---

## 5. Current Known Gaps

- RTM graph remains heuristic (text-based extraction)
- No persistent external event store backend
- Schema validation limited to metadata fields
- No cryptographic audit sealing
- No formal compliance scoring engine

---

## 6. Pending Consolidation Requirement

This document should be merged into:
- `CHANGELOG.md`

Once update permissions are available, this expanded log should replace or be merged into the canonical changelog.

---

End of expanded changelog

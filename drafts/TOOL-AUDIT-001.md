# TOOL-AUDIT-001 — Repository Structure Audit

## Branch
draft/tool-audit-20260623

## Scope
Initial structural reconnaissance of Meridian repository for pipeline alignment, governance conformance, and A1 schema readiness.

## Observed Top-Level Structure
Based on repository inspection:

- `/rfq/`
  - RFQ specification documents (e.g. RFQ-0100.md)
- `/repo/`
  - Canonical mapping layer (REPO-CANONICAL-MAP-001.md)
- `/schemas/`
  - A1 schema definitions (meridian-a1-markdown-artefact-standard.yaml)
- `/scripts/`
  - Validation and contract tooling (validate_contract.py)
- Root governance artifacts:
  - README.md
  - CLAUDE.md
  - CHATGPT.md
  - GEMINI.md
  - CHANGELOG.md
  - SYSTEM_HANDOVER_STATE.md
  - RIP-* governance documents

## Governance Layers Identified
1. Model onboarding layer
   - CHATGPT.md
   - CLAUDE.md
   - GEMINI.md

2. System specification layer
   - RFQ-0100.md (core RFQ baseline)
   - RIP-* protocol extensions

3. Schema enforcement layer
   - A1 markdown artefact schema (schemas/meridian-a1-markdown-artefact-standard.yaml)

4. Validation layer
   - scripts/validate_contract.py
   - GitHub Actions governance compiler workflow

## Structural Risks / Observations
- No explicit /drafts/ registry observed.
- Governance compiler exists but dependency graph enforcement not fully explicit.
- Canonical mapping not yet explicitly enforced as a graph edge system.

## Proposed Next Actions
1. Create /drafts registry index (A1 compliant)
2. Formalize RFQ-0100 → RIP dependency graph
3. Bind schema validation into CI gate enforcement
4. Define PR-level staging protocol for all A1 artefacts

## Status
Draft committed to working branch for review pipeline integration.

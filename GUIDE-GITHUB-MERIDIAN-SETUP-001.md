---
document_id: "GUIDE-GITHUB-MERIDIAN-SETUP-001"
title: "Meridian GitHub Repository Setup & Activation Guide"
version: "1.5"
status: "Approved by Kevin Slade"
classification: "Operational Guide"
date: "2026-06-11"
author: "Kevin Slade"
final_approval: "Kevin Slade"
programme: "Meridian"
purpose: >
  Provide a single, explicit, step-by-step procedure for establishing the Meridian GitHub repository and AI review ecosystem.
success_criteria:
  - "GitHub repository created and access secured."
  - "Repository structure established (provisional pending RFQ-0003)."
  - "AI review pipeline roles documented per RIP-003A v0.3."
  - "Kevin Slade final approval obtained."
changelog:
  - version: "1.5"
    date: "2026-06-11"
    editor: "Grok"
    summary: "Clean formatting, Claude & Gemini as Step 3, improved readability."
---

# Meridian GitHub Repository Setup & Activation Guide

## Current Situation
This repository is now the single source of truth for Meridian governance.

## Phase 1 — Freeze New Document Creation
Halt all new governance documents until the repository is fully operational.

## Phase 2 — Create GitHub Account Structure
1. Sign into GitHub.
2. Enable 2FA and passkey.
3. Create repository `meridian-governance` (Private) with README and .gitignore.

## Phase 3 — Build Repository Structure (Provisional)

> **PROVISIONAL** — Pending approval of RFQ-0003.

```bash
meridian-governance/
├── README.md
├── CHANGELOG.md
├── GOVERNANCE/
├── RFQ/
├── POLICIES/
├── REVIEW_PIPELINE/
├── MASTER_CHECKLISTS/
├── TEMPLATES/
├── DECISIONS/
├── ARCHIVE/
└── AUTOMATION/
```

## Phase 4 — Populate Repository
Place documents in the correct folders.

## Phase 5 — AI Review Pipeline Roles (per RIP-003A v0.3)

| Step | Participant                  | Function                              |
|------|------------------------------|---------------------------------------|
| 1    | Kevin Slade                  | Instruction                           |
| 2    | ChatGPT                      | Drafting                              |
| 3    | Claude (Anthropic) + Gemini  | Independent Review (parallel)         |
| 4    | Grok                         | Consolidation and Adjudication        |
| 5    | Kevin Slade                  | Final Approval (mandatory)            |

## Phase 6 — Version Control
1. Archive old version in `ARCHIVE/`.
2. Increment version number.
3. Update `CHANGELOG.md`.

## Phase 7 — n8n Automation Workflow
Kevin Instruction → ChatGPT Draft → (Claude + Gemini parallel) → Grok Consolidation → Kevin Final Approval → GitHub Commit

## Phase 8 — Definition of Done
- [x] Repository created
- [x] Folders created
- [x] Core files added
- [x] v1.5 approved by Kevin Slade

**Guiding Principle:** Meridian needs a reliable system more than more documents.

*End of GUIDE-GITHUB-MERIDIAN-SETUP-001 v1.5 — Approved by Kevin Slade on 2026-06-11*
# RIP-00XX — MCP Connector Setup & Validation

## Metadata
- **Document ID:** RIP-00XX-MCP-Connector-Setup
- **Date:** 2026-06-25
- **Status:** Draft
- **Scope:** Multi-agent MCP connector integration validation (ChatGPT / Claude / Grok)
- **Repository Path:** `draft/RIP-00XX-MCP-Connector-Setup.md`

---

## 1. Connector Configuration

### Enabled Connectors
| Connector | Mode | Status | Notes |
|----------|------|--------|------|
| Grok | Native connector | Active | Direct tool-native integration assumed operational |
| Claude | MCP | Active | Model Context Protocol bridge enabled |
| ChatGPT | MCP | Active | MCP server interface enabled for external agent tooling |

---

## 2. Validation Objectives

- Verify cross-agent repository access consistency
- Validate read operations across shared MCP surface
- Validate branch-level isolation and file retrieval integrity
- Confirm deterministic visibility of repository state across connectors

---

## 3. Test Results

### 3.1 Branch Access Tests

| Connector | Branch | Result | Notes |
|----------|--------|--------|------|
| Grok | main | PASS | Correct repo snapshot visibility confirmed |
| Claude MCP | main | PASS | MCP layer correctly resolves latest main state |
| ChatGPT MCP | main | PASS | File tree and metadata resolved successfully |

---

### 3.2 File Read Tests

| Connector | File Path | Result | Notes |
|----------|------------|--------|------|
| Grok | README.md | PASS | Full content retrieved |
| Claude MCP | CHATGPT.md | PASS | Correct file parsing via MCP |
| ChatGPT MCP | CLAUDE.md | PASS | Structural integrity preserved |

---

### 3.3 Cross-Connector Consistency Check

| Test | Result | Notes |
|------|--------|------|
| Hash consistency (README.md) | PASS | No divergence across connectors |
| Metadata parity | PASS | File tree structure aligned |
| Permission model | PASS | No unauthorized access observed |

---

## 4. Observations

- MCP layer introduces minor latency variance vs native connector (Grok)
- No evidence of branch desynchronization across connectors
- File resolution stable across identical commit references
- Schema interpretation consistent across all tested agents

---

## 5. Open Issues / Follow-ups

- Need explicit commit-hash pinning test across MCP connectors
- Add write-path validation (currently read-only validated)
- Expand test coverage to:
  - pull request diffs
  - large file streaming
  - concurrent multi-agent writes

---

## 6. Next Actions

- Promote test suite to automated CI validation layer
- Introduce deterministic connector conformance scoring
- Extend RIP-00XX into formal MCP interoperability spec (RIP-00XX-A)

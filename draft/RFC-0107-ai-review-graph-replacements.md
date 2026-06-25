# RFC-0107 — AI Review Graph: Replacement of Gemini Node

## 1. Context
The AI review graph contains a cross-model validation node currently lacking strong GitHub-native execution, MCP compatibility, OAuth-first authorization, and bidirectional repository mutation capability.

This creates degraded determinism in review consensus formation.

---

## 2. Problem Statement
Constraints:
- No MCP-native integration layer
- No standardized OAuth tool delegation
- Weak GitHub write-loop participation
- Reduced orchestration determinism

Impact:
- Review inconsistency across agents
- Duplicate validation overhead
- Reduced PR confidence scoring stability

---

## 3. Replacement Criteria
Hard:
- GitHub read/write capability
- OAuth tool authorization
- MCP-compatible or equivalent abstraction layer
- Long-context repo reasoning
- Deterministic tool invocation

Soft:
- Multi-tool orchestration
- Structured output formats
- Strong diff reasoning

---

## 4. Candidate Nodes
Claude (Anthropic): reasoning anchor
ChatGPT (OpenAI): orchestration layer
GitHub Copilot (Microsoft): execution layer
Perplexity AI: verification layer
Grok (xAI): optional signal layer

---

## 5. Topology
Claude -> ChatGPT -> Copilot -> Perplexity -> optional Grok

---

## 6. Governance
- No single node may both decide and execute writes
- Execution limited to OAuth-authorized GitHub agents
- Verification externalized
- MCP-compatible agents preferred

---

## 7. Recommendation
Replace current Gemini node with Claude + ChatGPT dual-core + Copilot execution authority.

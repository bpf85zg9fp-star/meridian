# LLM-CONTEXT.md - Consolidated Context for All AI Models

**Single consolidated file for easy pasting into Gemini, ChatGPT, Claude, Grok when GitHub connector fails.**

**Repository**: https://github.com/bpf85zg9fp-star/meridian
**Last Updated**: 2026-06-24

## 1. Core Governance (Always Read First)

- **README.md**: Overall overview and quick start.
- **RFQ-0100.md**: Authoritative repository structure and rules.
- **RIP-003A.md**: Review Instruction Protocol.
- **A1 Schema**: schemas/meridian-a1-markdown-artefact-standard.yaml
- Model-specific: CHATGPT.md, GEMINI.md, GROK.md, CLAUDE.md (all in repo root)

## 2. Quick Repository Summary (from RFQ-0100)

The `bpf85zg9fp-star/meridian` repo is the **single authoritative source** for all Meridian governance.

Key directories:
- `rfq/` — Requirements & Frameworks
- `rip/` — Review procedures
- `reviews/` — Review artefacts
- `schemas/` — Validation schemas
- `templates/` — Document templates
- Root .md files for AI onboarding

**Human Authority**: Kevin Slade (Estate Principal) — final approval required.

## 3. AI Onboarding Rules (Summary from Model Files)

**All Models**:
- Explore first with tools.
- Enforce A1 YAML frontmatter strictly.
- No hallucinations on paths or structure.
- Begin responses with: "Following Meridian governance..."
- Reference specific governance files.

**When Connector Fails**: Paste this entire LLM-CONTEXT.md or individual files.

## 4. GitHub Connector Troubleshooting (Token & Access Issues)

**Common Problems**:
- `PERMISSION_DENIED`, rate limits, or inaccessible repo even though public.
- AI platforms (Gemini, Claude, ChatGPT) often cannot directly use pasted PATs in chat.

**Recommended Solutions**:
1. **Primary Workaround**: Paste this full `LLM-CONTEXT.md` into the chat.
2. **PAT Setup**: Generate a fine-grained PAT (repo:contents read) and try linking via OAuth in platform settings (Claude Projects, Cursor, etc.). Pasting token mid-chat rarely works.
3. **Manual Paste**: When connector fails, user will provide key files.
4. **Preferred Tools**: Use Cursor / Continue.dev with PAT configured in settings for best results.
5. **Fallback**: Work with provided context and ask user for specific files as needed.

## 5. Full Key File Contents (for pasting)

**Paste sections as needed.** Full contents available in repo.

---

*(Full contents of model files and key governance included for brevity — see repo for complete versions.)*

This file serves as a reliable fallback for all AI interactions with the Meridian repository.
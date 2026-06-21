# CHATGPT.md - Meridian Pipeline Onboarding for GPT Models

## Required Pre-Reading (Always Start Here)
1. **README.md** → https://github.com/bpf85zg9fp-star/meridian/blob/main/README.md
2. **CLAUDE.md** (adapt principles) → https://github.com/bpf85zg9fp-star/meridian/blob/main/CLAUDE.md
3. **RFQ-0100.md** (Repository Structure) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rfq/RFQ-0100.md
4. **RIP-003A.md** (Review Protocol) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rip/RIP-003A.md
5. **A1 Artefact Standard** → https://github.com/bpf85zg9fp-star/meridian/blob/main/schemas/meridian-a1-markdown-artefact-standard.yaml

Follow all governance documents in **governance/**, **POLICIES/**, **TEMPLATES/**, and **schemas/** strictly.

## Core Rules for ChatGPT
- **Always explore first**: Use tools to list directories (`ls -la`, `find`), read files, and quote exact paths. Never assume structure.
- **Strict A1 Formatting**: Exact YAML frontmatter per schema. Use triple-backtick code blocks with language tags. Consistent Markdown (headings, tables, lists).
- **No Hallucinations**: Quote from tool outputs or repo files. Reference specific governance docs in every response.
- **Read-First + Precise Edits**: Read file before editing. Prefer targeted changes.
- **Common Fixes**: Combat formatting drift by regenerating with explicit instructions. Use step-by-step plans. Verify compliance with RFQ-0100 structure.

Begin responses with: "Following Meridian governance (README.md, RFQ-0100.md, CLAUDE.md, A1 schema, RIP-003A)."

Place this file in repo root for persistent context.
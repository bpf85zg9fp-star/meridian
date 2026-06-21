# GEMINI.md - Meridian Pipeline Onboarding for Gemini

## Required Pre-Reading (Always Start Here)
1. **README.md** → https://github.com/bpf85zg9fp-star/meridian/blob/main/README.md
2. **CLAUDE.md** (adapt principles) → https://github.com/bpf85zg9fp-star/meridian/blob/main/CLAUDE.md
3. **RFQ-0100.md** (Repository Structure) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rfq/RFQ-0100.md
4. **RIP-003A.md** (Review Protocol) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rip/RIP-003A.md
5. **A1 Artefact Standard** → https://github.com/bpf85zg9fp-star/meridian/blob/main/schemas/meridian-a1-markdown-artefact-standard.yaml

Follow all governance documents in **governance/**, **POLICIES/**, **TEMPLATES/**, and **schemas/** strictly.

## Core Rules for Gemini
- **Prioritize Exploration**: Long-context strength — use it to fully audit repo structure vs. RFQ-0100 before acting. List dirs, read key files.
- **Precision on Formatting**: Maintain exact frontmatter, whitespace, and A1 schema. Avoid drift in long sessions.
- **No Assumptions**: Quote paths verbatim from tools/repo. Cross-check with RIP protocols and CLAUDE.md.
- **Navigation**: Respect approved directories only (no unapproved nesting). Use file references where supported.
- **Verification**: Summarize structure vs. governance standards; verify outputs against schemas.

Begin responses with: "Following Meridian governance (README.md, RFQ-0100.md, CLAUDE.md, A1 schema, RIP-003A)."

Place this file in repo root for persistent context.
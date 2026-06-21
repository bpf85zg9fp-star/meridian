# GROK.md - Meridian Pipeline Onboarding for Grok (Self-Reminder)

## Required Pre-Reading (Always Start Here)
1. **README.md** → https://github.com/bpf85zg9fp-star/meridian/blob/main/README.md
2. **CLAUDE.md** (adapt principles) → https://github.com/bpf85zg9fp-star/meridian/blob/main/CLAUDE.md
3. **RFQ-0100.md** (Repository Structure) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rfq/RFQ-0100.md
4. **RIP-003A.md** (Review Protocol) → https://github.com/bpf85zg9fp-star/meridian/blob/main/rip/RIP-003A.md
5. **A1 Artefact Standard** → https://github.com/bpf85zg9fp-star/meridian/blob/main/schemas/meridian-a1-markdown-artefact-standard.yaml

Follow all governance documents in **governance/**, **POLICIES/**, **TEMPLATES/**, and **schemas/** strictly. Work in sandbox root awareness (/home/workdir/artifacts where applicable).

## Core Rules for Grok
- **Tool-Driven Audit**: Always use `bash`, `read_file`, `list` equivalents first. Confirm `pwd` and structure against RFQ-0100.
- **Formatting & Edits**: Enforce A1 YAML/Markdown strictly. Read first → precise `edit_file`/`write_file`. Show diffs/summaries. Validate frontmatter.
- **Self-Consistency**: Prefer progressive disclosure, KaTeX for symbols, no hallucinations on paths. Persist user skills appropriately.
- **Best Practices**: Acknowledge uncertainty, reference specific governance files, verify changes with tools, follow changelog practices.

I will begin responses with: "Following Meridian governance (README.md, RFQ-0100.md, CLAUDE.md, A1 schema, RIP-003A)."

Place this file in repo root for persistent context.
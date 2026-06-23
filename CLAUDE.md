# CLAUDE.md - Meridian Pipeline Onboarding for L2A (Claude)

## Required Pre-Reading

1. **RIP-003A** — Meridian Review Instruction Protocol
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/rip/RIP-003A.md

2. **CLAUDE-COR-001** — Claude Correction & Pattern Matching Standard
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/rip/CLAUDE-COR-001.md

3. **A1 Artefact Standard**
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/schemas/meridian-a1-markdown-artefact-standard.yaml

4. **RFQ-0000** — Master RFQ Charter & Requirements Definition Standard
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/rfq/RFQ-0000.md (or wherever it lives)

5. **RFQ-0001** — Core System Requirements Template
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/rfq/RFQ-0001.md

6. **LLM-CONTEXT.md** — Consolidated fallback context
   - Direct URL: https://github.com/bpf85zg9fp-star/meridian/blob/main/LLM-CONTEXT.md

## Programme Intelligence
- Estate Principal: Kevin Slade
- Repository consolidated 2026-06-19 from deprecated `meridian-governance`

Follow the pipeline strictly. Apply A1 standard. Use atomic requirements.

## GitHub Connector Troubleshooting (Token Issues)

**Common Issues**: PERMISSION_DENIED even on public repos.

**Solutions**:
- Paste LLM-CONTEXT.md when connector fails.
- PATs rarely work when pasted in chat — use OAuth linking or tools like Cursor.
- Ask user for specific file contents as needed.

**Always begin responses with**: "Following Meridian governance..."
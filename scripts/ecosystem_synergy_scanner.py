import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

def parse_a1_frontmatter(content):
    match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

def collect_components(repo_root):
    referenced_by = defaultdict(list)
    declared_docs = {}
    for scan_dir in ("rfq", "drafts"):
        base = os.path.join(repo_root, scan_dir)
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for f in files:
                if not f.endswith(".md"):
                    continue
                with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                    fm = parse_a1_frontmatter(file.read())
                if not fm:
                    continue
                doc_id = fm.get("document_id", Path(f).stem)
                declared_docs[doc_id] = fm.get("title", "")
                for dep in fm.get("dependencies", []) or []:
                    if isinstance(dep, dict) and "component" in dep:
                        referenced_by[dep["component"]].append(doc_id)
    return referenced_by, declared_docs

def scan_ecosystem(repo_root):
    print("Scanning for synergy/gaps across ecosystem...")
    referenced_by, declared_docs = collect_components(repo_root)

    gaps = [c for c in referenced_by if c not in declared_docs]
    synergy_candidates = {c: docs for c, docs in referenced_by.items() if len(set(docs)) > 1}

    print(f"Documents scanned: {len(declared_docs)}")
    print(f"Components referenced: {len(referenced_by)}")
    if gaps:
        print(f"\n{len(gaps)} component(s) with no dedicated artefact:")
        for g in gaps:
            print(f"  - {g}")
    if synergy_candidates:
        print(f"\n{len(synergy_candidates)} component(s) shared across documents (review for consolidation):")
        for c, docs in synergy_candidates.items():
            print(f"  - {c}: {', '.join(sorted(set(docs)))}")

    return {"documents_scanned": len(declared_docs), "gaps": gaps, "synergy_candidates": synergy_candidates}

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    scan_ecosystem(repo_root)

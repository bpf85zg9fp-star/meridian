import os
import yaml
import json
from pathlib import Path
from datetime import date

def generate_placeholder(parent, child, reasoning, doc_id):
    """Create A1-compliant placeholder MD."""
    placeholder_id = f"DEP-{doc_id.split('-')[-1]}-{child.replace(' ', '-').lower()[:20]}"
    content = f"""---
document_id: "{placeholder_id}"
title: "Placeholder: {child}"
version: "0.1"
status: "Draft"
classification: "Dependency Placeholder"
date: "{date.today()}"
programme: "Meridian"
author: "Auto-Generator (via dependency_resolver)"
yaml_schema: "meridian-a1-markdown-artefact-standard.yaml v1.1"
dependencies: []
related_documents: ["{doc_id}"]
---
# {placeholder_id} — Placeholder for {child}

**Reasoning**: {reasoning}

This placeholder was auto-generated to fill dependency gap from {parent}. Review and expand per Tier 0 standards.
"""
    target_dir = Path(f"drafts/{{placeholder_id}}")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / f"{{placeholder_id}}.md").write_text(content)
    return str(target_dir)

def main():
    repo_root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    graph_path = repo_root / "dependency_graph.json"
    
    if not graph_path.exists():
        print("No graph found. Run resolver first.")
        return
    
    with open(graph_path) as f:
        graph = json.load(f)
    
    for sug in graph.get("suggestions", []):
        path = generate_placeholder(sug["parent"], sug["child"], sug["reasoning"], "RFQ-0102")
        print(f"Generated placeholder at {path}")

if __name__ == "__main__":
    main()
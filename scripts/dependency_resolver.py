import os
import sys
import yaml
import re
from pathlib import Path
import json

def parse_a1_frontmatter(content):
    """Extract YAML frontmatter from Markdown."""
    match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except:
            return None
    return None

def resolve_dependencies(docs_path):
    """Scan docs, parse dependencies, suggest placeholders."""
    graph = {"nodes": [], "edges": [], "suggestions": []}
    
    for root, _, files in os.walk(docs_path):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    fm = parse_a1_frontmatter(content)
                    if fm and "dependencies" in fm:
                        deps = fm.get("dependencies", [])
                        doc_id = fm.get("document_id", Path(path).stem)
                        graph["nodes"].append(doc_id)
                        
                        for dep in deps:
                            if isinstance(dep, dict) and "component" in dep:
                                component = dep["component"]
                                requires = dep.get("requires", [])
                                graph["edges"].append((doc_id, component))
                                for req in requires:
                                    graph["edges"].append((component, req))
                                    graph["suggestions"].append({
                                        "parent": component,
                                        "child": req,
                                        "reasoning": f"Dependency from {doc_id} for {component}. Auto-suggested placeholder for completeness."
                                    })
    
    return graph

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    rfq_path = os.path.join(repo_root, "rfq")
    draft_path = os.path.join(repo_root, "drafts")
    
    print("Resolving dependencies across RFQs and drafts...")
    graph = resolve_dependencies(rfq_path)
    draft_graph = resolve_dependencies(draft_path)
    
    # Merge graphs
    graph["nodes"].extend(draft_graph["nodes"])
    graph["edges"].extend(draft_graph["edges"])
    graph["suggestions"].extend(draft_graph["suggestions"])
    
    out_path = os.path.join(repo_root, "dependency_graph.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)
    
    print(f"Dependency graph generated at {out_path}")
    if graph["suggestions"]:
        print("\nSuggested placeholders:")
        for sug in graph["suggestions"]:
            print(f"- Create placeholder for {sug['child']} under {sug['parent']}: {sug['reasoning']}")

if __name__ == "__main__":
    main()
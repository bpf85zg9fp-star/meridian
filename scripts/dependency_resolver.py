import os
import yaml
import re
import json
import logging
from pathlib import Path
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("dependency_resolver")

def parse_a1_frontmatter(content, source_path):
    match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        log.warning(f"Malformed A1 frontmatter in {source_path}: {e}")
        return None

class DependencyGraph:
    def __init__(self):
        self.adj = defaultdict(set)
        self.nodes = set()

    def add_edge(self, parent, child):
        self.nodes.add(parent)
        self.nodes.add(child)
        self.adj[parent].add(child)

    def find_cycles(self):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {n: WHITE for n in self.nodes}
        cycles, path = [], []

        def dfs(node):
            color[node] = GRAY
            path.append(node)
            for neighbor in self.adj[node]:
                if color[neighbor] == GRAY:
                    cycles.append(path[path.index(neighbor):] + [neighbor])
                elif color[neighbor] == WHITE:
                    dfs(neighbor)
            path.pop()
            color[node] = BLACK

        for node in list(self.nodes):
            if color[node] == WHITE:
                dfs(node)
        return cycles

    def to_dict(self):
        return {
            "nodes": sorted(self.nodes),
            "edges": sorted({(p, c) for p, kids in self.adj.items() for c in kids}),
        }

def resolve_dependencies(docs_path, graph, suggestions):
    if not os.path.isdir(docs_path):
        log.warning(f"Path does not exist, skipping: {docs_path}")
        return
    for root, _, files in os.walk(docs_path):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            fm = parse_a1_frontmatter(content, path)
            if not fm or "dependencies" not in fm:
                continue
            doc_id = fm.get("document_id", Path(path).stem)
            for dep in fm.get("dependencies", []):
                if not isinstance(dep, dict) or "component" not in dep:
                    log.warning(f"Malformed dependency entry in {doc_id}, skipping")
                    continue
                component = dep["component"]
                graph.add_edge(doc_id, component)
                for req in dep.get("requires", []):
                    graph.add_edge(component, req)
                    suggestions.append({
                        "parent": component,
                        "child": req,
                        "source_doc": doc_id,
                        "reasoning": f"Template-derived: {component} (from {doc_id}) lists '{req}' with no dedicated artefact found yet.",
                        "reasoning_type": "template",
                    })

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    graph = DependencyGraph()
    suggestions = []

    print("Resolving dependencies across RFQs and drafts...")
    resolve_dependencies(os.path.join(repo_root, "rfq"), graph, suggestions)
    resolve_dependencies(os.path.join(repo_root, "drafts"), graph, suggestions)

    cycles = graph.find_cycles()
    output = graph.to_dict()
    output["suggestions"] = suggestions
    output["cycles_detected"] = cycles

    out_path = os.path.join(repo_root, "dependency_graph.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Dependency graph generated at {out_path}")
    print(f"Nodes: {len(output['nodes'])}, Edges: {len(output['edges'])}")
    if cycles:
        print(f"\nWARNING: {len(cycles)} circular dependency chain(s):")
        for c in cycles:
            print(f"  - {' -> '.join(c)}")
    if suggestions:
        print(f"\n{len(suggestions)} non-blocking placeholder suggestion(s):")
        for s in suggestions:
            print(f"- {s['child']} under {s['parent']} (from {s['source_doc']})")

if __name__ == "__main__":
    main()

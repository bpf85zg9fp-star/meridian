import os
import sys
import json
import re
from pathlib import Path

RE_EVENT = re.compile(r"(DocumentCreated|ReviewRequested|ReviewCompleted|DecisionRecorded|DocumentApproved|DocumentRejected|DocumentArchived|GrokConsolidation)")
RE_REQ = re.compile(r"RFQ-\d{4}|RIP-\d{3}[A-Z]?")
RE_DOC = re.compile(r"document_id:\s*[\"']?([A-Z0-9-]+)[\"']?", re.I)

def extract_markdown_files(root_dir):
    docs = []
    for path in Path(root_dir).rglob("*.md"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                docs.append((str(path), content))
        except Exception as e:
            print(f"Warning: Could not read {path}: {e}")
    return docs

def build_graph(docs):
    nodes = set()
    edges = []
    for filepath, text in docs:
        reqs = RE_REQ.findall(text) + RE_DOC.findall(text)
        events = RE_EVENT.findall(text)
        doc_id = Path(filepath).stem.upper()

        for r in set(reqs):
            nodes.add(r)
        for e in events:
            nodes.add(e)
        for r in reqs:
            for e in events:
                edges.append((r, e))
            edges.append((doc_id, "TraceToReview"))

    nodes.add("drafts/")
    nodes.add("reviews/")
    nodes.add("rfq/")
    nodes.add("rip/")

    return {
        "nodes": sorted(list(nodes)),
        "edges": list(set(edges)),
        "metadata": {
            "generated": "2026-06-24",
            "scan_dirs": ["rfq", "rip", "drafts", "reviews", "continuum", "docs", "scripts"]
        }
    }

def generate_mermaid(graph):
    mermaid = "graph TD\n"
    for node in graph["nodes"]:
        safe_node = node.replace('-','_').replace('/','')
        mermaid += f"    {safe_node}[{node}]\n"
    for src, tgt in graph["edges"]:
        safe_src = src.replace('-','_').replace('/','')
        safe_tgt = tgt.replace('-','_').replace('/','')
        mermaid += f"    {safe_src} --> {safe_tgt}\n"
    return mermaid

def main():
    repo_root = Path(".")
    print("Building enhanced RTM/AI Review Graph...")

    scan_dirs = ["rfq", "rip", "drafts", "reviews", "continuum", "docs", "scripts"]
    all_docs = []
    for d in scan_dirs:
        dpath = repo_root / d
        if dpath.exists():
            all_docs.extend(extract_markdown_files(dpath))

    graph = build_graph(all_docs)

    out_json = repo_root / "rtm_graph.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    out_md = repo_root / "rtm_graph.md"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Meridian AI Review Graph\n\n```mermaid\n")
        f.write(generate_mermaid(graph))
        f.write("\n```\n")

    print(f"RTM GRAPH GENERATED: {out_json} and {out_md}")

if __name__ == "__main__":
    main()
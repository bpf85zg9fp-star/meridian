import os
import sys
import json
import re

RE_EVENT = re.compile(r"(DocumentCreated|ReviewRequested|ReviewCompleted|DecisionRecorded|DocumentApproved|DocumentRejected|DocumentArchived)")
RE_REQ = re.compile(r"RFQ-\d{4}")


def extract_markdown_files(path):
    docs = []
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                    docs.append(file.read())
    return docs


def build_graph(texts):
    nodes = set()
    edges = []

    for t in texts:
        reqs = RE_REQ.findall(t)
        events = RE_EVENT.findall(t)

        for r in reqs:
            nodes.add(r)
        for e in events:
            nodes.add(e)

        for r in reqs:
            for e in events:
                edges.append((r, e))

    return {
        "nodes": list(nodes),
        "edges": edges
    }


def validate_graph(graph):
    if not graph["nodes"]:
        print("ERROR: Empty RTM graph")
        return False
    return True


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("Building RTM graph...")

    rfq_docs = extract_markdown_files(os.path.join(repo_root, "rfq"))
    rip_docs = extract_markdown_files(os.path.join(repo_root, "rip"))

    graph = build_graph(rfq_docs + rip_docs)

    if not validate_graph(graph):
        print("RTM VALIDATION FAILED")
        sys.exit(1)

    out_path = os.path.join(repo_root, "rtm_graph.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    print(f"RTM GRAPH GENERATED at {out_path}")


if __name__ == "__main__":
    main()

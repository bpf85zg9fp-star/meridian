import argparse
import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GENERATED_DIR = os.path.join(REPO_ROOT, "_generated")

RE_EVENT = re.compile(
    r"(DocumentCreated|ReviewRequested|ReviewCompleted|"
    r"DecisionRecorded|DocumentApproved|DocumentRejected|DocumentArchived)"
)
RE_REQ = re.compile(r"RFQ-\d{4}")


def extract_markdown_files(path: str) -> list:
    docs = []
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as fh:
                    docs.append(fh.read())
    return docs


def build_graph(texts: list) -> dict:
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
    return {"nodes": list(nodes), "edges": edges}


def validate_graph(graph: dict) -> bool:
    if not graph["nodes"]:
        print("ERROR: Empty RTM graph — no RFQ references found")
        return False
    print(f"RTM graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    return True


def main():
    parser = argparse.ArgumentParser(description="Meridian RTM graph builder")
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate graph only; do not write output file",
    )
    parser.add_argument(
        "--output",
        default=os.path.join(GENERATED_DIR, "rtm_graph.json"),
        help="Output path for generated graph JSON",
    )
    args = parser.parse_args()

    print("Building RTM graph...")

    rfq_docs = extract_markdown_files(os.path.join(REPO_ROOT, "rfq"))
    rip_docs = extract_markdown_files(os.path.join(REPO_ROOT, "rip"))
    graph = build_graph(rfq_docs + rip_docs)

    if not validate_graph(graph):
        print("RTM VALIDATION FAILED")
        sys.exit(1)

    if args.validate:
        print("RTM VALIDATION PASSED (validate-only mode, no output written)")
        return

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)
    print(f"RTM GRAPH GENERATED at {args.output}")


if __name__ == "__main__":
    main()

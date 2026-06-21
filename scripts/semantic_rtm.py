from collections import defaultdict, deque


class SemanticRTM:
    """Graph-based RTM engine replacing regex extraction with structured reasoning."""

    def __init__(self):
        self.graph = defaultdict(set)
        self.nodes = set()

    def add_requirement(self, req_id: str):
        self.nodes.add(req_id)

    def link(self, src: str, dst: str, relation: str = "relates_to"):
        self.nodes.add(src)
        self.nodes.add(dst)
        self.graph[src].add((dst, relation))

    def build_from_events(self, events: list):
        """Build RTM from structured events (not text parsing)."""

        for e in events:
            et = e.get("event_type")
            doc = e.get("document_id")

            if not doc:
                continue

            self.add_requirement(doc)

            if et in ("DocumentApproved", "ReviewCompleted"):
                self.link(doc, f"event:{et}", "satisfies")
            elif et in ("ReviewRequested",):
                self.link(doc, f"event:{et}", "triggers")

    def traverse(self, start: str, depth: int = 3):
        visited = set()
        q = deque([(start, 0)])
        result = []

        while q:
            node, d = q.popleft()
            if node in visited or d > depth:
                continue

            visited.add(node)
            result.append(node)

            for nxt, rel in self.graph.get(node, []):
                q.append((nxt, d + 1))

        return result

    def export(self):
        return {
            "nodes": list(self.nodes),
            "edges": {k: list(v) for k, v in self.graph.items()}
        }

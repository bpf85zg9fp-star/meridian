import os
import json
import uuid
from datetime import datetime, timezone

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EVENT_STORE_DIR = os.path.join(REPO_ROOT, "event_store")


class EventStore:
    """Append-only event store for Meridian governance system."""

    def __init__(self):
        os.makedirs(EVENT_STORE_DIR, exist_ok=True)

    def _get_path(self, document_id: str):
        return os.path.join(EVENT_STORE_DIR, f"{document_id}.jsonl")

    def append(self, document_id: str, event_type: str, payload: dict):
        event = {
            "event_id": str(uuid.uuid4()),
            "document_id": document_id,
            "event_type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "payload": payload or {}
        }

        path = self._get_path(document_id)

        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        return event

    def load(self, document_id: str):
        path = self._get_path(document_id)
        if not os.path.exists(path):
            return []

        events = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    events.append(json.loads(line))
        return events

    def replay(self, document_id: str):
        """Reconstruct state from event stream."""
        events = self.load(document_id)
        state = {}

        for e in events:
            et = e["event_type"]

            if et == "DocumentCreated":
                state["created"] = True
            elif et == "ReviewRequested":
                state["review"] = "requested"
            elif et == "ReviewCompleted":
                state["review"] = "completed"
            elif et == "DocumentApproved":
                state["status"] = "approved"
            elif et == "DocumentRejected":
                state["status"] = "rejected"

        return state

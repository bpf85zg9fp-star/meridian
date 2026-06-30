import os
import json
import uuid
import hmac
import hashlib
from datetime import datetime, timezone
from scripts.key_management import KeyManager

# ---------------------------------------------------------------------------
# Key is sourced exclusively from the environment via KeyManager.
# Set MERIDIAN_KEY as a GitHub Actions secret (Settings > Secrets > Actions).
# Never hardcode a key value in this file.
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EVENT_STORE_DIR = os.path.join(REPO_ROOT, "event_store")

_km = KeyManager()


class CryptoEventStore:
    """Append-only, HMAC-signed event store for Meridian governance."""

    def __init__(self):
        os.makedirs(EVENT_STORE_DIR, exist_ok=True)

    def _get_path(self, document_id: str) -> str:
        safe = document_id.replace("/", "_").replace("\\", "_")
        return os.path.join(EVENT_STORE_DIR, f"{safe}.jsonl")

    def _sign(self, payload: str) -> str:
        raw_key = _km.get_key()
        key_bytes = raw_key.encode() if isinstance(raw_key, str) else raw_key
        return hmac.new(key_bytes, payload.encode("utf-8"), hashlib.sha256).hexdigest()

    def append(self, document_id: str, event_type: str, payload: dict) -> dict:
        event = {
            "event_id": str(uuid.uuid4()),
            "document_id": document_id,
            "event_type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "payload": payload or {},
        }
        body = json.dumps(event, sort_keys=True)
        signed = {"event": event, "sig": self._sign(body)}
        path = self._get_path(document_id)
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(signed) + "\n")
        return event

    def load(self, document_id: str) -> list:
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

    def verify_event(self, signed_record: dict) -> bool:
        """Return True if the stored signature matches a freshly computed one."""
        event = signed_record.get("event", {})
        stored_sig = signed_record.get("sig", "")
        body = json.dumps(event, sort_keys=True)
        return hmac.compare_digest(stored_sig, self._sign(body))

    def replay(self, document_id: str) -> dict:
        """Reconstruct current document state from verified event stream."""
        state = {}
        for record in self.load(document_id):
            if not self.verify_event(record):
                raise ValueError(
                    f"Tampered event detected for {document_id}: "
                    f"event_id={record.get('event', {}).get('event_id')}"
                )
            e = record["event"]
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

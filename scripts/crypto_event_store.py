import os
import json
import hmac
import hashlib
import uuid
from datetime import datetime, timezone

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EVENT_STORE_DIR = os.path.join(REPO_ROOT, "event_store_secure")

SECRET_KEY = b"meridian-governance-key"  # NOTE: replace with secret manager in production


class CryptoEventStore:
    """Append-only event store with HMAC signing for integrity verification."""

    def __init__(self):
        os.makedirs(EVENT_STORE_DIR, exist_ok=True)

    def _get_path(self, document_id: str):
        return os.path.join(EVENT_STORE_DIR, f"{document_id}.jsonl")

    def _sign(self, event: dict) -> str:
        payload = json.dumps(event, sort_keys=True).encode("utf-8")
        return hmac.new(SECRET_KEY, payload, hashlib.sha256).hexdigest()

    def append(self, document_id: str, event_type: str, payload: dict):
        event = {
            "event_id": str(uuid.uuid4()),
            "document_id": document_id,
            "event_type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "payload": payload or {}
        }

        event["signature"] = self._sign(event)

        path = self._get_path(document_id)

        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        return event

    def verify_event(self, event: dict) -> bool:
        signature = event.get("signature")
        if not signature:
            return False

        unsigned = dict(event)
        unsigned.pop("signature", None)

        expected = self._sign(unsigned)
        return hmac.compare_digest(signature, expected)

    def load(self, document_id: str):
        path = self._get_path(document_id)
        if not os.path.exists(path):
            return []

        events = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    events.append(json.loads(line))
        return events

    def verify_stream(self, document_id: str):
        events = self.load(document_id)
        return all(self.verify_event(e) for e in events)

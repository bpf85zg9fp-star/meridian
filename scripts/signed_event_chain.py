import os
import json
import uuid
import hmac
import hashlib
from datetime import datetime, timezone
from scripts.key_management import KeyManager

# ---------------------------------------------------------------------------
# Uses KeyManager — reads MERIDIAN_KEY from environment.
# For production, replace KeyManager with scripts/vault_kms.py VaultKMS.
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAIN_STORE_DIR = os.path.join(REPO_ROOT, "event_store")

_km = KeyManager()


class SignedEventChain:
    """Linked-hash chain: each event includes the signature of its predecessor."""

    def __init__(self):
        os.makedirs(CHAIN_STORE_DIR, exist_ok=True)

    def _get_path(self, chain_id: str) -> str:
        safe = chain_id.replace("/", "_").replace("\\", "_")
        return os.path.join(CHAIN_STORE_DIR, f"{safe}.chain.jsonl")

    def _sign(self, payload: str) -> str:
        raw_key = _km.get_key()
        key_bytes = raw_key.encode() if isinstance(raw_key, str) else raw_key
        return hmac.new(key_bytes, payload.encode("utf-8"), hashlib.sha256).hexdigest()

    def append(self, chain_id: str, event_type: str, payload: dict) -> dict:
        path = self._get_path(chain_id)
        prev_sig = self._get_last_sig(path)
        event = {
            "event_id": str(uuid.uuid4()),
            "chain_id": chain_id,
            "event_type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "payload": payload or {},
            "prev_sig": prev_sig,
        }
        body = json.dumps(event, sort_keys=True)
        sig = self._sign(body)
        record = {"event": event, "sig": sig}
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
        return event

    def _get_last_sig(self, path: str) -> str:
        if not os.path.exists(path):
            return "genesis"
        last = None
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    last = json.loads(line)
        return last["sig"] if last else "genesis"

    def verify_chain(self, chain_id: str) -> bool:
        """Walk the chain; return False on first tamper/break detected."""
        path = self._get_path(chain_id)
        if not os.path.exists(path):
            return True
        prev_sig = "genesis"
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                event = record["event"]
                if event.get("prev_sig") != prev_sig:
                    return False
                body = json.dumps(event, sort_keys=True)
                if not hmac.compare_digest(record["sig"], self._sign(body)):
                    return False
                prev_sig = record["sig"]
        return True

import json
import hashlib
import hmac
from datetime import datetime, timezone
from scripts.vault_kms import VaultKMS


class SignedEventChain:
    """Implements hash-linked event chaining for tamper-evident governance logs."""

    def __init__(self):
        self.vault = VaultKMS()

    def _hash_event(self, event: dict) -> str:
        payload = json.dumps(event, sort_keys=True).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def _hmac(self, data: str) -> str:
        key = self.vault.get_primary_key().key_material
        return hmac.new(key, data.encode("utf-8"), hashlib.sha256).hexdigest()

    def sign_chain(self, events: list) -> list:
        """Adds hash chaining + HMAC signature to event stream."""

        prev_hash = "GENESIS"
        signed = []

        for e in events:
            event_copy = dict(e)

            event_hash = self._hash_event(event_copy)

            chain_input = prev_hash + event_hash
            signature = self._hmac(chain_input)

            event_copy["event_hash"] = event_hash
            event_copy["prev_hash"] = prev_hash
            event_copy["chain_signature"] = signature

            prev_hash = event_hash
            signed.append(event_copy)

        return signed

    def verify_chain(self, events: list) -> bool:
        prev_hash = "GENESIS"

        for e in events:
            expected_hash = self._hash_event({k: v for k, v in e.items() if k not in ["event_hash", "prev_hash", "chain_signature"]})

            if e.get("event_hash") != expected_hash:
                return False

            chain_input = prev_hash + expected_hash
            expected_sig = self._hmac(chain_input)

            if e.get("chain_signature") != expected_sig:
                return False

            prev_hash = expected_hash

        return True

    def certify_replay(self, events: list) -> dict:
        valid = self.verify_chain(events)

        return {
            "valid": valid,
            "event_count": len(events),
            "certified_at": datetime.now(timezone.utc).isoformat()
        }

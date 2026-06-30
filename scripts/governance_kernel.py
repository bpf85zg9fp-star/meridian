from scripts.event_store import EventStore
from scripts.crypto_event_store import CryptoEventStore


class GovernanceKernel:
    """Central governance orchestrator.

    Uses CryptoEventStore (HMAC-signed) by default.
    Set use_crypto=False in tests or environments where MERIDIAN_KEY is
    not available (the plain EventStore has no signing but is otherwise
    identical in interface).
    """

    def __init__(self, use_crypto: bool = True):
        if use_crypto:
            self._store = CryptoEventStore()
        else:
            self._store = EventStore()

    def record_created(self, document_id: str, metadata: dict = None):
        return self._store.append(
            document_id, "DocumentCreated", metadata or {}
        )

    def record_review_requested(self, document_id: str, reviewer: str = None):
        return self._store.append(
            document_id, "ReviewRequested", {"reviewer": reviewer}
        )

    def record_review_completed(self, document_id: str, outcome: str = None):
        return self._store.append(
            document_id, "ReviewCompleted", {"outcome": outcome}
        )

    def record_approved(self, document_id: str, approver: str = "Kevin"):
        return self._store.append(
            document_id, "DocumentApproved", {"approver": approver}
        )

    def record_rejected(self, document_id: str, reason: str = None):
        return self._store.append(
            document_id, "DocumentRejected", {"reason": reason}
        )

    def get_state(self, document_id: str) -> dict:
        return self._store.replay(document_id)

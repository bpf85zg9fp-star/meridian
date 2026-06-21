import event_store
import crypto_event_store


class GovernanceKernel:
    def __init__(self, use_crypto=True):
        self.store = event_store.EventStore()
        self.crypto_store = crypto_event_store.CryptoEventStore()
        self.use_crypto = use_crypto

    def append_event(self, document_id, event_type, payload):
        if self.use_crypto:
            return self.crypto_store.append(document_id, event_type, payload)
        return self.store.append(document_id, event_type, payload)

    def get_events(self, document_id):
        if self.use_crypto:
            return self.crypto_store.load(document_id)
        return self.store.load(document_id)

    def replay(self, document_id):
        events = self.get_events(document_id)
        state = {}

        for e in events:
            et = e.get("event_type")
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

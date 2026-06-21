class GovernanceInvariantViolation(Exception):
    pass


class FormalVerifier:
    """Simple invariant-based verification engine for governance rules."""

    def __init__(self):
        self.rules = []

    def add_rule(self, name, fn):
        self.rules.append((name, fn))

    def verify(self, context: dict):
        results = []

        for name, rule in self.rules:
            ok = rule(context)
            results.append({"rule": name, "valid": bool(ok)})

            if not ok:
                raise GovernanceInvariantViolation(f"Rule failed: {name}")

        return {"status": "valid", "results": results}


# Default invariants

def default_invariants(verifier: FormalVerifier):
    verifier.add_rule(
        "events_must_have_id",
        lambda ctx: all("event_id" in e for e in ctx.get("events", []))
    )

    verifier.add_rule(
        "no_empty_documents",
        lambda ctx: len(ctx.get("events", [])) > 0
    )

    verifier.add_rule(
        "crypto_integrity_if_enabled",
        lambda ctx: not ctx.get("require_crypto") or ctx.get("crypto_valid")
    )

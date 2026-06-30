# TODO: This is a stub. Replace with real audit logic:
#   - Walk event_store/ and count events per document
#   - Check all documents in rfq/ and rip/ have at least one signed event
#   - Compute compliance score from: documents with approved events / total documents
#   - Surface documents stuck in review (ReviewRequested but no ReviewCompleted)

def run() -> dict:
    """Stub audit runner. Returns a placeholder score until real logic is wired in."""
    # Placeholder — do not rely on this score for real compliance decisions.
    score = 0
    notes = [
        "governance_audit.py is a stub — real audit logic not yet implemented.",
        "Score of 0 reflects unimplemented state, not actual compliance posture.",
    ]
    return {"score": score, "notes": notes}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))

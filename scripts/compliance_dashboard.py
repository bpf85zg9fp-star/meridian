import json
from scripts.governance_audit import run as audit_run


def build_dashboard():
    audit = audit_run()

    score = audit.get("score", 0)

    if score >= 80:
        status = "HEALTHY"
    elif score >= 50:
        status = "DEGRADED"
    else:
        status = "CRITICAL"

    return {
        "system_status": status,
        "compliance_score": score,
        "audit_notes": audit.get("notes", [])
    }


if __name__ == "__main__":
    print(json.dumps(build_dashboard(), indent=2))

import os
import json
import sys

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "governance", "registry", "tier0_weights.json")

def load_weights(config_path):
    if not os.path.isfile(config_path):
        return None
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_gate(inputs, weights):
    breakdown, total_weight, weighted_sum = {}, 0.0, 0.0
    for metric, value in inputs.items():
        w = weights.get("metrics", {}).get(metric)
        if w is None:
            breakdown[metric] = {"value": value, "weight": None, "note": "unweighted — excluded"}
            continue
        breakdown[metric] = {"value": value, "weight": w, "contribution": value * w}
        weighted_sum += value * w
        total_weight += w
    score = (weighted_sum / total_weight) if total_weight > 0 else None
    threshold = weights.get("pass_threshold")
    passed = score is not None and threshold is not None and score >= threshold
    return score, breakdown, passed

def main():
    config_path = os.environ.get("TIER0_WEIGHTS_PATH", DEFAULT_CONFIG_PATH)
    weights = load_weights(config_path)

    if weights is None:
        print("Tier 0 Gate: NO WEIGHTS CONFIGURED.")
        print(f"Expected config at: {config_path}")
        print("Running in ADVISORY-ONLY mode — nothing is being blocked.")
        print("Supply reviewed weights before this can act as a hard gate.")
        sys.exit(0)

    approved = weights.get("approved", False)

    # Real inputs should come from dependency_resolver.py / ecosystem_synergy_scanner.py output.
    example_inputs = {"schema_compliance": 1.0, "gap_density": 0.5, "synergy_overlap": 0.2}
    score, breakdown, passed = run_gate(example_inputs, weights)

    print("Tier 0 Gate — breakdown:")
    for metric, detail in breakdown.items():
        print(f"  {metric}: {detail}")
    print(f"Composite score: {score}")

    if not approved:
        print("Result: ADVISORY ONLY — weights not yet approved (set 'approved': true in "
              "governance/registry/tier0_weights.json once validated). Not a pass/fail verdict.")
    else:
        print(f"Result: {'PASS' if passed else 'FLAGGED FOR HUMAN REVIEW'}")

if __name__ == "__main__":
    main()

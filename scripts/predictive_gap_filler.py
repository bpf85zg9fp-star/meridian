import os
import re
import yaml
from pathlib import Path

def parse_a1_frontmatter(content):
    match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

# Manually curated. Not inferred. Treat as unverified until a qualified
# services/structural consultant confirms each entry.
PATTERN_LIBRARY = {
    "hvac": [
        "Ductwork modifications for zoning",
        "Electrical panel upgrade: capacity increase",
        "Smart thermostat integration with existing BMS",
        "Condensate drainage and insulation retrofits",
    ],
    "windows": [
        "Window frames and structural openings",
        "Glazing specification",
        "Flashing and weatherproofing",
    ],
    "electrical": ["Panel capacity assessment", "Circuit mapping"],
}

def suggest_gaps_for_component(name):
    lower = name.lower()
    return [s for key, sl in PATTERN_LIBRARY.items() if key in lower for s in sl]

def scan_for_predictive_gaps(repo_root):
    print("Predictive gap filler: pattern-matching components against known sequences...")
    found = False
    for scan_dir in ("rfq", "drafts"):
        base = os.path.join(repo_root, scan_dir)
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for f in files:
                if not f.endswith(".md"):
                    continue
                with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                    fm = parse_a1_frontmatter(file.read())
                if not fm:
                    continue
                doc_id = fm.get("document_id", Path(f).stem)
                for dep in fm.get("dependencies", []) or []:
                    if not isinstance(dep, dict) or "component" not in dep:
                        continue
                    existing = set(dep.get("requires", []))
                    missing = set(suggest_gaps_for_component(dep["component"])) - existing
                    if missing:
                        found = True
                        print(f"\n{doc_id} — '{dep['component']}':")
                        for m in sorted(missing):
                            print(f"  suggest (pattern match, unverified): {m}")
    if not found:
        print("No pattern-matched gaps found against current library.")

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    scan_for_predictive_gaps(repo_root)

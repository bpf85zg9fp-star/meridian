import os
import sys
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------------------------------------------------------------------
# Required YAML frontmatter fields per A1 Artefact Standard v1.1
# (schemas/meridian-a1-markdown-artefact-standard.yaml)
# ---------------------------------------------------------------------------
REQUIRED_FIELDS = [
    "document_id",
    "title",
    "version",
    "status",
    "classification",
    "date",
    "programme",
    "author",
]

# Fields that are recommended but not hard-required by A1 v1.1
RECOMMENDED_FIELDS = [
    "yaml_schema",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def extract_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def validate_file(path: str) -> list:
    """Return list of error strings for the given file. Empty list = pass."""
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        return [f"Cannot read file: {e}"]

    fm = extract_frontmatter(text)
    if not fm:
        errors.append("No YAML frontmatter found (document must begin with --- block)")
        return errors

    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"Missing required A1 field: '{field}'")

    # Warn (not fail) on recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in fm or not fm[field]:
            print(f"  WARN [{os.path.relpath(path, REPO_ROOT)}]: recommended field missing: '{field}'")

    return errors


def main():
    rfq_root = os.path.join(REPO_ROOT, "rfq")
    rip_root = os.path.join(REPO_ROOT, "rip")

    md_files = []
    for base in (rfq_root, rip_root):
        for root, _, files in os.walk(base):
            for fname in files:
                if fname.endswith(".md"):
                    md_files.append(os.path.join(root, fname))

    if not md_files:
        print("WARNING: No .md files found under rfq/ or rip/")
        sys.exit(0)

    total = len(md_files)
    failed = []

    for path in md_files:
        errors = validate_file(path)
        rel = os.path.relpath(path, REPO_ROOT)
        if errors:
            failed.append(rel)
            for err in errors:
                print(f"  FAIL [{rel}]: {err}")

    print(f"\nSchema validation: {total - len(failed)}/{total} passed")

    if failed:
        print(f"SCHEMA VALIDATION FAILED ({len(failed)} file(s))")
        sys.exit(1)

    print("SCHEMA VALIDATION PASSED")


if __name__ == "__main__":
    main()

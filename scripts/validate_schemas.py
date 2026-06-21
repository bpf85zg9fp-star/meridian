import os
import sys
import re

REQUIRED_FIELDS = [
    "document_id",
    "title",
    "version",
    "status",
    "date"
]


def extract_frontmatter(content):
    if not content.startswith("---"):
        return None
    parts = content.split("---")
    if len(parts) < 3:
        return None
    return parts[1]


def validate_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fm = extract_frontmatter(content)
    if fm is None:
        print(f"ERROR: Missing frontmatter in {path}")
        return False

    missing = []
    for field in REQUIRED_FIELDS:
        if not re.search(rf"{field}:", fm):
            missing.append(field)

    if missing:
        print(f"ERROR: {path} missing fields: {missing}")
        return False

    return True


def scan_dir(path):
    ok = True
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".md"):
                if not validate_file(os.path.join(root, f)):
                    ok = False
    return ok


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("Running schema enforcement gate...")

    rfq_ok = scan_dir(os.path.join(repo_root, "rfq")) if os.path.exists(os.path.join(repo_root, "rfq")) else True
    rip_ok = scan_dir(os.path.join(repo_root, "rip")) if os.path.exists(os.path.join(repo_root, "rip")) else True

    if not (rfq_ok and rip_ok):
        print("SCHEMA VALIDATION FAILED")
        sys.exit(1)

    print("SCHEMA VALIDATION PASSED")


if __name__ == "__main__":
    main()

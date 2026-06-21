import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RFQ_PATH = os.path.join(REPO_ROOT, "rfq")
RIP_PATH = os.path.join(REPO_ROOT, "rip")


def read_files(path):
    files = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                    files.append(file.read())
    return files


def validate_presence():
    rfq_files = read_files(RFQ_PATH)
    rip_files = read_files(RIP_PATH)

    if not rfq_files:
        print("ERROR: No RFQ files found")
        return False

    if not rip_files:
        print("ERROR: No RIP files found")
        return False

    return True


def validate_cross_references():
    rfq_text = "\n".join(read_files(RFQ_PATH))
    rip_text = "\n".join(read_files(RIP_PATH))

    # Ensure RFQ-0100 exists
    if "RFQ-0100" not in rfq_text:
        print("ERROR: RFQ-0100 missing")
        return False

    # Ensure RIP-003A or RIP-003B exist
    if not re.search(r"RIP-003[AB]", rip_text):
        print("ERROR: Missing RIP-003A or RIP-003B")
        return False

    return True


def main():
    print("Running RFQ → RIP contract validation...")

    ok1 = validate_presence()
    ok2 = validate_cross_references()

    if not (ok1 and ok2):
        print("CONTRACT VALIDATION FAILED")
        sys.exit(1)

    print("CONTRACT VALIDATION PASSED")


if __name__ == "__main__":
    main()

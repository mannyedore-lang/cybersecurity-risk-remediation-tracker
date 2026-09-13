import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "security_findings.csv"

if __name__ == "__main__":
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    severity = Counter(r["severity"] for r in rows)
    status = Counter(r["status"] for r in rows)
    evidence_ready = sum(1 for r in rows if r["evidence_ready"].lower() == "yes")

    print("Severity:", dict(severity))
    print("Status:", dict(status))
    print("Evidence ready:", f"{evidence_ready}/{len(rows)}")

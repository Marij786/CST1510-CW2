"""
RECORD CHECK - completed IT lane
================================
Lane: IT
Run: python template.py
"""

from pathlib import Path


def parse_line(raw_line):
    """Clean and parse one hostname, used and total record."""
    hostname_part, rest = raw_line.strip().split(",", 1)
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = float(value.strip())
    return {
        "hostname": hostname_part.strip().lower(),
        "used": fields["used"],
        "total": fields["total"],
    }


def status_of(used, total, warning_at=90):
    """Classify storage usage as OVER LIMIT, WARNING or OK."""
    if total <= 0:
        raise ValueError("total must be greater than zero")
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= warning_at:
        return "WARNING"
    return "OK"


# Excellent tier: load at least five varied records from a text file.
data_file = Path(__file__).with_name("raw_records.txt")
with data_file.open(encoding="utf-8") as file:
    raw_records = [line.rstrip("\\n") for line in file if line.strip()]

flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    print(record, "|", status)
    if status != "OK":
        flagged_count += 1

print(f"Summary: {len(raw_records)} records, {flagged_count} flagged.")

# Required invalid-number check: float("unknown") raises ValueError.
try:
    parse_line("srv-bad,used=unknown,total=100")
except ValueError as error:
    print(f"Invalid-number test: {type(error).__name__}: {error}")

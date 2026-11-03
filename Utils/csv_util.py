import csv
from pathlib import Path

CSV_FILE = Path(__file__).resolve().parent.parent / "reports" / "created_records.csv"


def save_record(record_type, record_id, name):
    """Append a created record's ID and name. Passwords are never written."""
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
    write_header = not CSV_FILE.exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["Type", "ID", "Name"])
        writer.writerow([record_type, record_id, name])

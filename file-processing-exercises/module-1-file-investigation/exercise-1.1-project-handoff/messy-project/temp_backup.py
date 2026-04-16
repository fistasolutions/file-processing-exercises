"""Temporary backup of some experimental code Dave was working on.
Not sure if this is still needed. Was trying to add batch processing
to the pipeline endpoint."""

import csv
import json
from io import StringIO

def process_batch(csv_content):
    """Process a batch of records from CSV content."""
    reader = csv.DictReader(StringIO(csv_content))
    results = []
    errors = []

    for i, row in enumerate(reader):
        try:
            record = {
                "id": row.get("id", f"auto_{i}"),
                "name": row["name"],
                "value": float(row.get("value", 0)),
                "processed": True,
            }
            results.append(record)
        except (KeyError, ValueError) as e:
            errors.append({"row": i, "error": str(e)})

    return {
        "total": len(results) + len(errors),
        "success": len(results),
        "failed": len(errors),
        "results": results,
        "errors": errors,
    }

# Quick test
if __name__ == "__main__":
    test_csv = "id,name,value\n1,test,42.0\n2,broken\n3,good,99.9"
    print(json.dumps(process_batch(test_csv), indent=2))

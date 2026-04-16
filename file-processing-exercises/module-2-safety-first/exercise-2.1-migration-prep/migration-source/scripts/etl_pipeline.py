"""ETL pipeline for processing customer data."""

import csv
import json
import os
from datetime import datetime

def extract(filepath):
    """Extract data from a CSV file."""
    with open(filepath) as f:
        return list(csv.DictReader(f))

def transform(records):
    """Transform records: normalize names, calculate derived fields."""
    transformed = []
    for record in records:
        record["name"] = record.get("name", "").strip().title()
        if "monthly_spend" in record:
            record["annual_projection"] = float(record["monthly_spend"]) * 12
        record["processed_at"] = datetime.now().isoformat()
        transformed.append(record)
    return transformed

def load(records, output_path):
    """Load transformed records to JSON file."""
    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)
    print(f"Loaded {len(records)} records to {output_path}")

if __name__ == "__main__":
    data = extract("data/customers.csv")
    result = transform(data)
    load(result, "data/processed_customers.json")

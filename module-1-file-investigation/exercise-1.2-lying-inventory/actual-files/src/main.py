"""Main application module for the analytics service."""

import json
import sys

def load_data(filepath):
    """Load data from a JSON or CSV file."""
    if filepath.endswith(".json"):
        with open(filepath) as f:
            return json.load(f)
    elif filepath.endswith(".csv"):
        import csv
        with open(filepath) as f:
            return list(csv.DictReader(f))
    else:
        raise ValueError(f"Unsupported format: {filepath}")

def analyze(data):
    """Run basic analysis on loaded data."""
    return {
        "count": len(data),
        "fields": list(data[0].keys()) if data else [],
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <datafile>")
        sys.exit(1)
    result = analyze(load_data(sys.argv[1]))
    print(json.dumps(result, indent=2))

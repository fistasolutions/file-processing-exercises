"""Data export utilities for CSV and JSON output."""

import csv
import json
from io import StringIO

def export_csv(records, fields=None):
    """Export a list of dicts to CSV string."""
    if not records:
        return ""
    fields = fields or list(records[0].keys())
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)
    return output.getvalue()

def export_json(records, pretty=True):
    """Export records to JSON string."""
    indent = 2 if pretty else None
    return json.dumps(records, indent=indent, default=str)

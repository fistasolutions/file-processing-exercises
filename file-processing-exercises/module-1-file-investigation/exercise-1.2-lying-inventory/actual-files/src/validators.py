"""Input validation functions."""

import re

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_email(email):
    """Check if an email address is valid."""
    return bool(EMAIL_PATTERN.match(email))

def validate_date(date_str):
    """Check if a date string is in YYYY-MM-DD format."""
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return bool(pattern.match(date_str))

def validate_required(data, fields):
    """Check that all required fields are present and non-empty."""
    missing = [f for f in fields if not data.get(f)]
    return missing

"""Utility functions for the task manager."""

from datetime import datetime

def format_date(dt):
    """Format a datetime object for display."""
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.strftime("%B %d, %Y at %I:%M %p")

def validate_priority(priority):
    """Validate that priority is one of the allowed values."""
    allowed = {"low", "medium", "high", "critical"}
    return priority.lower() in allowed

def truncate_text(text, max_length=100):
    """Truncate text to max_length, adding ellipsis if needed."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."

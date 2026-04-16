"""Helper functions for data transformation."""

def normalize_name(name):
    """Normalize a name string: strip, title case."""
    return name.strip().title()

def safe_float(value, default=0.0):
    """Convert to float safely, returning default on failure."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def chunk_list(lst, size=100):
    """Split a list into chunks of given size."""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

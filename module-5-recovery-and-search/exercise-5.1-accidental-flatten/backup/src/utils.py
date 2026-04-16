"""Shared utility functions."""

def format_response(data, status="success"):
    return {"status": status, "data": data}

def paginate(items, page=1, per_page=20):
    start = (page - 1) * per_page
    return items[start:start + per_page]

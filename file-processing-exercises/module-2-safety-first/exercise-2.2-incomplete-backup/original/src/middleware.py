"""Middleware for request logging and rate limiting."""

import time
import functools
from flask import request, g

def log_request(f):
    """Log request details for debugging."""
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        g.start_time = time.time()
        response = f(*args, **kwargs)
        duration = time.time() - g.start_time
        print(f"{request.method} {request.path} -> {response.status_code} ({duration:.3f}s)")
        return response
    return decorated

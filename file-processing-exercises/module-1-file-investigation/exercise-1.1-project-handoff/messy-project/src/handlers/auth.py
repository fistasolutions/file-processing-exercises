"""Authentication handler for API endpoints."""

import functools
import os
from flask import request, jsonify

API_KEY = os.getenv("API_KEY", "FAKE-api-key-for-exercise")

def require_auth(f):
    """Decorator that requires a valid API key in the Authorization header."""
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Missing Authorization header"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid auth format. Use: Bearer <token>"}), 401

        token = auth_header.split(" ", 1)[1]
        if token != API_KEY:
            return jsonify({"error": "Invalid API key"}), 403

        return f(*args, **kwargs)
    return decorated

def validate_token(token):
    """Validate a JWT token and return the payload."""
    # TODO: Implement proper JWT validation
    # Currently just checks if token matches the API key
    return token == API_KEY

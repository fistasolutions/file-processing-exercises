"""Main application entry point for the data pipeline service."""

import os
import logging
from flask import Flask, jsonify, request
from .utils import load_config, validate_input
from .handlers.auth import require_auth
from .handlers.users import get_user, create_user

app = Flask(__name__)
logger = logging.getLogger(__name__)

config = load_config(os.getenv("APP_ENV", "dev"))

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": config.get("version", "unknown")})

@app.route("/api/users", methods=["GET"])
@require_auth
def list_users():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 20, type=int)
    users = get_user(page=page, limit=limit)
    return jsonify({"users": users, "page": page})

@app.route("/api/users", methods=["POST"])
@require_auth
def add_user():
    data = request.get_json()
    if not validate_input(data, required=["name", "email"]):
        return jsonify({"error": "Missing required fields"}), 400
    user = create_user(data)
    return jsonify(user), 201

@app.route("/api/process", methods=["POST"])
@require_auth
def process_data():
    """Process incoming data through the pipeline."""
    payload = request.get_json()
    # TODO: implement actual pipeline processing
    # For now, just validate and return
    if not payload:
        return jsonify({"error": "Empty payload"}), 400
    return jsonify({"status": "queued", "id": "placeholder"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)

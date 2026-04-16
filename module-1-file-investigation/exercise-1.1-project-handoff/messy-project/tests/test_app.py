"""Tests for the main application endpoints."""

import json
import pytest

# NOTE: These tests were written for an older version of the app.
# Some may need updating after the API restructure in March.

class TestHealthEndpoint:
    def test_health_returns_ok(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["status"] == "ok"

    def test_health_includes_version(self, client):
        response = client.get("/health")
        data = json.loads(response.data)
        assert "version" in data

class TestUsersEndpoint:
    def test_list_users_requires_auth(self, client):
        response = client.get("/api/users")
        assert response.status_code == 401

    def test_list_users_with_valid_key(self, client, auth_headers):
        response = client.get("/api/users", headers=auth_headers)
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "users" in data

    def test_create_user_missing_fields(self, client, auth_headers):
        response = client.post(
            "/api/users",
            headers=auth_headers,
            data=json.dumps({"name": "Test"}),
            content_type="application/json"
        )
        assert response.status_code == 400

    def test_create_user_success(self, client, auth_headers):
        response = client.post(
            "/api/users",
            headers=auth_headers,
            data=json.dumps({"name": "Test User", "email": "test@example.com"}),
            content_type="application/json"
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data["name"] == "Test User"

class TestProcessEndpoint:
    def test_process_requires_auth(self, client):
        response = client.post("/api/process")
        assert response.status_code == 401

    def test_process_empty_payload(self, client, auth_headers):
        response = client.post(
            "/api/process",
            headers=auth_headers,
            content_type="application/json"
        )
        assert response.status_code == 400

"""Tests for the main application."""

import pytest

def test_index_returns_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Task Tracker" in response.json["message"]

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

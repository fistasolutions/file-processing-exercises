#!/bin/bash
# Scenario B: The Staging Mistake
# Creates a git repo where too many files are staged for commit.
# Student must unstage the wrong files and commit only production code.

set -e

REPO_DIR="staging-mistake-repo"

rm -rf "$REPO_DIR"
mkdir -p "$REPO_DIR/src" "$REPO_DIR/tests"
cd "$REPO_DIR"

git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

# Create initial state with just a README
cat > README.md << 'EOF'
# My API Project

A simple REST API built with Python.
EOF

git add README.md
git commit -m "Initial commit with README"

# Now create all the files that will be "accidentally staged"

cat > src/api.py << 'PYEOF'
"""API endpoint handlers — production code."""

from typing import Optional


def get_users(limit: int = 10, offset: int = 0) -> list[dict]:
    """Fetch a paginated list of users."""
    # Production implementation
    return [
        {"id": i, "name": f"User {i}", "active": True}
        for i in range(offset, offset + limit)
    ]


def get_user_by_id(user_id: int) -> Optional[dict]:
    """Fetch a single user by ID."""
    if user_id < 0:
        return None
    return {"id": user_id, "name": f"User {user_id}", "active": True}


def create_user(name: str, email: str) -> dict:
    """Create a new user record."""
    return {"id": 999, "name": name, "email": email, "active": True}


def delete_user(user_id: int) -> bool:
    """Soft-delete a user by ID."""
    # In production this would mark user as inactive
    return True
PYEOF

cat > src/models.py << 'PYEOF'
"""Data models for the API — production code."""


class User:
    """Represents a user in the system."""

    def __init__(self, user_id: int, name: str, email: str, active: bool = True):
        self.id = user_id
        self.name = name
        self.email = email
        self.active = active

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active,
        }

    def deactivate(self):
        self.active = False

    def __repr__(self):
        status = "active" if self.active else "inactive"
        return f"User({self.id}, {self.name}, {status})"
PYEOF

cat > tests/test_api.py << 'PYEOF'
"""UNFINISHED tests for api.py — NOT ready for commit."""

# TODO: These tests are incomplete. Do not commit yet.

def test_get_users():
    # Need to add assertions
    pass

def test_create_user():
    # Placeholder — implementation pending
    pass

# FIXME: Need to mock the database connection
# FIXME: Need error case tests
PYEOF

cat > tests/test_models.py << 'PYEOF'
"""UNFINISHED tests for models.py — NOT ready for commit."""

# TODO: These tests are scaffolding only. Not ready.

def test_user_creation():
    pass

def test_user_deactivate():
    pass

# FIXME: Need edge case tests for invalid inputs
PYEOF

cat > debug.log << 'EOF'
[2025-01-20 14:32:01] DEBUG Starting API server...
[2025-01-20 14:32:01] DEBUG Loading configuration from config.json
[2025-01-20 14:32:02] DEBUG Database connection established
[2025-01-20 14:32:15] DEBUG GET /users?limit=10 -> 200 OK (23ms)
[2025-01-20 14:32:18] DEBUG GET /users/5 -> 200 OK (12ms)
[2025-01-20 14:33:01] ERROR Failed to connect to cache: Connection refused
[2025-01-20 14:33:01] DEBUG Falling back to direct database queries
[2025-01-20 14:35:22] DEBUG POST /users -> 201 Created (45ms)
EOF

cat > temp_credentials.txt << 'EOF'
Temporary dev credentials — DELETE AFTER TESTING
=================================================
API_TOKEN=FAKE-temporary-token-for-exercise
ADMIN_PASSWORD=FAKE-admin-password-for-exercise
DB_CONNECTION=postgresql://dev:FAKE-dev-password-for-exercise@localhost/mydb
=================================================
REMEMBER: These are for local dev only. Never commit this file.
EOF

# Stage EVERYTHING (the mistake)
git add -A

echo ""
echo "=== Scenario B: Staging Mistake Created ==="
echo "Enter the '$REPO_DIR' directory and run 'git status' to see the problem."
echo "Everything is staged — your job is to unstage the wrong files."
echo ""

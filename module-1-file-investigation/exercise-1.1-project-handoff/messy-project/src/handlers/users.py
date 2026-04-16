"""User management handlers."""

import uuid
from datetime import datetime

# In-memory store for development
_users_db = [
    {"id": "usr_001", "name": "Alice Chen", "email": "alice@example.com", "role": "admin", "created": "2024-01-15"},
    {"id": "usr_002", "name": "Bob Martinez", "email": "bob@example.com", "role": "editor", "created": "2024-02-20"},
    {"id": "usr_003", "name": "Carol Williams", "email": "carol@example.com", "role": "viewer", "created": "2024-03-10"},
]

def get_user(user_id=None, page=1, limit=20):
    """Get a user by ID or return paginated list."""
    if user_id:
        for user in _users_db:
            if user["id"] == user_id:
                return user
        return None

    start = (page - 1) * limit
    end = start + limit
    return _users_db[start:end]

def create_user(data):
    """Create a new user and return it."""
    user = {
        "id": f"usr_{uuid.uuid4().hex[:6]}",
        "name": data["name"],
        "email": data["email"],
        "role": data.get("role", "viewer"),
        "created": datetime.now().isoformat()[:10],
    }
    _users_db.append(user)
    return user

def delete_user(user_id):
    """Delete a user by ID."""
    global _users_db
    _users_db = [u for u in _users_db if u["id"] != user_id]

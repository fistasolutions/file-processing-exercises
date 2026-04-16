#!/bin/bash
# Branch Tangle Setup
# Creates a repo with:
# - Commits on wrong branches
# - An orphaned branch with needed code
# - Two feature branches that conflict with each other

set -e

REPO_DIR="tangled-repo-workspace"

rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

# --- Set up main branch with base code ---

cat > app.py << 'PYEOF'
"""Main application — a simple URL shortener."""

URLS = {}
COUNTER = 1000


def shorten(long_url):
    """Create a short code for a URL."""
    global COUNTER
    code = f"s{COUNTER}"
    URLS[code] = long_url
    COUNTER += 1
    return code


def resolve(short_code):
    """Look up the original URL for a short code."""
    return URLS.get(short_code, None)


def list_all():
    """List all shortened URLs."""
    for code, url in URLS.items():
        print(f"  {code} -> {url}")
PYEOF

cat > storage.py << 'PYEOF'
"""Storage layer — currently in-memory, will be replaced."""

_store = {}


def save(key, value):
    _store[key] = value


def load(key):
    return _store.get(key)


def delete(key):
    _store.pop(key, None)


def list_keys():
    return list(_store.keys())
PYEOF

git add -A
git commit -m "Initial URL shortener with in-memory storage"

# --- Create feature-analytics branch with correct work ---

git checkout -b feature-analytics

cat > analytics.py << 'PYEOF'
"""Analytics module — tracks URL usage statistics."""

from collections import defaultdict
from datetime import datetime

_clicks = defaultdict(list)


def record_click(short_code):
    """Record a click event for a short URL."""
    _clicks[short_code].append(datetime.now().isoformat())


def get_click_count(short_code):
    """Get total clicks for a short URL."""
    return len(_clicks[short_code])


def get_top_urls(limit=5):
    """Get the most clicked URLs."""
    sorted_codes = sorted(_clicks.keys(), key=lambda c: len(_clicks[c]), reverse=True)
    return [(code, len(_clicks[code])) for code in sorted_codes[:limit]]
PYEOF

git add analytics.py
git commit -m "Add analytics module for tracking clicks"

# --- BUT someone accidentally committed storage changes to the analytics branch ---

cat > storage.py << 'PYEOF'
"""Storage layer — JSON file backend (this belongs on feature-storage branch!)."""

import json
import os

STORAGE_FILE = "urls.json"


def save(key, value):
    data = _load_all()
    data[key] = value
    _save_all(data)


def load(key):
    data = _load_all()
    return data.get(key)


def delete(key):
    data = _load_all()
    data.pop(key, None)
    _save_all(data)


def list_keys():
    return list(_load_all().keys())


def _load_all():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)


def _save_all(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=2)
PYEOF

git add storage.py
git commit -m "Switch to JSON file storage (WRONG BRANCH - should be on feature-storage)"

# --- Create feature-storage branch from main ---

git checkout main
git checkout -b feature-storage

# This branch also tries to modify storage.py but differently (creates conflict)
cat > storage.py << 'PYEOF'
"""Storage layer — SQLite backend."""

import sqlite3
import os

DB_FILE = "urls.db"


def _get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)
    return conn


def save(key, value):
    conn = _get_conn()
    conn.execute("INSERT OR REPLACE INTO urls (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()


def load(key):
    conn = _get_conn()
    row = conn.execute("SELECT value FROM urls WHERE key = ?", (key,)).fetchone()
    conn.close()
    return row[0] if row else None


def delete(key):
    conn = _get_conn()
    conn.execute("DELETE FROM urls WHERE key = ?", (key,))
    conn.commit()
    conn.close()


def list_keys():
    conn = _get_conn()
    rows = conn.execute("SELECT key FROM urls").fetchall()
    conn.close()
    return [r[0] for r in rows]
PYEOF

git add storage.py
git commit -m "Implement SQLite storage backend"

# --- Create an orphaned branch with a needed utility module ---

git checkout main
git checkout -b orphan-utils

cat > utils.py << 'PYEOF'
"""Utility functions needed by multiple modules."""

import hashlib
import re


def validate_url(url):
    """Check if a string looks like a valid URL."""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def generate_code(url, length=6):
    """Generate a deterministic short code from a URL."""
    hash_hex = hashlib.md5(url.encode()).hexdigest()
    return hash_hex[:length]


def sanitize_url(url):
    """Strip whitespace and ensure URL has a scheme."""
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url
PYEOF

git add utils.py
git commit -m "Add URL validation and code generation utilities"

# Make this branch "orphaned" by going back to main (no merge pointer)
git checkout main

# --- Add one more commit to main so it's ahead ---

cat >> app.py << 'PYEOF'


def stats():
    """Print basic statistics."""
    print(f"  Total URLs: {len(URLS)}")
    print(f"  Next code: s{COUNTER}")
PYEOF

git add app.py
git commit -m "Add basic stats function to main app"

echo ""
echo "=== Branch Tangle Created ==="
echo ""
echo "Enter the '$REPO_DIR' directory and explore with 'git branch' and 'git log --all --oneline --graph'"
echo ""
echo "Problems to fix:"
echo "  1. feature-analytics has a storage commit that belongs on feature-storage"
echo "  2. feature-storage and feature-analytics both modified storage.py (conflict)"
echo "  3. orphan-utils has needed code that no branch has merged"
echo "  4. You need to cleanly merge analytics + correct storage + utils into main"
echo ""

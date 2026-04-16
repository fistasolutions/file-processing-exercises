#!/bin/bash
# Scenario A: The Unstaged Mess
# Creates a git repo where an AI made changes to 4 files without committing.
# Student must sort good changes from bad and selectively restore/commit.

set -e

REPO_DIR="unstaged-mess-repo"

# Clean up if exists
rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

# --- Create the original "good" state ---

cat > app.py << 'PYEOF'
"""Simple note-taking application."""

import json
import os

NOTES_FILE = "notes.json"


def load_notes():
    """Load notes from file."""
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    """Save notes to file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


def add_note(title, content):
    """Add a new note."""
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    return len(notes)


def search_notes(keyword):
    """Search notes by keyword in title or content."""
    notes = load_notes()
    return [n for n in notes if keyword.lower() in n["title"].lower()
            or keyword.lower() in n["content"].lower()]


if __name__ == "__main__":
    print("Notes App v1.0")
    notes = load_notes()
    print(f"You have {len(notes)} notes.")
PYEOF

cat > utils.py << 'PYEOF'
"""Utility functions."""

def truncate(text, length=50):
    if len(text) <= length:
        return text
    return text[:length] + "..."

def count_words(text):
    return len(text.split())
PYEOF

cat > config.py << 'PYEOF'
"""Configuration settings."""

APP_NAME = "Notes App"
VERSION = "1.0"
API_KEY = "FAKE-notes-api-key-for-exercise"
MAX_NOTE_LENGTH = 5000
DEFAULT_FORMAT = "json"
PYEOF

cat > README.md << 'PYEOF'
# Notes App

A simple command-line note-taking application.

## Features
- Add notes with title and content
- Search notes by keyword
- Persistent JSON storage

## Usage
```bash
python app.py
```
PYEOF

git add -A
git commit -m "Initial project setup with notes app"

# --- Now simulate AI making changes to all 4 files without staging ---

# app.py: Mix of good (type hints) and bad (introduced bug in search)
cat > app.py << 'PYEOF'
"""Simple note-taking application."""

import json
import os
from typing import Optional

NOTES_FILE = "notes.json"


def load_notes() -> list[dict]:
    """Load notes from file."""
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes: list[dict]) -> None:
    """Save notes to file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


def add_note(title: str, content: str) -> int:
    """Add a new note."""
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    return len(notes)


def search_notes(keyword: str) -> list[dict]:
    """Search notes by keyword in title or content."""
    notes = load_notes()
    # BUG: changed to case-sensitive search (was case-insensitive before)
    return [n for n in notes if keyword in n["title"]
            or keyword in n["content"]]


if __name__ == "__main__":
    print("Notes App v1.0")
    notes = load_notes()
    print(f"You have {len(notes)} notes.")
PYEOF

# utils.py: Good changes — added docstrings and a new useful function
cat > utils.py << 'PYEOF'
"""Utility functions for text processing and formatting."""


def truncate(text: str, length: int = 50) -> str:
    """Truncate text to a given length, appending ellipsis if needed.

    Args:
        text: The input string to truncate.
        length: Maximum length before truncation.

    Returns:
        The original or truncated string.
    """
    if len(text) <= length:
        return text
    return text[:length] + "..."


def count_words(text: str) -> int:
    """Count the number of words in a text string.

    Args:
        text: The input string.

    Returns:
        Number of whitespace-separated words.
    """
    return len(text.split())


def format_note_preview(title: str, content: str, max_content: int = 40) -> str:
    """Format a note for display in a list view.

    Args:
        title: The note title.
        content: The note content.
        max_content: Maximum characters of content to show.

    Returns:
        Formatted string like 'Title — Content preview...'
    """
    preview = truncate(content, max_content)
    return f"{title} — {preview}"
PYEOF

# config.py: Bad change — accidentally overwrote the API key
cat > config.py << 'PYEOF'
"""Configuration settings."""

APP_NAME = "Notes App"
VERSION = "1.0"
API_KEY = "FAKE-wrong-key-ai-overwrote-this"
MAX_NOTE_LENGTH = 5000
DEFAULT_FORMAT = "json"
PYEOF

# README.md: Unwanted rewrite — completely different tone and style
cat > README.md << 'PYEOF'
# NOTES APP - THE ULTIMATE NOTE TAKING SOLUTION!!!

## WHY NOTES APP?

Because everyone needs notes! This is the BEST note app ever created.
It uses CUTTING EDGE technology like JSON and Python to deliver
an UNPARALLELED note-taking experience!

## AMAZING FEATURES
- BLAZING FAST note creation
- REVOLUTIONARY keyword search
- ENTERPRISE GRADE JSON storage

## GET STARTED NOW!!!
Just run `python app.py` and PREPARE TO BE AMAZED!

Built with love and AI! 🚀🚀🚀
PYEOF

echo ""
echo "=== Scenario A: Unstaged Mess Created ==="
echo "Enter the '$REPO_DIR' directory and use 'git status' to see the mess."
echo "Your job: keep good changes, discard bad ones."
echo ""

#!/bin/bash
# Scenario A: Branch Mismatch
# Creates a local repo with "master" as default branch.
# Student must rename to "main" to match GitHub conventions.

set -e

REPO_DIR="branch-mismatch-repo"

rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

# Initialize with "master" as default branch (old convention)
git init -b master
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

cat > app.py << 'PYEOF'
"""Simple greeting app."""


def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}! Welcome to the project."


def farewell(name):
    """Return a farewell string."""
    return f"Goodbye, {name}! See you next time."


if __name__ == "__main__":
    print(greet("World"))
PYEOF

cat > README.md << 'EOF'
# Greeting App

A simple Python greeting application.

## Usage

```bash
python app.py
```

## Note

This project was initialized with `master` as the default branch.
GitHub now uses `main` as the default. You need to rename the branch
before pushing.
EOF

git add -A
git commit -m "Initial commit on master branch"

# Add a few more commits to make the history interesting
cat > tests.py << 'PYEOF'
"""Tests for greeting app."""


def test_greet():
    from app import greet
    assert greet("Alice") == "Hello, Alice! Welcome to the project."


def test_farewell():
    from app import farewell
    assert farewell("Bob") == "Goodbye, Bob! See you next time."
PYEOF

git add tests.py
git commit -m "Add basic tests for greet and farewell"

echo ""
echo "=== Scenario A: Branch Mismatch Created ==="
echo "Enter '$REPO_DIR' and notice: 'git branch' shows 'master', not 'main'."
echo "Your task: rename the branch to 'main' before pushing to GitHub."
echo "Hint: git branch -m master main"
echo ""

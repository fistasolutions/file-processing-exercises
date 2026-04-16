#!/bin/bash
# Scenario C: The Bad Commit
# Creates a git repo with a working state, then a broken commit on top.
# Student must use git revert to undo the broken commit.

set -e

REPO_DIR="bad-commit-repo"

rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

# Commit 1: Working calculator with basic operations
cat > calculator.py << 'PYEOF'
"""Simple calculator module."""


def add(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with zero-check."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
PYEOF

git add calculator.py
git commit -m "Add calculator with basic operations"

# Commit 2: Add square root and power (still working)
cat > calculator.py << 'PYEOF'
"""Simple calculator module."""

import math


def add(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with zero-check."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square_root(a):
    """Return the square root of a non-negative number."""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def power(base, exponent):
    """Raise base to the given exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return base ** exponent
PYEOF

git add calculator.py
git commit -m "Add square root and power functions"

# Commit 3: BROKEN "refactor" — removes input validation and has division bug
cat > calculator.py << 'PYEOF'
"""Simple calculator module — REFACTORED for performance."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # "Optimized" — removed the zero check for speed
    return a / b


def square_root(a):
    return math.sqrt(a)


def power(base, exponent):
    return base ** exponent
PYEOF

git add calculator.py
git commit -m "Refactor all operations for performance"

echo ""
echo "=== Scenario C: Bad Commit Created ==="
echo "Enter the '$REPO_DIR' directory and run 'git log --oneline' to see the history."
echo "The latest commit broke everything. Use 'git revert' to fix it."
echo ""

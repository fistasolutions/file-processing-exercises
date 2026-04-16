#!/bin/bash
# Scenario B: Wrong Remote
# Creates a local repo with an incorrect remote URL configured.
# Student must diagnose and fix the remote configuration.

set -e

REPO_DIR="wrong-remote-repo"

rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

cat > app.py << 'PYEOF'
"""Budget tracker application."""

expenses = []


def add_expense(description, amount, category="general"):
    """Add an expense entry."""
    expenses.append({
        "description": description,
        "amount": round(float(amount), 2),
        "category": category,
    })


def total_spent():
    """Get total amount spent."""
    return sum(e["amount"] for e in expenses)


def by_category():
    """Group expenses by category."""
    categories = {}
    for exp in expenses:
        cat = exp["category"]
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += exp["amount"]
    return categories


if __name__ == "__main__":
    add_expense("Coffee", 4.50, "food")
    add_expense("Bus ticket", 2.75, "transport")
    add_expense("Notebook", 8.99, "supplies")
    print(f"Total: ${total_spent():.2f}")
    print(f"By category: {by_category()}")
PYEOF

git add -A
git commit -m "Add budget tracker app"

# Set up WRONG remote URLs (common mistakes)
git remote add origin https://github.com/WRONG-USER/WRONG-REPO.git
git remote add upstream https://github.com/ALSO-WRONG/NOT-A-REAL-REPO.git

echo ""
echo "=== Scenario B: Wrong Remote Created ==="
echo "Enter '$REPO_DIR' and run 'git remote -v' to see the problem."
echo "The remote URLs point to non-existent repositories."
echo "Your task: fix the remote URLs to point to YOUR GitHub repo."
echo ""
echo "Commands you'll need:"
echo "  git remote -v                          # See current remotes"
echo "  git remote set-url origin NEW_URL      # Fix origin URL"
echo "  git remote remove upstream             # Remove wrong upstream"
echo ""

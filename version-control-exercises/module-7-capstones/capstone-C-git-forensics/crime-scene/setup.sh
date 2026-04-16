#!/bin/bash
# Git Forensics Crime Scene Setup
# Creates a repository with multiple layers of problems:
# 1. Secrets committed in history (later "deleted" but still in git log)
# 2. A force-push that overwrote work
# 3. Unresolved merge conflicts left in a file
# 4. Abandoned feature branches with useful code
# 5. A mysterious revert that nobody documented

set -e

REPO_DIR="crime-scene-repo"

rm -rf "$REPO_DIR"
mkdir "$REPO_DIR"
cd "$REPO_DIR"

git init
git config user.email "lead-dev@company.local"
git config user.name "Lead Developer"

# === Layer 1: Initial project with secrets accidentally committed ===

cat > app.py << 'PYEOF'
"""Company internal tool — expense tracker."""

import json


def load_expenses():
    with open("expenses.json", "r") as f:
        return json.load(f)


def total_by_department(expenses):
    totals = {}
    for exp in expenses:
        dept = exp["department"]
        totals[dept] = totals.get(dept, 0) + exp["amount"]
    return totals


def generate_report(expenses):
    totals = total_by_department(expenses)
    print("=== Expense Report ===")
    for dept, amount in sorted(totals.items()):
        print(f"  {dept}: ${amount:,.2f}")
    print(f"  TOTAL: ${sum(totals.values()):,.2f}")
PYEOF

cat > expenses.json << 'EOF'
[
    {"id": 1, "department": "Engineering", "amount": 5420.00, "description": "Cloud hosting"},
    {"id": 2, "department": "Marketing", "amount": 3200.00, "description": "Ad campaign"},
    {"id": 3, "department": "Engineering", "amount": 1800.00, "description": "Software licenses"},
    {"id": 4, "department": "HR", "amount": 950.00, "description": "Training materials"},
    {"id": 5, "department": "Marketing", "amount": 2100.00, "description": "Conference booth"}
]
EOF

# SECRET: Accidentally committed!
cat > .env << 'EOF'
DATABASE_URL=postgresql://admin:FAKE-production-db-password-for-exercise@db.company.internal:5432/expenses
API_SECRET=FAKE-api-secret-for-exercise
STRIPE_KEY=FAKE-stripe-key-for-exercise
AWS_ACCESS_KEY=FAKE-aws-access-key-for-exercise
AWS_SECRET_KEY=FAKE-aws-secret-key-for-exercise
EOF

git add -A
git commit -m "Initial project setup"

# === Layer 1b: Someone "deleted" the secrets but they're still in history ===

rm .env
cat > .gitignore << 'EOF'
.env
__pycache__/
*.pyc
EOF

git add -A
git commit -m "Remove .env file and add gitignore (oops)"

# === Layer 2: Feature branch with good work ===

git checkout -b feature-export

cat > export.py << 'PYEOF'
"""Export expenses to CSV format."""

import csv


def to_csv(expenses, filepath="expenses.csv"):
    """Export expenses list to a CSV file."""
    if not expenses:
        return

    fieldnames = ["id", "department", "amount", "description"]
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Exported {len(expenses)} expenses to {filepath}")


def to_summary_csv(expenses, filepath="summary.csv"):
    """Export department summaries to CSV."""
    from app import total_by_department
    totals = total_by_department(expenses)

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Department", "Total"])
        for dept, amount in sorted(totals.items()):
            writer.writerow([dept, f"{amount:.2f}"])
    print(f"Exported summary to {filepath}")
PYEOF

git add export.py
git commit -m "Add CSV export functionality"

# Add tests on this branch
cat > test_export.py << 'PYEOF'
"""Tests for export module."""


def test_to_csv_creates_file():
    import os
    from export import to_csv
    expenses = [{"id": 1, "department": "Test", "amount": 100, "description": "Test expense"}]
    to_csv(expenses, "test_output.csv")
    assert os.path.exists("test_output.csv")
    os.remove("test_output.csv")


def test_to_csv_empty():
    from export import to_csv
    # Should not raise an error
    to_csv([], "test_empty.csv")
PYEOF

git add test_export.py
git commit -m "Add tests for export module"

# === Layer 3: Back to main, simulate force-push disaster ===

git checkout main

# Junior dev makes commits
git config user.email "junior@company.local"
git config user.name "Junior Developer"

cat > utils.py << 'PYEOF'
"""Utility functions for the expense tracker."""


def format_currency(amount):
    """Format a number as USD currency string."""
    return f"${amount:,.2f}"


def validate_expense(expense):
    """Validate an expense entry has required fields."""
    required = ["department", "amount", "description"]
    for field in required:
        if field not in expense:
            raise ValueError(f"Missing required field: {field}")
    if expense["amount"] < 0:
        raise ValueError("Amount cannot be negative")
    return True
PYEOF

git add utils.py
git commit -m "Add utility functions"

# Junior dev makes another commit
cat > filters.py << 'PYEOF'
"""Filter expenses by various criteria."""


def by_department(expenses, department):
    return [e for e in expenses if e["department"] == department]


def by_amount_range(expenses, min_amount=0, max_amount=float("inf")):
    return [e for e in expenses if min_amount <= e["amount"] <= max_amount]


def top_expenses(expenses, n=5):
    return sorted(expenses, key=lambda e: e["amount"], reverse=True)[:n]
PYEOF

git add filters.py
git commit -m "Add expense filtering functions"

# Simulate force-push by resetting back (losing the junior dev's work)
# We create a backup branch first so the student can find it
git branch backup-before-force-push

git reset --hard HEAD~2

# Now lead dev commits something different (simulating what happens after force push)
git config user.email "lead-dev@company.local"
git config user.name "Lead Developer"

cat > analytics.py << 'PYEOF'
"""Analytics module — replaced the junior dev's work after force push."""

def monthly_trend(expenses):
    """This function exists but the filtering code is lost."""
    pass  # TODO: The filter functions were lost in a force push
PYEOF

git add analytics.py
git commit -m "Add analytics placeholder (after force push incident)"

# === Layer 4: Create abandoned branch with merge conflicts ===

git checkout -b feature-departments

# Modify app.py in a way that conflicts with main
cat > app.py << 'PYEOF'
"""Company internal tool — expense tracker with department management."""

import json

DEPARTMENTS = ["Engineering", "Marketing", "HR", "Sales", "Operations"]


def load_expenses():
    with open("expenses.json", "r") as f:
        return json.load(f)


def validate_department(department):
    """Ensure department is in the approved list."""
    if department not in DEPARTMENTS:
        raise ValueError(f"Unknown department: {department}. Valid: {DEPARTMENTS}")
    return True


def total_by_department(expenses):
    totals = {}
    for exp in expenses:
        dept = exp["department"]
        validate_department(dept)
        totals[dept] = totals.get(dept, 0) + exp["amount"]
    return totals


def generate_report(expenses):
    totals = total_by_department(expenses)
    print("=== Expense Report by Department ===")
    for dept in DEPARTMENTS:
        amount = totals.get(dept, 0)
        print(f"  {dept}: ${amount:,.2f}")
    print(f"  TOTAL: ${sum(totals.values()):,.2f}")
PYEOF

git add app.py
git commit -m "Add department validation and management"

# Go back to main and also modify app.py differently
git checkout main

cat > app.py << 'PYEOF'
"""Company internal tool — expense tracker with date filtering."""

import json
from datetime import datetime


def load_expenses():
    with open("expenses.json", "r") as f:
        return json.load(f)


def total_by_department(expenses):
    totals = {}
    for exp in expenses:
        dept = exp["department"]
        totals[dept] = totals.get(dept, 0) + exp["amount"]
    return totals


def filter_by_date(expenses, start_date, end_date):
    """Filter expenses by date range."""
    return [e for e in expenses if start_date <= e.get("date", "") <= end_date]


def generate_report(expenses):
    totals = total_by_department(expenses)
    print("=== Expense Report ===")
    print(f"  Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    for dept, amount in sorted(totals.items()):
        print(f"  {dept}: ${amount:,.2f}")
    print(f"  TOTAL: ${sum(totals.values()):,.2f}")
PYEOF

git add app.py
git commit -m "Add date filtering to expense tracker"

# === Layer 5: A mysterious revert with no explanation ===

# First add a useful feature
cat > notifications.py << 'PYEOF'
"""Send notifications when expense thresholds are reached."""


def check_budget(expenses, budget_limit=10000):
    """Check if total expenses exceed budget."""
    total = sum(e["amount"] for e in expenses)
    if total > budget_limit:
        return f"WARNING: Total expenses (${total:,.2f}) exceed budget (${budget_limit:,.2f})"
    remaining = budget_limit - total
    return f"Budget OK: ${remaining:,.2f} remaining"


def department_alert(expenses, department, limit=5000):
    """Alert if a department exceeds its budget."""
    dept_total = sum(e["amount"] for e in expenses if e["department"] == department)
    if dept_total > limit:
        return f"ALERT: {department} spent ${dept_total:,.2f} (limit: ${limit:,.2f})"
    return None
PYEOF

git add notifications.py
git commit -m "Add budget notification system"

# Now revert it with no explanation
git revert HEAD --no-edit

echo ""
echo "==========================================="
echo "  GIT FORENSICS CRIME SCENE CREATED"
echo "==========================================="
echo ""
echo "Enter the '$REPO_DIR' directory and investigate."
echo ""
echo "Crimes to discover:"
echo "  1. Secrets still lurking in git history"
echo "  2. A force-push that destroyed a junior dev's work"
echo "  3. An abandoned feature branch (feature-departments)"
echo "  4. An orphaned feature branch with useful code (feature-export)"
echo "  5. A mysterious revert of the notification system"
echo ""
echo "Your forensic toolkit:"
echo "  git log --all --oneline --graph"
echo "  git log --all --diff-filter=D -- '.env'"
echo "  git show <commit-hash>"
echo "  git branch -a"
echo "  git reflog"
echo "  git diff branch1..branch2"
echo ""
echo "Write a full forensic report documenting all findings."
echo ""

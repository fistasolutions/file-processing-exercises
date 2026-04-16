#!/bin/bash
# Scenario C: Push Rejected
# Creates a local repo and a "fake remote" (bare repo) that has commits
# the local doesn't have — simulating the "push rejected" error.
# Student must pull/merge before pushing.

set -e

WORKSPACE="push-rejected-workspace"

rm -rf "$WORKSPACE"
mkdir "$WORKSPACE"
cd "$WORKSPACE"

# Create a bare repo to act as "remote"
mkdir remote-repo.git
cd remote-repo.git
git init --bare
cd ..

# Clone it to simulate a "teammate" making changes
git clone remote-repo.git teammate-copy
cd teammate-copy
git config user.email "teammate@exercise.local"
git config user.name "Teammate"

cat > app.py << 'PYEOF'
"""Shared project — a simple quiz game."""

questions = [
    {"q": "What command initializes a git repo?", "a": "git init"},
    {"q": "What command stages files?", "a": "git add"},
    {"q": "What command creates a snapshot?", "a": "git commit"},
]


def ask_question(question):
    print(f"\nQ: {question['q']}")
    answer = input("Your answer: ").strip()
    if answer.lower() == question["a"].lower():
        print("Correct!")
        return True
    else:
        print(f"Wrong. The answer was: {question['a']}")
        return False


def run_quiz():
    score = 0
    for q in questions:
        if ask_question(q):
            score += 1
    print(f"\nScore: {score}/{len(questions)}")
PYEOF

git add -A
git commit -m "Add quiz game with git questions"

# Teammate adds more questions (this commit exists on remote but not on student's local)
cat >> app.py << 'PYEOF'


def add_question(question_text, answer_text):
    """Add a new question to the quiz."""
    questions.append({"q": question_text, "a": answer_text})
PYEOF

git add app.py
git commit -m "Add function to dynamically add quiz questions"
git push origin main
cd ..

# Now create the student's local repo (clone from same remote)
git clone remote-repo.git student-local
cd student-local
git config user.email "student@exercise.local"
git config user.name "Exercise Student"

# Reset student's local to BEFORE teammate's second commit
git reset --hard HEAD~1

# Student makes their own changes (diverging from remote)
cat > scoring.py << 'PYEOF'
"""Scoring module for the quiz game."""


def calculate_percentage(correct, total):
    """Calculate score as a percentage."""
    if total == 0:
        return 0
    return round((correct / total) * 100, 1)


def grade(percentage):
    """Return a letter grade based on percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
PYEOF

git add scoring.py
git commit -m "Add scoring module with percentage and grades"

echo ""
echo "=== Scenario C: Push Rejected Created ==="
echo "Enter '$WORKSPACE/student-local' and try 'git push origin main'."
echo "It will be REJECTED because the remote has commits you don't have."
echo ""
echo "Your task:"
echo "  1. Understand WHY the push was rejected (git log vs remote)"
echo "  2. Pull the remote changes (git pull --rebase or git pull)"
echo "  3. Resolve any conflicts if they arise"
echo "  4. Push successfully"
echo ""

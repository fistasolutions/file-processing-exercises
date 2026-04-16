# Exercise 1.1 — Project Kickoff

**Build: Repository initialization** — Transform a raw project folder into a well-structured Git repository

## Goal

Take the `weather-tracker/` project (which has no Git history) and initialize a clean, professional repository with proper `.gitignore` patterns, selective staging, and meaningful commit messages.

## What You Have

```
weather-tracker/
├── data/
│   └── sample-readings.csv    # 36 rows of weather station data
├── src/
│   ├── app.py                 # Weather data reader (~50 lines)
│   └── config.json            # Contains FAKE API key and database password
└── notes/
    └── todo.txt               # Personal notes and reminders
```

**Important:** `config.json` contains secrets (fake ones for this exercise). Your `.gitignore` must prevent these from being committed. The `notes/` folder contains personal files that shouldn't be in the repository.

## Your Tasks

### Step 1: Assess the Project

Before touching Git, understand what you have:

```bash
cd weather-tracker
ls -R
cat src/config.json    # Notice the secrets!
cat notes/todo.txt     # Personal notes — shouldn't be in git
```

Ask yourself: Which files belong in the repository? Which don't?

### Step 2: Initialize the Repository

```bash
git init
git status
```

Notice how `git status` shows ALL files as untracked. You need to be selective about what gets committed.

### Step 3: Create a .gitignore BEFORE Your First Commit

This is critical — create `.gitignore` FIRST so secrets never enter git history:

```bash
# Create .gitignore with patterns for this project
```

Your `.gitignore` should exclude:
- `src/config.json` (contains secrets)
- `notes/` directory (personal files)
- `__pycache__/` and `*.pyc` (Python bytecode)
- `.env` files (environment variables)

**Use Claude Code:** Ask it to help you write a `.gitignore` for a Python project that has secrets in `src/config.json`.

### Step 4: Create a Config Template

Since `config.json` is gitignored, create a template so other developers know the format:

```bash
# Create src/config.template.json with the structure but no real values
```

### Step 5: Stage Selectively and Commit

Don't use `git add .` — stage files intentionally:

```bash
git add .gitignore
git status                    # Verify only .gitignore is staged
git commit -m "Add .gitignore to protect secrets and personal files"

git add data/sample-readings.csv
git add src/app.py
git status                    # Verify the right files are staged
git commit -m "Add weather data reader with sample station data"

git add src/config.template.json
git commit -m "Add config template (actual config excluded for security)"
```

### Step 6: Verify Your Repository

```bash
git log --oneline             # Should show 3 clean commits
git status                    # Should be clean
git ls-files                  # Should NOT include config.json or notes/
```

## Verification

Run these commands to verify success:

```bash
# Should show 3 commits with descriptive messages
git log --oneline

# Should show clean working tree
git status

# config.json should NOT appear in tracked files
git ls-files | grep config.json
# (should return nothing)

# notes/ should NOT appear in tracked files
git ls-files | grep notes
# (should return nothing)

# .gitignore should be tracked
git ls-files | grep .gitignore
# (should show .gitignore)
```

## Reflection

1. What would have happened if you ran `git add .` before creating `.gitignore`? Why is the order important?
2. Why create a `config.template.json` instead of just documenting the format in the README?
3. Look at your commit messages. Could a teammate understand what each commit does without reading the code? If not, how would you improve them?

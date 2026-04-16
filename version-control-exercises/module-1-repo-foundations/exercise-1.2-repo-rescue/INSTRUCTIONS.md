# Exercise 1.2 — Repo Rescue

**Debug: Repository hygiene** — Diagnose and fix a colleague's messy repository

## Goal

A colleague's project has multiple problems: secrets committed to the repository, terrible commit messages, no `.gitignore`, and config files with exposed credentials. Your job is to assess the damage and fix what you can.

## What You Have

```
broken-project/
├── src/
│   ├── main.py               # Inventory management script
│   └── helpers.py             # Utility functions
├── config.json                # Contains FAKE-api-key-for-exercise
├── .env                       # Contains FAKE secrets — committed!
└── commit-log.txt             # Shows the terrible commit history
```

**The problems:**
1. `.env` file with secrets is committed (and in git history)
2. `config.json` has an API key committed
3. `commit-log.txt` shows meaningless commit messages ("fix", "stuff", "asdf")
4. No `.gitignore` exists at all

## Your Tasks

### Step 1: Assess the Damage

First, understand what's wrong:

```bash
cd broken-project
cat .env                       # Secrets in plain text!
cat config.json                # API key exposed!
cat commit-log.txt             # Useless commit history
ls -la                         # No .gitignore
```

Write a brief damage report. What are the risks of each problem?

### Step 2: Initialize Git and Simulate the Bad History

Since this is a starter exercise (not an actual git repo), first create the bad state:

```bash
git init
git config user.email "student@exercise.local"
git config user.name "Exercise Student"
git add -A
git commit -m "fix"
```

Now you have a repo where secrets are in the first commit. This is realistic — many real projects have this exact problem.

### Step 3: Create the .gitignore

```bash
# Create .gitignore that prevents future secret commits
```

Your `.gitignore` should cover:
- `.env` files
- Any file with "secret", "credential", or "key" in the name
- `__pycache__/` and `*.pyc`
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)

### Step 4: Remove Secrets from Tracking

Even after adding `.gitignore`, files already tracked stay tracked. Remove them:

```bash
git rm --cached .env
git rm --cached config.json
git status                    # Should show both as "deleted" in staging
```

### Step 5: Create Safe Replacements

```bash
# Create .env.example with placeholder values
# Create config.template.json with placeholder values
```

### Step 6: Commit the Fixes

```bash
git add .gitignore .env.example config.template.json
git add -u                    # Stage the removals
git commit -m "Remove committed secrets and add .gitignore

- Remove .env and config.json from tracking
- Add .gitignore to prevent future secret commits
- Add .env.example and config.template.json as safe templates"
```

### Step 7: Verify Secrets Are No Longer Tracked

```bash
git ls-files                  # .env and config.json should NOT appear
git status                    # Should show clean working tree
```

**Important note:** The secrets are still in the git history (first commit). In a real project, you'd need to use `git filter-branch` or BFG Repo Cleaner to remove them from history entirely. For this exercise, being aware of this limitation is sufficient.

## Verification

```bash
# .env should NOT be tracked
git ls-files | grep ".env"
# (should return nothing, or only .env.example)

# config.json should NOT be tracked
git ls-files | grep "config.json"
# (should return nothing, or only config.template.json)

# .gitignore should be tracked
git ls-files | grep ".gitignore"
# (should show .gitignore)

# Commit messages should be meaningful
git log --oneline
# Should show improvement over "fix", "stuff", "asdf"
```

## Reflection

1. The secrets are still in the git history even after removing them from tracking. Why is this a problem? What would you do in a real project?
2. Look at the `commit-log.txt` file. For each bad message ("fix", "stuff", "asdf"), write what a GOOD commit message would have been.
3. If you pushed this repo to GitHub before adding the `.gitignore`, could you "un-push" the secrets? What would you need to do?

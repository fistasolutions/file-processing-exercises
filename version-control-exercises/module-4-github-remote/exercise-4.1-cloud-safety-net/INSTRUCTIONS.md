# Exercise 4.1 — Cloud Safety Net

**Build: GitHub backup workflow** — Push a local project to GitHub with proper secret protection and verify the backup works

## Goal

Take the `portfolio-project/` website, push it to a new GitHub repository with proper `.gitignore` protection for secrets, verify the backup by cloning to a separate folder, and establish the push-verify-pull cycle.

## What You Have

```
portfolio-project/
├── index.html         # Portfolio website (~70 lines)
├── style.css          # Styles (~120 lines)
├── script.js          # Interactive behaviors (~35 lines)
├── .env.example       # Template showing what env vars are needed
└── secrets.json       # FAKE tokens — must be gitignored!
```

**Note:** `secrets.json` contains fake credentials. In a real project, these would be real. Your `.gitignore` MUST prevent this file from ever reaching GitHub.

## Your Tasks

### Step 1: Initialize and Protect

```bash
cd portfolio-project
git init
```

Create `.gitignore` BEFORE staging anything:

```
# Secrets — never commit
secrets.json
.env

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
```

```bash
git add .gitignore
git commit -m "Add .gitignore to protect secrets"

git add index.html style.css script.js .env.example
git commit -m "Add portfolio website with HTML, CSS, and JavaScript"
```

### Step 2: Create a GitHub Repository

Using the GitHub CLI (or GitHub web interface):

```bash
# Option A: Using GitHub CLI
gh repo create my-portfolio --public --source=. --push

# Option B: Manual steps
# 1. Go to github.com/new
# 2. Create repo named "my-portfolio" (public, no README)
# 3. Copy the remote URL
# 4. Run:
git remote add origin https://github.com/YOUR-USERNAME/my-portfolio.git
git push -u origin main
```

### Step 3: Verify on GitHub

```bash
# Check what GitHub has
gh repo view --web          # Opens in browser
# OR
gh api repos/YOUR-USERNAME/my-portfolio --jq '.name, .visibility'
```

**Critical check:** Go to your repo on GitHub and verify that `secrets.json` is NOT there.

### Step 4: Test the Backup — Clone to a New Folder

The whole point of pushing to GitHub is backup. Verify it works:

```bash
cd /tmp
git clone https://github.com/YOUR-USERNAME/my-portfolio.git portfolio-backup
cd portfolio-backup
ls -la                       # Should have all files EXCEPT secrets.json
```

### Step 5: Establish the Push-Verify Cycle

Go back to your original project and make a change:

```bash
cd /path/to/portfolio-project
# Edit index.html — add a new project card or update your name
git add index.html
git commit -m "Update portfolio with new project listing"
git push
```

Verify the change arrived:
```bash
cd /tmp/portfolio-backup
git pull
# The change should appear
```

## Verification

```bash
# Remote should be configured
git remote -v

# secrets.json should NOT be on GitHub
gh api repos/YOUR-USERNAME/my-portfolio/contents/ --jq '.[].name' | grep secrets
# (should return nothing)

# Local and remote should be in sync
git status
# Should show "Your branch is up to date with 'origin/main'"
```

## Reflection

1. If you accidentally pushed `secrets.json` to GitHub, what would you need to do? (Hint: just deleting it in a new commit is NOT enough.)
2. What's the difference between `git push -u origin main` (first push) and `git push` (subsequent pushes)?
3. Why did we clone to `/tmp` to test the backup? Could you test without cloning?

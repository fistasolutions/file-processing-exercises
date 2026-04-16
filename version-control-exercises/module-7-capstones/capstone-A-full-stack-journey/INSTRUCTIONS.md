# Capstone A — Full Stack Git Journey

**Complete lifecycle:** Empty folder to professional GitHub repository with branches, PRs, and workflow documentation

## Goal

Execute the complete Git lifecycle in one project: initialize, structure commits, create feature branches, merge with review, push to GitHub, create a PR with AI documentation, and write a workflow document. This capstone integrates everything from Modules 1-6.

## Estimated Time: 2-4 hours

## The Project

Build a **Contact Manager** — a Python command-line app that stores contacts (name, email, phone, notes). Simple enough to build in an afternoon, complex enough to exercise every Git workflow.

## Phase 1: Repository Foundation (Module 1 Skills)

### Step 1: Initialize
```bash
mkdir contact-manager && cd contact-manager
git init
```

### Step 2: Create .gitignore FIRST
Include patterns for: Python files, environment files, OS files, editor files, and any config files with secrets.

### Step 3: Create the initial structure
Ask Claude Code to create a basic contact manager with:
- `contacts.py` — Core logic (add, remove, search, list contacts)
- `storage.py` — JSON file storage
- `contacts.json` — Sample data (5-8 contacts)
- `config.json` — App config (gitignored, create a template instead)

### Step 4: Stage selectively and commit
```bash
git add .gitignore
git commit -m "Add .gitignore for Python project"

git add contacts.py storage.py contacts.json
git commit -m "Add contact manager with JSON storage and sample data"

git add config.template.json
git commit -m "Add config template (actual config excluded for security)"
```

## Phase 2: Feature Development with Branches (Module 3 Skills)

### Step 5: Feature branch — Search functionality
```bash
git checkout -b feature/search
```
Ask Claude Code to add search by name, email, or phone. Review with `git diff` before committing.

### Step 6: Feature branch — Export to CSV
```bash
git checkout main
git checkout -b feature/export
```
Ask Claude Code to add CSV export. Review and commit.

### Step 7: Merge features
```bash
git checkout main
git merge feature/search
git merge feature/export
git branch -d feature/search feature/export
```

## Phase 3: Change Review & Recovery (Module 2 Skills)

### Step 8: Intentional recovery practice
Ask Claude Code to make a risky change:
> "Refactor the entire storage layer to use SQLite instead of JSON"

Review with `git diff`. If the change is too aggressive, practice recovery:
```bash
git stash          # Save the changes
# Test without them
git stash pop      # Bring them back
# Or git stash drop to discard
```

## Phase 4: GitHub Push (Module 4 Skills)

### Step 9: Push to GitHub
```bash
gh repo create contact-manager --public --source=. --push
```

### Step 10: Verify backup
```bash
cd /tmp && git clone YOUR_REPO_URL && cd contact-manager
ls -la    # Verify all files present, no secrets
```

## Phase 5: Pull Request (Module 5 Skills)

### Step 11: Create a PR with AI transparency
```bash
git checkout -b feature/import-csv
```
Ask Claude Code to add CSV import functionality. Push and create PR:
```bash
git push -u origin feature/import-csv
gh pr create --title "Add CSV import functionality" --body "..."
```

The PR description MUST include the AI transparency template from Exercise 5.1.

## Phase 6: Workflow Documentation (Module 6 Skills)

### Step 12: Document your workflow
Create `CONTRIBUTING.md` in the repository with:
- How to set up the project
- Branching strategy
- Commit message conventions
- PR requirements including AI disclosure
- Your personal workflow for AI-assisted development

## Deliverables Checklist

- [ ] Git repository with 8+ meaningful commits
- [ ] At least 2 merged feature branches (visible in `git log --graph`)
- [ ] `.gitignore` protecting secrets (no config.json in tracked files)
- [ ] GitHub repository with clean push
- [ ] At least 1 PR with AI transparency documentation
- [ ] `CONTRIBUTING.md` with workflow documentation
- [ ] No secrets in any commit (`git log -p | grep FAKE` should find nothing in tracked files)

## Verification

```bash
git log --oneline --graph           # 8+ commits, merge points visible
git ls-files | grep -v config.json  # No secrets tracked
git remote -v                       # GitHub remote configured
cat CONTRIBUTING.md                 # Workflow doc exists
```

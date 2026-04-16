# Exercise 3.2 — Branch Tangle

**Debug: Branch archaeology** — Untangle a repository where commits ended up on wrong branches, code is orphaned, and merge conflicts exist

## Goal

A URL shortener project has three problems: a commit was made on the wrong branch, a useful branch was never merged (orphaned), and two feature branches conflict with each other. Use `setup.sh` to create the mess, then untangle it.

## What You Have

```
tangled-repo/
├── setup.sh              # Creates the tangled repository
└── expected-state.md     # Describes what clean state looks like
```

## Your Tasks

### Step 1: Create the Mess

```bash
cd tangled-repo
chmod +x setup.sh
bash setup.sh
cd tangled-repo-workspace
```

### Step 2: Map the Situation

Before fixing anything, understand the full picture:

```bash
git branch -a                          # List all branches
git log --all --oneline --graph        # Visualize the full history
```

For each branch, check what it contains:
```bash
git log main --oneline
git log feature-analytics --oneline
git log feature-storage --oneline
git log orphan-utils --oneline
```

**Draw a map** (on paper or in a text file) of:
- What commits are on which branches
- Which commit is on the WRONG branch
- What code exists on orphan-utils that main doesn't have

### Step 3: Fix Problem 1 — Commit on Wrong Branch

The `feature-analytics` branch has a storage-related commit that belongs on `feature-storage`. You need to:

1. Identify the misplaced commit: `git log feature-analytics --oneline`
2. Note the commit hash of "Switch to JSON file storage (WRONG BRANCH...)"
3. Cherry-pick it to the correct branch (or just note it — the storage branch already has its own implementation)

### Step 4: Fix Problem 2 — Merge the Orphan

The `orphan-utils` branch has useful code (URL validation) that nobody merged:

```bash
git checkout main
git merge orphan-utils -m "Merge URL utility functions from orphan-utils"
```

### Step 5: Fix Problem 3 — Resolve the Conflict

Now merge the feature branches. Start with analytics (but skip the misplaced storage commit):

```bash
git merge feature-analytics
```

Then merge the storage branch (this will likely conflict on `storage.py`):

```bash
git merge feature-storage
```

When the conflict appears:
```bash
git status                    # See conflicted files
cat storage.py                # See the conflict markers
```

Choose which storage implementation to keep (JSON or SQLite), edit the file to resolve the conflict, then:
```bash
git add storage.py
git commit -m "Merge SQLite storage, resolve conflict with analytics branch storage"
```

### Step 6: Verify Clean State

Compare your result with `expected-state.md`:

```bash
ls *.py                       # Should have app.py, storage.py, analytics.py, utils.py
git log --oneline --graph     # Should show clean merge history
git branch                    # Clean up feature branches if done
```

## Verification

```bash
# All four Python files should exist
ls app.py storage.py analytics.py utils.py

# Git log should show clean merges
git log --oneline --graph

# No unresolved conflicts
grep -r "<<<<<<" *.py
# (should return nothing)
```

## Reflection

1. What is `git cherry-pick` and when would you use it instead of `git merge`?
2. When you encountered the merge conflict, how did you decide which version to keep? What factors matter?
3. The "orphan-utils" branch was never merged. In a real project, how would you prevent useful branches from being forgotten?

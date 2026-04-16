# Exercise 4.2 — Remote Troubles

**Debug: Remote configuration problems** — Fix three common issues with GitHub remote setup

## Goal

Work through three scenarios, each with a different remote configuration problem. Each has a `setup.sh` that creates a local repo with the problem. Fix each one.

## What You Have

```
remote-scenarios/
├── scenario-A-branch-mismatch/
│   └── setup.sh              # Local uses "master", GitHub expects "main"
├── scenario-B-wrong-remote/
│   └── setup.sh              # Remote URL points to non-existent repo
└── scenario-C-push-rejected/
    └── setup.sh              # Remote has commits local doesn't have
```

## Your Tasks

### Scenario A: Branch Name Mismatch

**Problem:** Your local repo uses `master` (old convention) but GitHub defaults to `main`.

```bash
cd scenario-A-branch-mismatch
chmod +x setup.sh
bash setup.sh
cd branch-mismatch-repo
```

Diagnose:
```bash
git branch                    # Shows "master" — not what GitHub expects
```

Fix:
```bash
git branch -m master main     # Rename the branch
git branch                    # Verify it's now "main"
```

After renaming, if you had a remote, you'd need:
```bash
# git push origin -u main      # Push the renamed branch
# git push origin --delete master  # Delete old "master" on remote
```

### Scenario B: Wrong Remote URL

**Problem:** Someone set up the remote URLs incorrectly.

```bash
cd scenario-B-wrong-remote
chmod +x setup.sh
bash setup.sh
cd wrong-remote-repo
```

Diagnose:
```bash
git remote -v                 # Shows wrong URLs
```

Fix:
```bash
# Fix the origin URL (use your actual GitHub repo URL)
git remote set-url origin https://github.com/YOUR-USERNAME/budget-tracker.git

# Remove the wrong upstream
git remote remove upstream

# Verify
git remote -v
```

### Scenario C: Push Rejected

**Problem:** Someone else pushed to the remote, and now your push is rejected.

```bash
cd scenario-C-push-rejected
chmod +x setup.sh
bash setup.sh
cd push-rejected-workspace/student-local
```

Diagnose:
```bash
git push origin main          # REJECTED! Why?
git log --oneline             # Your commits
git log --oneline origin/main # Remote's commits (may need fetch first)
git fetch origin
git log --oneline --all       # See both histories
```

Fix (Option A — Merge):
```bash
git pull origin main          # Fetches remote changes and merges
# Resolve conflicts if any
git push origin main          # Now it works
```

Fix (Option B — Rebase, cleaner history):
```bash
git pull --rebase origin main # Replay your commits on top of remote
git push origin main          # Clean linear history
```

## Verification

**Scenario A:**
```bash
git branch                    # Should show "main", not "master"
```

**Scenario B:**
```bash
git remote -v                 # Should show correct URLs, no "upstream"
```

**Scenario C:**
```bash
git log --oneline --all       # Should show both sets of commits
# Push should succeed (if remote is real)
```

## Reflection

1. Why did GitHub switch from "master" to "main" as the default branch name? How do you configure Git to use "main" for all new repos? (Hint: `git config`)
2. In Scenario C, what's the difference between `git pull` (merge) and `git pull --rebase`? When would you prefer one over the other?
3. If `git push` is rejected, why is `git push --force` almost never the right answer?

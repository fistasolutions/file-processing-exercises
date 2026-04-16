# Expected Clean State

After untangling the branches, the repository should look like this:

## Branch Structure

```
main
├── app.py          — Original + stats function
├── storage.py      — ONE chosen storage backend (SQLite OR JSON, not both)
├── analytics.py    — Click tracking module (from feature-analytics)
└── utils.py        — URL validation utilities (from orphan-utils)
```

## What "Clean" Means

1. **main** contains all features merged properly
2. **feature-analytics** has ONLY analytics-related commits (the storage commit is removed or cherry-picked away)
3. **feature-storage** has the chosen storage backend
4. **orphan-utils** code is merged into main
5. No merge conflicts remain
6. `git log --oneline --graph` shows a clean, understandable history

## Steps to Get There (Hints)

1. Cherry-pick the storage commit from feature-analytics to feature-storage (or just note it's misplaced)
2. Decide: JSON storage or SQLite storage? Pick one.
3. Merge feature-analytics into main (minus the storage commit)
4. Merge your chosen storage branch into main (resolve conflicts)
5. Merge orphan-utils into main
6. Verify everything works together
7. Clean up: delete merged feature branches

## Verification Commands

```bash
# Should show only main (feature branches deleted after merge)
git branch

# Should show clean merge history
git log --oneline --graph

# All four files should exist
ls app.py storage.py analytics.py utils.py
```

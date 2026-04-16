# Exercise 2.2 — Recovery Room

**Debug: Git recovery techniques** — Practice recovering from three common mistakes

## Goal

Work through three scenarios, each representing a common Git mistake. Each scenario has a `setup.sh` script that creates the broken state. Your job is to diagnose and fix each one using the appropriate recovery command.

## What You Have

```
recovery-scenarios/
├── scenario-A-unstaged-mess/
│   ├── README.md              # Describes the problem
│   └── setup.sh               # Creates the broken state
├── scenario-B-staging-mistake/
│   ├── README.md              # Describes the problem
│   └── setup.sh               # Creates the broken state
└── scenario-C-bad-commit/
    ├── README.md              # Describes the problem
    └── setup.sh               # Creates the broken state
```

## Your Tasks

### Scenario A: The Unstaged Mess

**Problem:** AI modified 4 files without committing. Some changes are good, some are bad.

```bash
cd scenario-A-unstaged-mess
chmod +x setup.sh
bash setup.sh
cd unstaged-mess-repo
```

**Your recovery toolkit:**
- `git status` — See what's changed
- `git diff` — See exactly what changed in each file
- `git diff <file>` — See changes in a specific file
- `git restore <file>` — Discard all changes to a file
- `git add -p <file>` — Stage specific parts of a file (interactive)
- `git add <file>` — Stage all changes in a file

**Steps:**
1. Run `git diff` and read each file's changes carefully
2. `utils.py` — Good changes (better docstrings). Stage it: `git add utils.py`
3. `config.py` — Bad change (API key overwritten). Restore it: `git restore config.py`
4. `README.md` — Unwanted rewrite. Restore it: `git restore README.md`
5. `app.py` — Mixed (type hints good, search bug bad). Use `git add -p app.py`
6. Commit the good changes with a clear message

### Scenario B: The Staging Mistake

**Problem:** `git add .` staged everything, including files that shouldn't be committed.

```bash
cd scenario-B-staging-mistake
chmod +x setup.sh
bash setup.sh
cd staging-mistake-repo
```

**Your recovery toolkit:**
- `git status` — See what's staged
- `git restore --staged <file>` — Unstage a file (keep changes in working directory)
- `git reset HEAD <file>` — Alternative way to unstage (older syntax)

**Steps:**
1. Run `git status` to see everything that's staged
2. Unstage the files that shouldn't be committed:
   ```bash
   git restore --staged tests/test_api.py
   git restore --staged tests/test_models.py
   git restore --staged debug.log
   git restore --staged temp_credentials.txt
   ```
3. Verify with `git status` — only `src/` files should be staged
4. Commit the production code
5. Create a `.gitignore` to prevent this from happening again

### Scenario C: The Bad Commit

**Problem:** The latest commit broke everything. Need to undo it while preserving history.

```bash
cd scenario-C-bad-commit
chmod +x setup.sh
bash setup.sh
cd bad-commit-repo
```

**Your recovery toolkit:**
- `git log --oneline` — See commit history
- `git show HEAD` — See what the latest commit changed
- `git revert HEAD` — Create a new commit that undoes the latest
- `git diff HEAD~1..HEAD` — See what changed in the last commit

**Steps:**
1. Run `git log --oneline` — identify the bad commit
2. Run `git show HEAD` — see exactly what the "refactor" broke
3. Revert the bad commit: `git revert HEAD`
4. Verify: `git log --oneline` should show 4 commits (3 original + 1 revert)
5. Read `calculator.py` — it should have the input validation back

## Verification

For each scenario, verify your fix:

**Scenario A:**
```bash
git status          # Clean working tree
git log --oneline   # Shows your fix commit
cat config.py       # Should have original API key
cat README.md       # Should have original content
```

**Scenario B:**
```bash
git status          # Tests and logs are untracked, not staged
git log --oneline   # Shows production commit
cat .gitignore      # Should prevent future accidents
```

**Scenario C:**
```bash
git log --oneline   # Shows 4 commits including revert
python -c "from calculator import divide; divide(1, 0)"
# Should raise ValueError (validation restored), not ZeroDivisionError
```

## Reflection

1. What's the difference between `git restore` (unstaged changes), `git restore --staged` (staged changes), and `git revert` (committed changes)?
2. Why does `git revert` create a NEW commit instead of deleting the old one? When would this matter?
3. In Scenario A, you used `git add -p` for partial staging. When is this more useful than staging entire files?

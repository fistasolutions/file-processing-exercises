# Scenario A: The Unstaged Mess

## What Happened

You asked Claude Code to "improve the codebase" and it made changes across 4 files
without committing anything. Some changes are good, some are bad, and nothing is staged.

## Your Mission

1. Run `setup.sh` to create the broken state
2. Use `git status` and `git diff` to understand what changed
3. Identify which changes are good and which are bad
4. Use `git restore` to discard the bad changes
5. Stage and commit only the good changes

## The Broken State

After running setup.sh, you'll have:
- `app.py` — rewritten with some improvements and some bugs introduced
- `utils.py` — refactored (good changes)
- `config.py` — API key accidentally changed (bad!)
- `README.md` — rewritten in a completely different style (unwanted)

None of these changes are staged. Your job is to sort the good from the bad.

## Success Criteria

- `utils.py` changes are committed (they're improvements)
- `app.py` bugs are discarded, improvements kept (use partial staging with `git add -p`)
- `config.py` is restored to its original state
- `README.md` is restored to its original state
- Clean `git status` with a meaningful commit message

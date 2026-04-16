# Scenario B: The Staging Mistake

## What Happened

You're preparing a commit for your production code changes. You ran `git add .`
out of habit, but that accidentally staged test files, debug logs, and a file
with temporary passwords alongside your actual production changes.

## Your Mission

1. Run `setup.sh` to create the broken state
2. Use `git status` to see everything that's staged
3. Unstage the files that shouldn't be committed (test files, debug log, temp credentials)
4. Keep the production files staged
5. Commit only the production changes with a proper message

## The Broken State

After running setup.sh, the staging area will contain:
- `src/api.py` — production code (SHOULD be committed)
- `src/models.py` — production code (SHOULD be committed)
- `tests/test_api.py` — unfinished test (should NOT be committed yet)
- `tests/test_models.py` — unfinished test (should NOT be committed yet)
- `debug.log` — debug output (should NEVER be committed)
- `temp_credentials.txt` — temporary fake passwords (should NEVER be committed)

## Success Criteria

- Only `src/api.py` and `src/models.py` are committed
- Tests, debug.log, and temp_credentials.txt are unstaged
- A `.gitignore` is created to prevent future accidents with logs and credential files
- Clean commit with message explaining the production changes

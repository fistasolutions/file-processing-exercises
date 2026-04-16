# Scenario C: The Bad Commit

## What Happened

You committed a version of your code that breaks everything. The previous commit
was working perfectly. You need to undo the bad commit without losing the history
of what happened.

## Your Mission

1. Run `setup.sh` to create the broken state
2. Use `git log` to see the commit history
3. Identify the bad commit
4. Use `git revert` to undo the bad commit (NOT `git reset` — we want to keep the history)
5. Verify the code works again

## The Broken State

After running setup.sh, you'll have a repo with 3 commits:
- Commit 1: "Add calculator with basic operations" (working)
- Commit 2: "Add square root and power functions" (working)
- Commit 3: "Refactor all operations for performance" (BROKEN — introduced division by zero bug and removed input validation)

## Success Criteria

- The bad commit (Commit 3) is reverted using `git revert`
- The git history shows all 4 commits (3 original + 1 revert)
- The code from Commit 2 is restored and working
- You can explain WHY `git revert` is preferred over `git reset` for shared repos

# PR #63: Fix data export feature

**Author:** dev-student-3
**Branch:** fix-export -> main
**Files Changed:** 3 files changed, +89 lines, -34 lines
**CI Status:** FAILING (2 of 5 checks failed)

## Description

Fixed the data export feature that was broken after the database migration.
The export now correctly handles the new schema format.

## Changes

- `export.py`: Updated query to match new column names
- `formats.py`: Added CSV header mapping for renamed fields
- `test_export.py`: Updated test fixtures

## Failed Checks

```
FAIL test_export.py::test_large_export_performance
    AssertionError: Export took 12.3s, expected < 5.0s
    The performance test fails because the new query doesn't use the index.

FAIL lint::check_formatting
    export.py:45:1: E302 expected 2 blank lines before function
    export.py:67:80: E501 line too long (94 > 88 characters)
    formats.py:12:1: W291 trailing whitespace
```

## PR Comment Thread (Simulated)

> **dev-student-3**: "The lint errors are minor, I'll fix later. The performance test is flaky."

> **senior-dev**: "The performance test isn't flaky — it's telling you the query needs an index. Don't merge with failing checks."

> **tech-lead**: "Our policy is: all checks must pass before merge. No exceptions."

> **dev-student-3**: "But the export WORKS. Can we just skip the checks this once?"

> **senior-dev**: "No. Fix the lint issues (2 minutes), then address the performance problem (add the missing index). These are real problems, not noise."

---

## Your Task

This PR has real problems the author is trying to ignore. Write an improved approach:

1. Fix the lint issues (describe what you'd change — the exact lines)
2. Explain the performance problem (why is it slow without the index?)
3. Write a plan for fixing the performance issue
4. Rewrite the PR description acknowledging these issues and the fix plan
5. Explain WHY merging with failing checks is bad practice

Save your improved description as `pr-3-improved.md` in this directory.

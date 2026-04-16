# Incident Report: The Silent Breaking Change

**Date:** 2025-02-14
**Severity:** High
**Duration:** 6 hours before detection

## What Happened

Carol pushed a "small fix" (3 lines) directly to `main` without a PR, as
allowed by the workflow document for changes under 5 lines. The fix changed
the return type of `get_user()` from a dictionary to a User object.

Three other features being developed on branches relied on `get_user()`
returning a dictionary. When Alice, Bob, and Dave each merged their feature
branches to `main`, all three got unexpected errors that took hours to debug.

## Timeline

- 2:15 PM: Carol pushes 3-line change directly to main
- 2:30 PM: Alice merges feature-cart, tests pass on her branch
- 2:31 PM: Cart page crashes — `TypeError: 'User' object is not subscriptable`
- 3:00 PM: Alice spends 30 minutes debugging, finds Carol's change
- 3:45 PM: Bob merges feature-checkout, same error pattern
- 5:00 PM: Dave merges feature-profile, same error
- 8:15 PM: All three features fixed to use User object instead of dict

## Root Cause

The workflow allows direct pushes to main for "small" changes. But a 3-line
change to a return type is a breaking API change, regardless of line count.

## Questions

1. What workflow rule allowed this to happen?
2. How should the rule be changed to prevent this?
3. Would a PR have caught this? Why or why not?

# Incident Report: The Hotfix That Made Things Worse

**Date:** 2025-03-10
**Severity:** Critical
**Duration:** 12 hours of degraded service

## What Happened

A critical bug was discovered in the checkout flow — orders were being
double-charged. Alice followed the hotfix procedure in the workflow document:
branch from main, fix the issue, push directly to main (skip PR for speed).

Alice's fix resolved the double-charge bug but introduced a new bug: orders
under $10 were being silently dropped (not saved to the database). This
wasn't discovered until the next morning when a customer reported a missing order.

The fix for the fix then needed another hotfix, creating a chain of
untested direct-to-main pushes.

## Timeline

- Mar 10, 9:00 AM: Customer reports double-charge
- Mar 10, 9:30 AM: Alice confirms bug, starts hotfix
- Mar 10, 10:00 AM: Alice pushes fix directly to main (per hotfix procedure)
- Mar 10, 10:05 AM: Double-charge bug fixed, but new condition check drops small orders
- Mar 10, 10:00 PM: Customer reports missing $7.50 order
- Mar 11, 8:00 AM: Alice investigates, finds her fix introduced the new bug
- Mar 11, 9:00 AM: Second hotfix pushed directly to main
- Mar 11, 9:15 AM: Carol notices the second fix has a typo in variable name
- Mar 11, 9:30 AM: Third fix pushed to main

## Root Cause

The hotfix procedure explicitly says "skip PR for speed." But:
1. No tests were run before the direct push
2. No second pair of eyes saw the code
3. The "fix for the fix for the fix" pattern shows the procedure is broken
4. The workflow says "run tests before pushing" but also says "skip PR for hotfixes" — contradiction

## Questions

1. How did the hotfix procedure's "skip PR" rule conflict with the "run tests" rule?
2. What should a hotfix procedure actually look like?
3. How would you balance speed with safety for critical bugs?

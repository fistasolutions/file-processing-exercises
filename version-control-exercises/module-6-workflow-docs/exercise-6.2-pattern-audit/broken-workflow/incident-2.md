# Incident Report: The Unreviewed Merge

**Date:** 2025-03-01
**Severity:** Medium
**Duration:** 3 days before anyone noticed

## What Happened

Dave submitted a PR for the product search feature. It sat without review
for 48 hours. Following the workflow document's rule ("If no review after
48 hours, the author can merge without approval"), Dave merged it himself.

The PR contained 400+ lines of AI-generated code that Dave didn't fully
understand. Three days later, Bob discovered that the search feature was
making a database query for EVERY KEYSTROKE with no debouncing, causing
the database to slow down for all users.

## Timeline

- Feb 27, 10:00 AM: Dave creates PR #34 for search feature
- Feb 27 - Mar 1: No reviews (Alice busy, Bob on vacation, Carol missed it)
- Mar 1, 10:00 AM: Dave merges without review (following 48-hour rule)
- Mar 1 - Mar 4: Search feature live, database gradually slowing
- Mar 4, 3:00 PM: Bob returns, notices database performance alerts
- Mar 4, 5:00 PM: Root cause identified — no debouncing on search input
- Mar 4, 7:00 PM: Hotfix deployed

## Root Cause

Two workflow failures combined:
1. The 48-hour auto-merge rule allowed unreviewed code into main
2. AI-generated code wasn't flagged for extra review scrutiny
3. No AI disclosure in the PR description (workflow says "no special documentation needed")

## Questions

1. Should the 48-hour auto-merge rule exist at all?
2. What should happen when nobody reviews a PR?
3. How should the workflow handle AI-generated code review?

# Exercise 2.2 -- The Incomplete Backup

**Debug** -- Find and fix discrepancies between an original folder and its supposedly complete backup

## Goal

A colleague created a backup of `original/` into `backup/`. They said "everything is copied." You are about to delete the original to free up space. But before you do, you want to verify the backup is actually complete. Your job: compare the two directories, find every discrepancy, diagnose why each failure happened, and fix the backup.

## What You Have

- `original/` -- The source directory with 20 files across 3 subdirectories (the ground truth)
- `backup/` -- The supposed backup, which has at least 6 discrepancies

## Your Tasks

### Step 1: Compare Directory Structures

Use Claude Code to compare file counts, directory structures, and file names between `original/` and `backup/`.

### Step 2: Compare File Contents

For files that exist in both locations, compare sizes and contents. Look for truncated or corrupted files.

### Step 3: Check for Hidden Files

Verify that hidden files from the original are present in the backup.

### Step 4: Diagnose Each Discrepancy

For each difference you find, determine the likely cause:

- Missing file: Was it a hidden file? Permission issue? Interrupted copy?
- Wrong content: Truncated? Corrupted? Wrong version?
- Empty file: Permission denied during copy?

### Step 5: Fix the Backup

Copy the missing or corrupted files from `original/` to `backup/` to make the backup complete.

### Step 6: Create BACKUP-AUDIT.md

Document every discrepancy: what was wrong, likely cause, and how you fixed it.

## Expected Results

- A `BACKUP-AUDIT.md` documenting all 6 discrepancies with causes and fixes
- A `backup/` directory that now matches `original/` exactly
- Verification proof (diff output showing the directories now match)

## Reflection

1. Which discrepancy would have caused the most damage if you had deleted the original without checking?
2. What single command or approach would have prevented most of these backup failures?
3. Design a 5-step "backup verification checklist" that works for any backup operation.

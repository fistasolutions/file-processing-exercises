# Exercise 2.1 -- The Migration Prep

**Build** -- Create a verified, bulletproof backup before reorganizing a project folder

## Goal

You are about to reorganize `migration-source/` but it contains edge cases that will trip up a naive backup: hidden configuration files, a large data file, files in nested directories, and a spot where a symlink should exist. You need to create a timestamped backup that handles every edge case, verify it is complete, and document your strategy for reuse.

## What You Have

- `migration-source/` -- A folder with ~20 files including hidden files, a large CSV, and nested directories

## Setup (Do This First)

Before starting the exercise, create a symlink to simulate a shared config:

```bash
cd migration-source/config
ln -s ../reports/quarterly-summary.md shared-config-link.md
```

This simulates a real-world scenario where one file is actually a symlink to another.

## Your Tasks

### Step 1: Survey Before Backup

Use Claude Code to get a complete picture of `migration-source/`: file count (including hidden files), total size, directory depth, and any special files (symlinks, large files).

### Step 2: Create Timestamped Backup

Create a backup with a timestamp in the name (e.g., `migration-source-backup-YYYY-MM-DD-HHMM/`). Use a copy method that preserves hidden files and handles symlinks.

### Step 3: Verify Completeness

Compare the backup against the original:

- File counts match (including hidden files)
- Total sizes match
- Symlink is handled (either preserved or dereferenced -- document which)
- Large file copied completely (compare sizes)
- Hidden files are present in backup

### Step 4: Document Strategy

Create `BACKUP-STRATEGY.md` documenting:

- The exact commands you used
- How you handled each edge case
- Verification steps someone else could follow
- Estimated time for this backup approach

## Expected Results

- A timestamped backup directory that matches the original
- A `BACKUP-STRATEGY.md` that someone could follow to replicate the backup
- Verification evidence showing the backup is complete

## Reflection

1. What edge cases did you discover that a simple `cp -r` would have missed?
2. How did you verify the backup was complete? What specific comparisons did you run?
3. If this backup needed to be restored 6 months later by someone unfamiliar with the project, would your documentation be sufficient?

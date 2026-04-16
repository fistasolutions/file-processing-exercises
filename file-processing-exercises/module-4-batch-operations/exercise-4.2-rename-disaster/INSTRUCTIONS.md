# Exercise 4.2 -- The Rename Disaster

**Debug** -- Diagnose and recover from a botched batch rename operation

## Goal

Someone ran a batch rename script on `mangled-files/` and it went wrong. Files have impossible dates, doubled prefixes, stripped extensions, and some files were overwritten because they got renamed to the same name. The `rename-log.txt` shows what the script did. Your job: read the log, diagnose each bug, recover what you can, and write a post-mortem.

## What You Have

- `mangled-files/` -- 30 files in their current mangled state (after the bad rename)
- `rename-log.txt` -- A log showing every rename operation the script performed, including errors

## Your Tasks

### Step 1: Read the Rename Log

Study `rename-log.txt` to understand what the script intended to do and what went wrong.

### Step 2: Categorize the Bugs

Identify each distinct type of bug: wrong date parsing, double date prefix, extension stripping, name collision/overwrite, etc.

### Step 3: Identify Recoverable vs. Lost Files

Determine which files can be recovered (renamed back to their correct name) and which are permanently lost (overwritten by another file).

### Step 4: Write a Recovery Script

Create a plan or script to undo the recoverable damage, restoring correct filenames where possible.

### Step 5: Write POST-MORTEM.md

Document: what happened, each bug and its root cause, which files were lost, and safeguards to prevent this in the future.

## Expected Results

- A `POST-MORTEM.md` documenting all bugs, root causes, and prevention measures
- A recovery plan or script for undoing the damage
- Clear identification of which files are recoverable and which are permanently lost

## Reflection

1. Which bug caused the most damage? Why?
2. What three safeguards would you add to any batch rename script?
3. Design a log format that captures enough information for complete rollback.

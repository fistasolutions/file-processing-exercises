# Exercise 1.2 -- The Lying Inventory

**Debug** -- Find every error in an outdated inventory report by comparing it against actual files

## Goal

A previous team member left an inventory report (`wrong-inventory.md`) that documents the contents of the `actual-files/` folder. Management relies on this report for storage planning and project decisions. Your job is to compare the report against reality and find every single discrepancy. This exercise builds the critical skill of verifying documentation against actual state.

## What You Have

- `actual-files/` -- A folder with files across several subdirectories (the ground truth)
- `wrong-inventory.md` -- An inventory report with at least 6 specific errors

## Your Tasks

### Step 1: Read the Inventory Report
Read `wrong-inventory.md` carefully. Note every claim it makes: file counts, directory contents, total size, nesting depth, hidden files.

### Step 2: Survey the Actual Files
Use Claude Code to thoroughly survey `actual-files/`. Get exact file counts (including hidden files), directory structure, file sizes, and nesting depth.

### Step 3: Compare Claim by Claim
Go through each claim in the inventory report and verify it against reality. For each claim, determine: is it accurate, inaccurate, or partially correct?

### Step 4: Create DISCREPANCY-REPORT.md
Document every error you find. For each error, include:
- What the report claims
- What is actually true
- How you verified it (the command you ran)

## Expected Results

A `DISCREPANCY-REPORT.md` that identifies at least 6 specific errors in the inventory report, with verification evidence for each. The report should be structured so someone could read it and immediately understand what is wrong with the original inventory.

## Reflection

1. How many errors did you find? Were any of them the kind that could cause real problems if management relied on them?
2. What process would prevent inventory reports from becoming stale? Is manual maintenance realistic?
3. Could you write a command or script that generates an accurate inventory automatically? What would it need to check?

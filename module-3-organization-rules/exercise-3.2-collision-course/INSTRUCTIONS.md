# Exercise 3.2 -- The Collision Course

**Debug** -- Find and fix conflicts, gaps, and ambiguities in a set of file organization rules

## Goal

Someone wrote `broken-rules.md` for organizing the files in `unsorted-files/`. The rules look reasonable at first glance, but they contain overlapping categories, missing file types, case sensitivity issues, and conflicting instructions. If someone followed these rules literally, files would end up in multiple folders or have no destination at all. Your job: audit the rules, fix every problem, and prove your fixes work.

## What You Have

- `unsorted-files/` -- 30 files to be organized (similar to the freelancer files, but a smaller set)
- `broken-rules.md` -- Organization rules with at least 8 specific problems

## Your Tasks

### Step 1: Read the Rules Carefully

Read `broken-rules.md` and identify every conflict, gap, and ambiguity.

### Step 2: Create RULE-AUDIT.md

Document each problem you found: what the rule says, why it is broken, and the principle it violates (mutual exclusivity, completeness, clarity, etc.).

### Step 3: Write fixed-rules.md

Create a corrected version of the rules. Every rule should be unambiguous, and the complete set should handle every file type in `unsorted-files/` with no overlaps and a clear fallback.

### Step 4: Test Against Real Files

Apply your fixed rules to `unsorted-files/` and verify every file has exactly one destination.

## Expected Results

- A `RULE-AUDIT.md` documenting all problems found (at least 8)
- A `fixed-rules.md` with corrected, complete, unambiguous rules
- Evidence that the fixed rules work on the actual files (no file left behind, no file in two places)

## Reflection

1. How many distinct problems did you find? Categorize them: conflicts, gaps, ambiguities, and other.
2. What minimum set of principles prevents these kinds of rule failures?
3. Could you write a "rule validation checklist" for auditing ANY set of organization rules?

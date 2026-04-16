# Exercise 1.1 -- The Project Handoff

**Build** -- Survey an inherited project folder and create a complete file inventory

## Goal

You have just inherited a project folder from a departing colleague. Before you touch a single file, you need to know exactly what is in this folder: how many files, what types, how big, how deeply nested, and whether anything looks suspicious (credentials, stale backups, temp files). Your deliverable is a FILE-INVENTORY.md that serves as your reference map for this project.

## What You Have

- `messy-project/` -- A project folder with 40+ files across nested directories: source code, tests, configuration, documentation, deployment scripts, image assets, data files, and scattered notes. No README. No documentation. No handoff notes.

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Initial Survey
Ask Claude Code to survey the entire `messy-project/` directory tree. Get a count of all files (including hidden ones), the directory structure, and nesting depth.

### Step 3: File Type Breakdown
Get a breakdown of file types: how many `.py`, `.md`, `.yml`, `.csv`, `.json`, `.txt`, `.sh`, and other extensions exist.

### Step 4: Size Analysis
Find the total size of the folder, the 5 largest files, and the average file size.

### Step 5: Suspicious File Detection
Identify files that might contain secrets (`.env` files, files with "key" or "token" in the name), backup files (`.bak`), temp files, and files that look stale or unused.

### Step 6: Create FILE-INVENTORY.md
Compile everything into a structured FILE-INVENTORY.md document in this exercise folder. Include: total count, type breakdown, size analysis, directory tree, suspicious files, and recommendations for cleanup.

## Expected Results

A `FILE-INVENTORY.md` file that someone could read to understand this project's file structure without looking at the folder themselves. It should include:
- Exact file count (including hidden files)
- File type breakdown with counts
- Total size and top 5 largest files
- Directory tree with depth annotation
- List of suspicious/notable files with explanations
- At least 3 recommendations for project cleanup

## Reflection

1. What did you discover in the survey that would have surprised you if you had started editing files immediately?
2. Compare running a vague prompt ("look at this folder") vs. a specific prompt (listing exactly what to survey). What did the specific version catch?
3. How long did this inventory take? Would you skip this step on a real project? Why or why not?

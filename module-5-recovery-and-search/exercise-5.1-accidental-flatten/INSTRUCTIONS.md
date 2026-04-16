# Exercise 5.1 -- The Accidental Flatten

**Build** -- Reconstruct a nested directory structure from a flattened folder using a backup as reference

## Goal

Someone ran a command that moved ALL files from a nested directory structure into a single `flattened/` folder. Four levels of carefully organized nesting are gone. Files that had the same name in different directories (like `__init__.py`) now have numbers appended. Luckily, `backup/` preserves the original structure. Your job: reconstruct.

## What You Have

- `flattened/` -- All files from the project dumped into a single flat directory, with numbered suffixes for name collisions
- `backup/` -- The original nested directory structure (your reference for reconstruction)

## Your Tasks

### Step 1: Survey the Damage

Count files in `flattened/`. Identify files with numbered suffixes (`__init__ (1).py`, etc.) that indicate name collisions.

### Step 2: Study the Original Structure

Map the directory tree from `backup/`. Understand where each file originally lived.

### Step 3: Plan Reconstruction

For each file in `flattened/`, determine its correct destination based on the backup. Pay special attention to the numbered duplicates -- you need to figure out which `__init__` goes where.

### Step 4: Execute Reconstruction

Recreate the directory structure and move each file to its correct location.

### Step 5: Verify

Compare your reconstructed structure against `backup/`. They should match exactly -- same files, same directories, same nesting.

## Expected Results

- A reconstructed directory that matches `backup/` exactly
- Documentation of how you resolved the `__init__.py` collision (which numbered file went where)
- Verification proof (diff or comparison showing the structures match)

## Reflection

1. How did you determine which `__init__ (1).py` belonged in which directory?
2. What would you do if there were no backup at all? What clues in the files might help?
3. What command likely caused the original flattening, and how would you prevent it?

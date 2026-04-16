# Exercise 4.1 -- Photo Library Cleanup

**Build** -- Standardize naming across 50+ photos with inconsistent naming conventions

## Goal

Your `photo-dump/` folder has 50+ photos and screenshots with wildly inconsistent names: camera defaults, screenshot timestamps, descriptive names, and files with no useful name at all. You want every file named with a consistent format. Your job is to survey the naming patterns, design a convention, preview the changes, execute the batch rename, and save a reusable script.

## What You Have

- `photo-dump/` -- 50+ image files with various naming patterns: `IMG_YYYYMMDD_HHMMSS.jpg`, `Screenshot YYYY-MM-DD at HH.MM.SS.png`, `DCIM_NNN.jpg`, `unnamed.jpg`, `unnamed (1).jpg`, descriptive names, and more.

## Your Tasks

### Step 1: Survey Naming Patterns

Catalog the different naming formats in the folder. How many distinct patterns exist?

### Step 2: Design Naming Convention

Define your target format (e.g., `YYYY-MM-DD_description.ext`). Create rules for:

- Extracting dates from different source formats
- Handling files with no date in the name
- Resolving name collisions (two files that would get the same name)
- Handling files with wrong or missing extensions

### Step 3: Preview Changes

Generate a rename plan showing every OLD NAME -> NEW NAME WITHOUT executing any renames. Review the plan for problems.

### Step 4: Execute Batch Rename

Run the batch rename operation.

### Step 5: Handle Edge Cases

Address any files that your initial plan could not handle: no-date files, duplicates, wrong extensions.

### Step 6: Verify and Document

Confirm all files renamed correctly (same count, no overwrites). Save a reusable rename template or script.

## Expected Results

- All 50+ files renamed with a consistent convention
- A rename log showing old name -> new name for every file
- A reusable rename script or template
- No files lost or overwritten

## Reflection

1. How many different naming formats existed in the original files? Which was hardest to parse?
2. What edge cases did your initial plan not account for?
3. Would your rename script work on a new batch of photos without modification?

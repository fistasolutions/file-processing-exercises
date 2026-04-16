# Exercise 5.2 -- The Tax Season Hunt

**Search** -- Find 5 specific documents in a 100+ file archive using only vague descriptions

## Goal

It is tax season. Your accountant needs 5 specific documents from your `document-archive/` -- a folder with 100+ files accumulated over 2 years. The catch: you can only describe the documents vaguely. You cannot search by exact filename because you do not remember the exact names. You need to use content-based search, metadata filtering, and iterative refinement to find each document.

## What You Have

- `document-archive/` -- 100+ files scattered across subdirectories (`2024/`, `2025/`, `taxes/`, `receipts/`, `contracts/`, `misc/`, `unsorted/`), with inconsistent naming and some files in unexpected locations

## Your Tasks

### The 5 Documents to Find

1. **"The PDF about Q3 dividends from my accountant"** -- A summary of dividend income for Q3 2024
2. **"The spreadsheet with monthly expenses from 2024"** -- A tracking sheet with all monthly expenses
3. **"That receipt from the office furniture purchase"** -- A receipt for a desk or office equipment
4. **"The contract with the freelance developer"** -- An agreement with a developer named John
5. **"The bank statement showing the large transfer in March"** -- A March 2024 bank statement with a transfer over $5,000

### For Each Document

1. Describe your search strategy (what terms, filters, or approaches you tried first)
2. Show the search commands you used
3. Document what you found and how you confirmed it was the right file
4. If you found multiple candidates, explain how you narrowed to the correct one

### Create SEARCH-RESULTS.md

Document your complete search process and findings for all 5 documents.

## Expected Results

- All 5 documents located and identified
- A `SEARCH-RESULTS.md` documenting the search process for each document
- For each document: search strategy, commands used, file found, and confirmation method

## Reflection

1. Which document was hardest to find? What made it difficult?
2. What search strategy worked best: filename patterns, content grep, date filtering, or size filtering?
3. What changes to file naming or structure would make future searches easier?

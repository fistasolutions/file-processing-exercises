# Exercise 3.1 -- The Freelancer's Chaos

**Build** -- Organize 60+ mixed files into a systematic folder structure with documented rules

## Goal

A freelance designer has 60+ files dumped in a single folder: invoices, design mockups, contracts, project assets, correspondence, and miscellaneous junk. No folders, no naming convention, no organization. Your job is to collaborate with Claude Code to design categorization rules, document them, and organize every file -- creating a reusable SYSTEM, not just a one-time cleanup.

## What You Have

- `freelancer-files/` -- A flat folder with 60+ files of various types: PDFs (invoices, contracts), PNGs/SVGs (designs, screenshots), DOCX (contracts), TXT/MD (notes, correspondence), and miscellaneous files. Some files are ambiguous (a PDF could be an invoice OR a contract).

## Your Tasks

### Step 1: Survey the Chaos

Use Claude Code to catalog every file by type. Identify clusters and patterns. How many file types exist? Are there naming patterns?

### Step 2: Design Categorization Rules

Create rules for organizing files. Your rules must handle:

- Clear cases (a file named "invoice-..." goes to Invoices/)
- Ambiguous cases (a PDF that could be an invoice or a contract)
- Edge cases (temp files, screenshots, duplicates)
- A fallback for files that match no rule

### Step 3: Document Rules

Write your rules in `organization-rules.md`. Each rule should be unambiguous -- someone else should be able to follow them without asking you questions.

### Step 4: Test on One File Per Category

Before batch organizing, pick one file from each category and manually verify your rules place it correctly.

### Step 5: Execute Organization

Organize all 60+ files into your folder structure.

### Step 6: Verify

Confirm every file is accounted for. No files lost, no files in wrong categories.

## Expected Results

- An organized folder structure with clear categories
- An `organization-rules.md` file with unambiguous, complete rules
- All 60+ files organized (verify with file counts: before vs. after)

## Reflection

1. Which files were hardest to categorize? What made them ambiguous?
2. Could the freelancer follow your rules for new files without asking you? What would make the rules clearer?
3. How would your rules change if this were a team of 3 freelancers?

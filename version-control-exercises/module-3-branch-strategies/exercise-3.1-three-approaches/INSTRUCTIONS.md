# Exercise 3.1 — Three Approaches

**Build: Parallel branching workflow** — Develop three competing solutions on separate branches, test them, and merge the winner

## Goal

You have unsorted data that needs to be sorted three different ways. Develop each sorting approach on its own Git branch, test each against provided test cases, merge the best implementation to `main`, and clean up the rest.

## What You Have

```
sorting-challenge/
├── data.txt           # 50 records: LastName, FirstName, Date, Score
├── requirements.md    # What each sorting approach must do
└── test-cases.txt     # 5 test cases with expected outputs
```

## Your Tasks

### Step 1: Initialize and Study the Data

```bash
cd sorting-challenge
git init
git add -A
git commit -m "Initial sorting challenge with data and test cases"
```

Read `requirements.md` and `test-cases.txt` carefully. You need three sorting approaches:
1. Sort by Score (descending)
2. Sort by Date (chronological)
3. Sort by Name (alphabetical)

### Step 2: Create Branch for Approach 1 — Sort by Score

```bash
git checkout -b approach-score
```

Ask Claude Code to write a sorting script:
> "Write a Python script sort.py that reads data.txt and sorts records by the Score column (descending). On ties, sort alphabetically by last name. Output to sorted_by_score.txt."

Test against the test cases:
```bash
python sort.py
head -5 sorted_by_score.txt    # Compare with TEST 1 in test-cases.txt
tail -3 sorted_by_score.txt    # Compare with TEST 2 in test-cases.txt
```

Commit your work:
```bash
git add sort.py
git commit -m "Implement sort by score (descending) with tiebreaker"
```

### Step 3: Create Branch for Approach 2 — Sort by Date

Go back to `main` first (clean starting point):
```bash
git checkout main
git checkout -b approach-date
```

Ask Claude Code for the date-sorting approach:
> "Write a Python script sort.py that reads data.txt and sorts records by date (chronological). On same dates, sort by score descending. Output to sorted_by_date.txt."

Test and commit:
```bash
python sort.py
head -5 sorted_by_date.txt     # Compare with TEST 3
git add sort.py
git commit -m "Implement sort by date (chronological) with score tiebreaker"
```

### Step 4: Create Branch for Approach 3 — Sort by Name

```bash
git checkout main
git checkout -b approach-name
```

Ask Claude Code:
> "Write a Python script sort.py that reads data.txt and sorts records alphabetically by last name, then first name (case-insensitive). Output to sorted_by_name.txt."

Test and commit:
```bash
python sort.py
head -5 sorted_by_name.txt     # Compare with TEST 4
tail -2 sorted_by_name.txt     # Compare with TEST 5
git add sort.py
git commit -m "Implement sort by name (alphabetical, case-insensitive)"
```

### Step 5: Compare and Choose

```bash
git log --all --oneline --graph    # See all three branches
```

Review each approach:
```bash
git diff approach-score..approach-date -- sort.py
git diff approach-score..approach-name -- sort.py
```

Pick the approach with the cleanest code (not just correctness — readability matters).

### Step 6: Merge the Winner

```bash
git checkout main
git merge approach-score       # (or whichever you chose)
```

### Step 7: Clean Up

```bash
git branch -d approach-score
git branch -d approach-date
git branch -d approach-name
git branch                     # Should show only main
```

## Verification

```bash
# Should be on main branch
git branch

# Should show merge commit
git log --oneline --graph

# Only main branch should exist
git branch | wc -l

# The winning sort script should work
python sort.py
```

## Reflection

1. Why is it useful to develop competing approaches on separate branches instead of rewriting the same file three times?
2. When you switched between branches, what happened to `sort.py`? How does Git manage different versions of the same file?
3. If you wanted to combine elements from two approaches (e.g., the algorithm from one and the output format from another), how would you do that?

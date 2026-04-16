# Sorting Challenge Requirements

## The Data

The file `data.txt` contains 50 records in the format:
```
LastName, FirstName, Date, Score
```

## What You Need to Build

Write a Python script (`sort.py`) that can sort this data in three different ways.
Each sorting approach should be developed on its own branch.

## Three Sorting Approaches

### Approach 1: Sort by Score (Descending)
- Highest scores first
- If scores are tied, sort alphabetically by last name
- Output: `sorted_by_score.txt`

### Approach 2: Sort by Date (Chronological)
- Earliest dates first
- If dates are the same, sort by score descending
- Output: `sorted_by_date.txt`

### Approach 3: Sort by Name (Alphabetical)
- Sort by last name, then first name
- Case-insensitive
- Output: `sorted_by_name.txt`

## Evaluation

After building all three approaches on separate branches:
1. Test each against `test-cases.txt`
2. Pick the approach that best demonstrates clean code
3. Merge the winner to `main`
4. Delete the other branches

## Constraints

- Pure Python only (no external libraries)
- Each approach should be a complete, runnable script
- Include a `--verify` flag that checks output against test cases

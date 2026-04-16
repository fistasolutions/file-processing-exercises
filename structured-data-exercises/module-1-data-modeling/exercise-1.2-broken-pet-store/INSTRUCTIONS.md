# Exercise 1.2 -- Broken Pet Store

**Debug**: Data Modeling -- Find and fix 6 bugs in SQLAlchemy model definitions

## Goal

Fix 6 bugs in a pet store management system's model definitions. The bugs span imports, attribute naming, column types, foreign key references, and constraints. Each bug produces a different type of error. When all bugs are fixed, the test suite passes completely.

## What You Have

- `broken_models.py` -- Pet store models (Owner, Pet, Vet) with 6 bugs. Each bug is a different category of mistake.
- `test_models.py` -- A test script that creates tables, inserts data, and validates model behavior. Currently fails due to the bugs.

## Your Tasks

### Step 1: Run the Tests

Run `python test_models.py` and observe the first error. Read the error message and traceback carefully -- it tells you exactly where to look.

### Step 2: Open the Models

Open `broken_models.py` and trace the error to the specific line causing it. Do not scan for all bugs at once -- focus on the one error the tests are showing you.

### Step 3: Fix and Re-test

Fix the first bug, then re-run the tests. A new error should appear (from the next bug). Repeat the cycle: read error, trace to line, fix, re-test.

### Step 4: Fix All Six Bugs

Continue until all tests pass with zero errors. The six bugs are:
1. An import error (something is not imported that should be)
2. A wrong attribute name (SQLAlchemy looks for a specific attribute and it is misspelled)
3. A wrong column type (the type does not match what the data requires)
4. A missing foreign key reference (a relationship column has no ForeignKey)
5. A missing constraint (data that should be unique is not enforced)
6. A missing nullability constraint (a required field allows NULL values)

### Step 5: Verify Complete Fix

After all tests pass, verify by inserting additional records: try a duplicate email (should fail), try a pet without a name (should work since name will be String), try a vet without a license number (should fail after your fix).

## Expected Results

- All tests in `test_models.py` pass with zero errors
- The models correctly enforce: unique owner emails, required vet license numbers, proper pet-to-owner foreign key relationships
- Each bug fix addresses a different category of SQLAlchemy modeling mistake

## Reflection

1. Which bug was hardest to identify from the error message alone? Why?
2. If you were writing a code review checklist for SQLAlchemy models, what 3 items would you always check?
3. How does the `__tablename__` attribute relate to what you see in the actual database? What happens if you get it wrong?

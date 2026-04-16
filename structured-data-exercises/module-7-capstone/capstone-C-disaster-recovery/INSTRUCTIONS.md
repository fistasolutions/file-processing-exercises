# Capstone C -- Disaster Recovery

**Forensics**: Full-system debugging -- find and fix 8+ bugs spanning models, CRUD, transactions, and deployment

## Goal

Repair a "production" budget tracker application that has bugs in every layer: model definitions, CRUD operations, relationship configuration, transaction safety, connection configuration, and query logic. Triage the bugs, fix them in the right order, and write a postmortem documenting each one.

## What You Have

- `broken_budget_tracker.py` -- A complete budget tracker application with 8+ bugs across all layers. The application has User, Category, and Expense models, CRUD functions, a transfer function, a monthly summary query, and database connection setup.
- `test_budget_tracker.py` -- A comprehensive test suite that exercises all functions. Many tests currently fail due to the bugs.

## Your Tasks

### Step 1: Run the Tests

Run `python test_budget_tracker.py` and observe the cascade of failures. Some errors may block other tests from running.

### Step 2: Inventory the Bugs

Before fixing anything, read through `broken_budget_tracker.py` and make a list of every bug you can find. Categorize each one:
- Model layer (wrong types, missing attributes, relationship errors)
- CRUD layer (session management, missing commits)
- Transaction layer (atomicity violations)
- Deployment layer (security, pooling)
- Query layer (logic errors)

### Step 3: Triage

Determine which bugs block other fixes. Fix blocking bugs first. For example:
- Import errors and model definition errors block everything
- Relationship errors block navigation tests
- CRUD bugs block transaction tests

### Step 4: Fix All Bugs

Fix each bug, re-running relevant tests after each fix. The 8+ bugs span:
1. Model: wrong column type for amount
2. Model: missing tablename on a model
3. CRUD: missing commit in create function
4. Relationship: back_populates mismatch
5. Transaction: non-atomic transfer
6. Deployment: hardcoded credentials
7. Deployment: missing pool_pre_ping
8. Query: wrong date comparison in monthly summary

### Step 5: Verify All Tests Pass

Run the full test suite. All tests should pass.

### Step 6: Write a Postmortem

Create a `postmortem.md` file documenting:
- Each bug found
- Its category (model/CRUD/transaction/deployment/query)
- Root cause
- Fix applied
- How to prevent this category of bug in the future

## Expected Results

- All tests in `test_budget_tracker.py` pass
- All 8+ bugs identified and fixed
- `postmortem.md` documents every bug with category, cause, fix, and prevention
- Bugs are fixed in the correct order (blocking bugs first)

## Reflection

1. Which layer had the most impactful bugs (the ones that caused the most cascading failures)?
2. If you could only add 3 automated checks to prevent these bugs, which 3 would have the highest ROI?
3. How would you organize a code review to catch these categories of bugs before they reach production?

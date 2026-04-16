# Exercise 2.2 -- Broken Task Manager

**Debug**: CRUD Operations -- Find and fix 5 bugs in task management CRUD functions

## Goal

Fix 5 bugs in a task management system's CRUD functions. The data models are correct -- all bugs are in the operations layer. Each bug represents a different category of CRUD mistake: data persistence, query syntax, session lifecycle, error handling, and query execution.

## What You Have

- `models.py` -- Working Task model with id, title, status, priority, due_date, and created_at fields. This file is correct -- do not modify it.
- `broken_crud.py` -- Five CRUD functions that each contain one bug. The functions look reasonable at first glance, but each one fails in a specific way.
- `test_crud.py` -- A test suite that validates each CRUD operation. Some tests currently fail due to the bugs.

## Your Tasks

### Step 1: Understand the Model

Read `models.py` to understand the Task model and its fields. Note the column types and defaults.

### Step 2: Run the Tests

Run `python test_crud.py` and observe which tests fail and what error messages they produce. The errors should point you toward specific functions.

### Step 3: Trace Each Bug

Open `broken_crud.py` and for each failing test, trace the error back to the specific line in the CRUD function that causes it. The five bugs are:

1. **create_task()** -- Data is added but never persists to the database
2. **get_tasks_by_status()** -- Uses assignment instead of comparison in the filter
3. **update_task()** -- Modifies the task object after the session context has ended
4. **delete_task()** -- Crashes when trying to delete a non-existent task ID
5. **search_tasks()** -- Returns a Query object instead of actual results

### Step 4: Fix One at a Time

Fix each bug, re-run the tests, and confirm that specific test now passes. Do not fix all bugs at once.

### Step 5: Verify All Pass

Continue until all tests pass with zero errors.

## Expected Results

- All tests in `test_crud.py` pass
- `create_task()` persists data to the database
- `get_tasks_by_status()` correctly filters by status
- `update_task()` modifies and saves changes within the session
- `delete_task()` handles missing task IDs gracefully
- `search_tasks()` returns a list of Task objects, not a Query

## Reflection

1. Bug #1 (missing commit) is extremely common in real applications. What strategy would you use to make sure you never forget a commit?
2. Bug #3 (modifying after session closes) reveals a key concept about SQLAlchemy sessions. In your own words, what does "detached instance" mean?
3. If you were adding a new CRUD function to this codebase, what 3 things would you verify before considering it "done"?

# Exercise 6.1 -- Expense Audit

**Build**: Hybrid Verification -- Build a SQL+bash pipeline that cross-checks expense report totals

## Goal

Build a hybrid verification pipeline that computes expense totals two different ways -- once with SQLAlchemy (SQL) and once with bash+awk on an exported CSV -- then compares the results. If both methods agree, the numbers are trustworthy. If they disagree, something is wrong in one of the pipelines.

## What You Have

- `models.py` -- User, Category, and Expense models for an expense tracking system. Expense has user_id, category_id, amount (Float), description, and expense_date.
- `seed_data.py` -- A script that populates the database with 3 users, 5 categories, and 200+ expense records across 12 months with realistic amounts and distributions.

## Your Tasks

### Step 1: Understand the Data

Read `models.py` to understand the data model. Read `seed_data.py` to understand how the data is structured (which users, categories, date ranges, amount ranges).

### Step 2: Seed the Database

Run `python seed_data.py` to create and populate the database. The script creates a `expenses.db` SQLite file with 200+ records.

### Step 3: Build the Audit Functions

Create a new file called `audit.py` with these four functions:

1. **`get_monthly_total(session, user_id, year, month)`** -- Uses SQLAlchemy `func.sum()` to compute the total expenses for a specific user in a specific month. Returns a float.

2. **`export_to_csv(session, user_id, year, month, output_path)`** -- Exports matching expenses to a CSV file with columns: id, amount, description, date. Returns the number of rows exported.

3. **`verify_with_bash(csv_path)`** -- Uses `subprocess.run()` to execute an awk command that sums the `amount` column of the CSV file. Returns a float. The awk command should be something like: `awk -F',' 'NR>1 {sum+=$2} END {print sum}' file.csv`

4. **`hybrid_audit(session, user_id, year, month)`** -- Orchestrates the full audit:
   - Calls `get_monthly_total()` to get the SQL total
   - Calls `export_to_csv()` to export the data
   - Calls `verify_with_bash()` to get the bash total
   - Compares the two totals (allow for floating-point tolerance of $0.01)
   - Prints PASS or FAIL with both values
   - Returns True/False

### Step 4: Run Audits

Run the hybrid audit for at least 3 different user/month combinations:
- User 1, January 2024
- User 2, June 2024
- User 3, November 2024

Print results for each.

### Step 5: Print Summary

Print a summary table showing all audited periods, their SQL totals, bash totals, and PASS/FAIL status.

## Expected Results

- `audit.py` with 4 working functions
- SQL and bash totals agree (within $0.01) for all audited periods
- CSV files are created for each audited period
- Summary table shows all PASS results
- Temporary CSV files can be cleaned up after verification

## Reflection

1. If the SQL total and bash total disagree, how would you determine which one is wrong?
2. What floating-point issues might cause the totals to differ slightly even when both are correct? How would you handle that?
3. In what situation would hybrid verification be overkill? When is a single-tool check sufficient?

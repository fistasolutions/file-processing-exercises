# Tool Selection Scenarios

Five developers each chose the wrong tool for their data task. Analyze each one.

---

## Scenario 1: Grep vs. SQL for Structured Query

**The Task:** Find all customer orders over $500 placed in Q3 (July-September) from a dataset of 50,000 orders stored in JSON files (one file per day, 365 files).

**The Tool Used:** Bash with grep and awk
```bash
grep -r '"amount"' orders/ | awk -F':' '{print $NF}' | \
  awk '{gsub(/[^0-9.]/, ""); if ($1 > 500) print}' | wc -l
```

**The Result:** The developer reported 2,847 orders over $500. The actual count was 4,912. The bash pipeline:
- Failed to filter by Q3 dates (only filtered by amount)
- Missed amounts in nested JSON objects
- Incorrectly parsed amounts that had commas (e.g., "1,234.56" became "1" and "234.56")
- Produced a 43% accuracy rate

**Context:** The developer was comfortable with bash and distrusted "heavy" tools. The JSON files had varying structures -- some had `amount` as a top-level field, others nested it under `payment.amount`. Date fields used ISO format (`2024-07-15T14:30:00Z`).

---

## Scenario 2: SQL for Mathematical Computation

**The Task:** Calculate compound interest projections for 100 savings accounts over 30 years with monthly compounding, adjustable rate changes, and penalty calculations for early withdrawal.

**The Tool Used:** A single SQL query with nested CTEs
```sql
WITH RECURSIVE months AS (
    SELECT account_id, balance, rate, 1 as month_num
    FROM accounts
    UNION ALL
    SELECT account_id,
           balance * (1 + CASE
               WHEN month_num <= 60 THEN rate/12
               WHEN month_num <= 120 THEN (rate-0.005)/12
               ELSE (rate-0.01)/12
           END),
           rate,
           month_num + 1
    FROM months
    WHERE month_num <= 360
)
SELECT account_id, balance as projected_balance
FROM months
WHERE month_num = 360;
```

**The Result:** The query:
- Took 45 seconds to execute (recursive CTE generated 36,000 intermediate rows per account)
- Could not easily handle the early withdrawal penalty formula (which required conditional logic based on account age and withdrawal amount)
- Was nearly impossible to debug when projections looked wrong -- a single error in the CASE statement affected all 36,000 rows
- Required a rewrite every time the business changed the rate adjustment schedule

**Context:** The developer knew SQL well and wanted to keep everything in the database. The compound interest formula was straightforward in isolation, but the business rules around rate adjustments and penalties made the SQL increasingly complex and unmaintainable.

---

## Scenario 3: Python Loop for File System Operations

**The Task:** Count the number of `.log` files in a directory tree with 50,000 files across 2,000 subdirectories, and report the total size of log files per subdirectory.

**The Tool Used:** Python with os.walk
```python
import os

log_counts = {}
for root, dirs, files in os.walk("/var/logs/application"):
    for f in files:
        if f.endswith(".log"):
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            if root not in log_counts:
                log_counts[root] = {"count": 0, "size": 0}
            log_counts[root]["count"] += 1
            log_counts[root]["size"] += size

for directory, stats in sorted(log_counts.items()):
    print(f"{directory}: {stats['count']} files, {stats['size'] / 1024 / 1024:.1f} MB")
```

**The Result:** The script:
- Took 12 seconds to run (Python's os.walk is significantly slower than native filesystem tools for large directory trees)
- Broke when encountering symlinks that created circular references (infinite loop)
- Required manual handling of permission errors (crashed on first inaccessible directory)
- Used 200MB of memory building the dictionary for 2,000 directories

**Context:** The equivalent bash command `find /var/logs/application -name "*.log" -exec du -sh {} + | awk ...` completes in under 1 second and handles symlinks and permissions gracefully. The developer was more comfortable with Python and did not consider bash for the task.

---

## Scenario 4: Single SQL Query for Financial Audit

**The Task:** Generate a monthly financial audit report for a SaaS company, calculating Monthly Recurring Revenue (MRR), churn rate, and expansion revenue from a subscriptions database.

**The Tool Used:** A single SQL query
```sql
SELECT
    DATE_TRUNC('month', billing_date) as month,
    SUM(CASE WHEN status = 'active' THEN amount ELSE 0 END) as mrr,
    COUNT(CASE WHEN status = 'churned' THEN 1 END)::float /
        NULLIF(COUNT(CASE WHEN prev_status = 'active' THEN 1 END), 0) as churn_rate,
    SUM(CASE WHEN amount > prev_amount AND status = 'active'
        THEN amount - prev_amount ELSE 0 END) as expansion_revenue
FROM subscription_events
GROUP BY DATE_TRUNC('month', billing_date)
ORDER BY month;
```

**The Result:** The report showed:
- June MRR was off by $12,340 (3.2% error)
- The root cause: billing dates in the database used UTC timestamps, but 47 subscriptions billed on the last day of the month in US timezones appeared in the next month in UTC
- This timezone bug was invisible because there was no cross-check -- the SQL query was the single source of truth
- The error was discovered 3 months later during a board meeting when the CFO compared the report to Stripe's numbers

**Context:** A hybrid approach (SQL query + Python script that pulls the same data from the Stripe API and compares) would have caught the $12,340 discrepancy immediately. The developer assumed a single query was sufficient because "the database has all the data."

---

## Scenario 5: Hybrid Verification for Quick Exploration

**The Task:** During a debugging session, quickly check how many users signed up in the last 24 hours. The data is in a PostgreSQL database.

**The Tool Used:** A hybrid pipeline
```python
# Step 1: SQL query
result = session.execute(text(
    "SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '24 hours'"
))
sql_count = result.scalar()

# Step 2: Export to CSV
result = session.execute(text(
    "SELECT id, email, created_at FROM users WHERE created_at > NOW() - INTERVAL '24 hours'"
))
with open('/tmp/recent_users.csv', 'w') as f:
    f.write('id,email,created_at\n')
    for row in result:
        f.write(f'{row.id},{row.email},{row.created_at}\n')

# Step 3: Bash verification
import subprocess
bash_count = subprocess.run(
    ['bash', '-c', "tail -n +2 /tmp/recent_users.csv | wc -l"],
    capture_output=True, text=True
).stdout.strip()

# Step 4: Compare
print(f"SQL count: {sql_count}")
print(f"Bash count: {bash_count}")
if str(sql_count) == bash_count:
    print("VERIFIED: Counts match")
else:
    print("WARNING: Counts differ!")
```

**The Result:**
- The pipeline took 4 minutes to write and 15 seconds to run
- A single SQL query (`SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '24 hours'`) would have taken 5 seconds to write and 0.1 seconds to run
- The hybrid approach added zero value -- this was a simple count query with no calculation that could drift
- The developer's time was wasted because they applied a heavyweight verification process to a lightweight question

**Context:** The developer had just learned about hybrid verification in a course and was applying it everywhere. Hybrid verification is valuable for financial reports, data migrations, and complex aggregations where bugs are costly. For a quick count during debugging, it is pure overhead.

---

## Your Task

For each scenario, determine:
1. **Why it failed**: What limitation of the chosen tool caused the problem?
2. **Correct tool**: Which tool should have been used, and why?
3. **Consequence**: What was the real-world cost of the wrong choice?

Then write a **Tool Selection Decision Tree** that helps choose the right tool for future tasks.

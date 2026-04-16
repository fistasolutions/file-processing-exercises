# Exercise 5.2 -- Connection Doctor

**Debug**: Cloud Deployment -- Diagnose 5 different Neon connection failure scenarios

## Goal

Diagnose 5 different Neon PostgreSQL connection failure scenarios. Each scenario presents an error message, the code that produced it, and the developer's context. For each one, you will identify the root cause, write the fix, and explain how to prevent it in the future.

## What You Have

- `error_scenarios.md` -- 5 real-world connection failure scenarios, each with the exact error message, the code that produced it, and what the developer was doing at the time.

## Your Tasks

### Step 1: Read All Scenarios

Read `error_scenarios.md` to understand all 5 failure scenarios before diagnosing any of them. Some scenarios share root causes at different layers.

### Step 2: Diagnose Each Scenario

For each scenario, determine:
- **Root Cause**: One sentence explaining exactly why this error occurred
- **Fix**: The specific code or configuration change that resolves it
- **Prevention**: How to ensure this never happens again

### Step 3: Write Your Diagnosis

Create a new file called `diagnosis.md` with your findings for all 5 scenarios. Use this format for each:

```markdown
## Scenario N: [Error Name]

**Root Cause:** [One sentence]

**Fix:**
[Code change or configuration fix]

**Prevention:**
[Process or configuration that prevents recurrence]
```

### Step 4: Identify Patterns

After diagnosing all 5, write a summary section identifying which errors could be caught by:
- A connection test at startup
- A pre-deployment checklist
- An automated health check
- Better documentation

## Expected Results

- A `diagnosis.md` file with correct diagnosis for all 5 scenarios
- Each diagnosis includes: root cause, fix, and prevention strategy
- A summary section identifying which errors are preventable by automation

## Reflection

1. Which error message was most misleading (the message did not clearly point to the actual cause)?
2. If you were building a deployment health check script, which of these 5 scenarios could it automatically detect?
3. What is the difference between a connection error at startup versus a connection error during operation? Which is easier to debug?

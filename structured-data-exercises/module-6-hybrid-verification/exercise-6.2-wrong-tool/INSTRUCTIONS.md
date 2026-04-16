# Exercise 6.2 -- Wrong Tool

**Debug/Analysis**: Hybrid Verification -- Analyze 5 scenarios where the wrong tool was chosen

## Goal

Analyze 5 real-world data scenarios where a developer chose the wrong tool (bash, Python, SQL, or hybrid), leading to incorrect results, poor performance, or wasted effort. For each scenario, determine why it failed and recommend the correct approach.

## What You Have

- `scenarios.md` -- 5 real-world data scenarios, each describing the task, the tool that was used, and the result. Each choice was wrong in a different way.

## Your Tasks

### Step 1: Read All Scenarios

Read `scenarios.md` to understand all 5 scenarios. Each one describes what the developer was trying to do, which tool they used, and what went wrong.

### Step 2: Analyze Each Scenario

For each scenario, determine:
- **Why it failed**: What specific limitation of the chosen tool caused the problem?
- **Correct tool**: Which tool (bash, Python, SQL, hybrid) should have been used?
- **Consequence**: What was the real-world cost of the wrong choice?

### Step 3: Write Your Analysis

Create a new file called `analysis.md` with your findings. For each scenario, use this format:

```markdown
## Scenario N: [Short Title]

**Wrong Tool:** [What was used]
**Should Have Used:** [What should have been used]

**Why It Failed:**
[2-3 sentences explaining the specific limitation]

**Correct Approach:**
[Brief description of how the right tool solves the problem]

**Consequence:**
[What the wrong choice cost in real terms]
```

### Step 4: Build a Decision Tree

At the end of your analysis, write a "Tool Selection Decision Tree" -- a set of rules for choosing the right tool:

```markdown
## Tool Selection Decision Tree

1. Is the data in a database? -> [guidance]
2. Is it a one-off exploration or recurring report? -> [guidance]
3. Does accuracy need to be verified? -> [guidance]
4. How large is the dataset? -> [guidance]
5. Does the task require mathematical computation? -> [guidance]
```

## Expected Results

- An `analysis.md` file with correct analysis for all 5 scenarios
- Each analysis identifies the right tool with justification
- A decision tree that could help a developer choose the right tool for future tasks

## Reflection

1. Which scenario was most surprising -- where the "obvious" tool choice was actually the worst choice?
2. Is there a task where ALL four approaches (bash, Python, SQL, hybrid) would work equally well? What would make you prefer one over the others?
3. In your own work, how would you decide when to switch from a single tool to a hybrid approach?

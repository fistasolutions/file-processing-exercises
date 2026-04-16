# Exercise 6.2 — Pattern Audit

**Debug: Workflow gap analysis** — Find the flaws in a team's Git workflow that caused three real incidents

## Goal

A team's `git-workflow.md` has inconsistencies and gaps that led to three incidents. Read each incident report, trace the root cause back to a specific workflow rule (or missing rule), and fix the document.

## What You Have

```
broken-workflow/
├── git-workflow.md       # The team's workflow doc (~60 lines, has problems)
├── incident-1.md         # Silent breaking change pushed to main
├── incident-2.md         # AI-generated code merged without review
└── incident-3.md         # Hotfix chain that made things worse
```

## Your Tasks

### Step 1: Read the Workflow Document

```bash
cat broken-workflow/git-workflow.md
```

Read it once, noting anything that seems risky or contradictory. Don't read the incidents yet.

**Initial suspicions** (write these down before reading incidents):
1. _______
2. _______
3. _______

### Step 2: Read Each Incident

```bash
cat broken-workflow/incident-1.md
cat broken-workflow/incident-2.md
cat broken-workflow/incident-3.md
```

For each incident, answer the questions at the bottom of the report.

### Step 3: Map Incidents to Workflow Gaps

Create a file `broken-workflow/audit-findings.md` with this structure:

```markdown
# Workflow Audit Findings

## Incident 1: Silent Breaking Change
**Workflow rule that failed:** [quote the specific rule]
**Why it failed:** [explain the gap]
**Recommended fix:** [new rule text]

## Incident 2: Unreviewed AI Merge
**Workflow rule that failed:** [quote the specific rule(s)]
**Why it failed:** [explain the gap(s)]
**Recommended fix:** [new rule text]

## Incident 3: Hotfix Chain
**Workflow rule that failed:** [quote the specific rule]
**Why it failed:** [explain the contradiction]
**Recommended fix:** [new rule text]

## Additional Gaps Found
[List any other problems you spotted in the workflow doc
 that haven't caused incidents YET but could]
```

### Step 4: Fix the Workflow Document

Create `broken-workflow/git-workflow-fixed.md` — a corrected version that:

1. Removes the "small changes skip PR" rule (caused Incident 1)
2. Fixes the 48-hour auto-merge rule (caused Incident 2)
3. Adds proper AI disclosure requirements (caused Incident 2)
4. Fixes the hotfix procedure contradiction (caused Incident 3)
5. Addresses any additional gaps you found

### Step 5: Verify Your Fixes

For each incident, trace through your fixed workflow and confirm it would have prevented the problem:

- Incident 1: Carol's 3-line change. Would your new workflow require a PR? Yes/No
- Incident 2: Dave's unreviewed merge. What happens after 48 hours in your workflow?
- Incident 3: Alice's hotfix. Does your hotfix procedure include testing?

## Verification

```bash
# Both audit and fixed workflow should exist
ls broken-workflow/audit-findings.md broken-workflow/git-workflow-fixed.md

# Fixed workflow should be longer (more comprehensive)
wc -l broken-workflow/git-workflow.md broken-workflow/git-workflow-fixed.md

# Fixed workflow should not contain the dangerous rules
grep "skip PR" broken-workflow/git-workflow-fixed.md
# Should NOT match "can merge without approval" in the auto-merge context
grep "merge without approval" broken-workflow/git-workflow-fixed.md
```

## Reflection

1. Were your initial suspicions (Step 1) correct? Did you spot the problems before reading the incidents?
2. The original workflow was written with good intentions. Why do well-intentioned "efficiency shortcuts" often cause more problems than they solve?
3. How would you introduce these workflow changes to a team that's been using the broken workflow for months?

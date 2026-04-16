# Exercise 6.1 — Workflow Builder

**Build: Git workflow documentation** — Create a comprehensive team Git workflow document for a new project

## Goal

A new e-commerce project is starting with a 4-person team. Create a complete `git-workflow.md` that covers branching strategy, commit conventions, PR process, AI usage policies, and push schedules — all tailored to the team's constraints.

## What You Have

```
ecommerce-project/
├── README.md             # Project description and tech stack
├── requirements.md       # Feature list (MVP + nice-to-have)
└── team-info.md          # 4 team members with timezones and availability
```

## Your Tasks

### Step 1: Understand the Constraints

Read all three files carefully:

```bash
cat ecommerce-project/README.md
cat ecommerce-project/requirements.md
cat ecommerce-project/team-info.md
```

Key constraints to note:
- 4 people across 4 different timezones
- Limited overlapping availability (only Sundays 3-4pm UTC for all)
- Some team members are Git beginners
- The project has both frontend and backend work
- 8-week timeline for MVP

### Step 2: Create the Workflow Document

Create `ecommerce-project/git-workflow.md` with these sections:

**Section 1: Branching Strategy**
- What branches exist (main, develop, feature, fix, experiment)
- Naming conventions for each
- Rules about who can push to which branches
- How to handle long-running feature branches

**Section 2: Commit Conventions**
- Message format (type: description)
- Allowed types (feat, fix, docs, refactor, test, chore)
- Examples of good and bad messages
- When to commit (frequency guidance)

**Section 3: Pull Request Process**
- When PRs are required (always? exceptions?)
- What the PR description must include
- Review requirements (who, how many approvals)
- What to do when no one reviews within a time limit
- Merge strategy (squash? merge commit? rebase?)

**Section 4: AI Usage Policy**
- When AI tools are allowed
- What MUST be disclosed in PRs
- Review requirements for AI-generated code
- What the developer must understand before merging AI code

**Section 5: Push Schedule and Coordination**
- How often to push (every commit? end of session? daily?)
- How to handle the timezone challenge
- Async code review expectations
- How to communicate about blocking issues

**Section 6: Emergency Procedures**
- What counts as an emergency
- Hotfix process
- Who has authority to push directly to main
- Post-incident review process

### Step 3: Use Claude Code to Help

Ask Claude Code for help with specific sections:

> "Given a team of 4 developers across UTC-5, UTC-8, UTC+0, and UTC+5:30 with only 1 hour of weekly overlap, what's the best Git branching strategy? The project is an e-commerce site with 8 weeks to MVP."

But don't just accept AI's suggestion blindly. Adapt it to YOUR team's specific needs.

### Step 4: Peer Review Your Own Document

Read through the workflow document and check for:
- [ ] Are there any contradictions? (e.g., "always PR" but "push to main for small fixes")
- [ ] Does it account for the timezone differences?
- [ ] Is it realistic for beginners? (Dave is still learning Git basics)
- [ ] Does it handle the AI transparency requirement from requirements.md?
- [ ] Are emergency procedures safe enough?

## Verification

```bash
# Workflow document should exist and be substantial
wc -l ecommerce-project/git-workflow.md
# Should be 80+ lines

# Check all sections exist
grep -c "##" ecommerce-project/git-workflow.md
# Should be 6+ sections

# Check for common pitfalls
grep -i "directly to main" ecommerce-project/git-workflow.md
# If this exists, make sure it's in the emergency section ONLY
```

## Reflection

1. Which section was hardest to write? Why?
2. The team has only 1 hour of weekly overlap. How does this affect your PR review process?
3. Look at your AI usage policy. Is it strict enough to prevent the problems from Exercise 5.2? Is it flexible enough to not slow down development?

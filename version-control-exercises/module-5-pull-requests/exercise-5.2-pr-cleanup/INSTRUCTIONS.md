# Exercise 5.2 — PR Cleanup

**Debug: Pull request quality** — Analyze three bad PRs and rewrite them to be professional

## Goal

Three pull requests have problems: one has no description, one hides AI usage, and one ignores failing CI checks. Read each PR, understand what's wrong, and write improved versions.

## What You Have

```
bad-prs/
├── pr-1-no-description.md     # "Updated code" — 47 files, no explanation
├── pr-2-hidden-ai.md          # Sophisticated code with no AI disclosure
└── pr-3-failing-checks.md     # Merging despite failing tests and linting
```

## Your Tasks

### PR 1: The No-Description Monster

```bash
cat bad-prs/pr-1-no-description.md
```

Read the simulated reviewer comments. Then:

1. Identify ALL the problems with this PR (not just the missing description)
2. Write `pr-1-improved.md` with:
   - A proper summary explaining the changes
   - Changes grouped by area (auth, database, UI, logging)
   - A suggestion for how to split this into 3-4 smaller PRs
   - Testing information for each area

Ask Claude Code: "Help me write a proper PR description for a PR that changes authentication, database schema, UI components, and logging format across 47 files."

### PR 2: The Hidden AI

```bash
cat bad-prs/pr-2-hidden-ai.md
```

The code quality is fine. The problem is transparency. Write `pr-2-improved.md` with:

1. The same technical description (it's accurate)
2. An honest AI disclosure section:
   - Which tool was likely used (based on the code style)
   - Which parts were AI-generated
   - Which parts the developer understands vs. needs to study more
   - How the AI output was verified
3. A note about what the developer should learn to fully own this code

### PR 3: The Failing Checks Ignorer

```bash
cat bad-prs/pr-3-failing-checks.md
```

Read the failing checks and the comment thread. Write `pr-3-improved.md` with:

1. A plan for fixing the lint issues (describe the specific fixes)
2. An explanation of WHY the performance test fails (what is a database index?)
3. A plan for fixing the performance issue
4. An explanation of why merging with failing checks is bad practice
5. The rewritten PR description acknowledging these issues

## Verification

```bash
# All three improved descriptions should exist
ls bad-prs/pr-*-improved.md

# Each should be substantially longer than the original
wc -l bad-prs/pr-1-no-description.md bad-prs/pr-1-improved.md
wc -l bad-prs/pr-2-hidden-ai.md bad-prs/pr-2-improved.md
wc -l bad-prs/pr-3-failing-checks.md bad-prs/pr-3-improved.md
```

## Reflection

1. Which of the three bad PRs do you think is the most dangerous? Why?
2. The "hidden AI" PR (#2) has working code. Some people argue "if it works, who cares how it was written?" Why is that reasoning flawed?
3. For PR #3, the developer says the performance test is "flaky." How can you tell the difference between a flaky test and a real performance problem?

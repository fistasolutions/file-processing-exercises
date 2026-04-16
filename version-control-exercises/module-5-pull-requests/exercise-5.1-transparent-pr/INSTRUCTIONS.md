# Exercise 5.1 — Transparent PR

**Build: Pull request workflow** — Create a professional pull request with AI transparency documentation

## Goal

You have a calculator project with a feature branch that adds error handling. Create a pull request using the provided AI transparency template, self-review the diff, and write a description that honestly documents which parts were AI-generated.

## What You Have

```
calculator-feature/
├── calculator.py         # Calculator with 6 operations (~85 lines)
├── test_calculator.py    # Tests for all operations (~55 lines)
└── pr-template.md        # PR template with AI transparency sections
```

## Your Tasks

### Step 1: Initialize the Repository

```bash
cd calculator-feature
git init
git add calculator.py test_calculator.py
git commit -m "Add calculator with basic operations and tests"
```

### Step 2: Create a Feature Branch

```bash
git checkout -b feature/error-handling
```

### Step 3: Ask AI to Improve Error Handling

Ask Claude Code to enhance the calculator:

> "Add input validation to all calculator functions: check that inputs are numbers, add clear error messages, and handle edge cases like dividing by zero with informative messages."

After AI makes changes, review them:
```bash
git diff
```

Commit the AI-generated changes:
```bash
git add calculator.py
git commit -m "Add comprehensive input validation to all calculator operations"
```

### Step 4: Update Tests for New Error Handling

Ask Claude Code:
> "Update test_calculator.py to test the new input validation — test that TypeError is raised for non-number inputs and ValueError for invalid operations."

Review and commit:
```bash
git diff
git add test_calculator.py
git commit -m "Add tests for input validation and error handling"
```

### Step 5: Write the PR Description

Now the important part. Read `pr-template.md` and fill it out honestly. Create a file called `my-pr-description.md`:

**Key sections to fill out:**

1. **Summary:** What the PR does and why
2. **Changes Made:** Specific changes, file by file
3. **AI Assistance Disclosure:**
   - Which AI tool(s) you used
   - What AI generated (be specific — "AI wrote the validation logic in calculator.py lines 15-45")
   - What YOU wrote or modified
   - How you verified the AI output (did you read every line? run tests? test edge cases?)
4. **Testing Done:** What you tested and how

### Step 6: Self-Review

Pretend you're reviewing someone else's PR. Look at the full diff:

```bash
git diff main..feature/error-handling
```

Check for:
- [ ] Does every function have proper validation?
- [ ] Are error messages clear and helpful?
- [ ] Do tests cover the error cases?
- [ ] Is there any dead code or unnecessary changes?
- [ ] Would you approve this PR if someone else wrote it?

Write 2-3 review comments in your PR description noting things you'd flag.

### Step 7: Create the PR (if you have a remote)

If you've pushed to GitHub:
```bash
git push -u origin feature/error-handling
gh pr create --title "Add input validation to calculator" --body-file my-pr-description.md
```

## Verification

```bash
# Feature branch should have 2 commits beyond main
git log main..feature/error-handling --oneline

# Tests should pass
python -m pytest test_calculator.py -v

# PR description should exist and be filled out
cat my-pr-description.md | head -30

# The diff should show meaningful changes
git diff main..feature/error-handling --stat
```

## Reflection

1. Why is AI transparency in PRs important? What could go wrong if a reviewer doesn't know which parts were AI-generated?
2. Look at your AI disclosure section. Was it uncomfortable to be specific about what AI wrote? Why is specificity important?
3. During self-review, did you find anything the AI got wrong that you didn't catch before? What does this tell you about the review process?

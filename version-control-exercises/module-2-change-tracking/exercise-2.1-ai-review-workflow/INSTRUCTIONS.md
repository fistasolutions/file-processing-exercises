# Exercise 2.1 — AI Code Review Workflow

**Build: Change review discipline** — Practice the review-before-commit workflow with AI-assisted development

## Goal

Use Claude Code to make three rounds of improvements to a working todo app. For each round, use `git diff` to review changes before committing, `git restore` to undo bad changes, and selective staging to keep only the good ones.

## What You Have

```
todo-app/
├── app.py          # Working todo app (~75 lines)
├── tasks.json      # 10 sample tasks
└── README.md       # Basic documentation
```

The app works as-is. You're going to improve it iteratively, practicing the review workflow each time.

## Your Tasks

### Step 1: Initialize and Make Your First Commit

```bash
cd todo-app
git init
git add -A
git commit -m "Initial todo app with sample tasks"
```

### Step 2: Round 1 — Ask AI to Add Due Date Support

Ask Claude Code to add due date support to the todo app. Something like:

> "Add a due_date parameter to add_task and display overdue tasks in red when listing"

After AI makes changes:

```bash
git status                    # See what files changed
git diff                      # Review EVERY change line by line
```

**Review checklist:**
- Does the change make sense?
- Did AI modify anything unexpected?
- Are there any bugs in the new code?
- Did it break existing functionality?

If everything looks good:
```bash
git add app.py
git commit -m "Add due date support with overdue task highlighting"
```

If something looks wrong:
```bash
git restore app.py            # Undo ALL changes to app.py
# Or use git add -p app.py to stage only specific hunks
```

### Step 3: Round 2 — Ask AI to Add Search Functionality

Ask Claude Code:

> "Add a search_tasks function that finds tasks by keyword in the title"

Review the changes again:
```bash
git diff
```

This time, practice **partial staging**. If AI changed both `app.py` and `tasks.json`, but you only want the code changes:

```bash
git add app.py                # Stage only the code
git restore tasks.json        # Discard data changes
git commit -m "Add keyword search for tasks"
```

### Step 4: Round 3 — Ask AI to Refactor the Code

Ask Claude Code:

> "Refactor the task storage to use a class instead of module-level functions"

This is a bigger change. Review carefully:
```bash
git diff --stat               # Overview of what changed
git diff app.py               # Detailed line-by-line changes
```

If the refactor is good, commit it. If it's too aggressive or breaks the interface:
```bash
git stash                     # Save changes temporarily
python app.py                 # Test the original still works
git stash pop                 # Bring changes back
```

### Step 5: Review Your History

```bash
git log --oneline             # Should show 4 clean commits
git log --stat                # Shows files changed per commit
git diff HEAD~3..HEAD         # See all changes from start to finish
```

## Verification

```bash
# Should have 4 commits (initial + 3 improvements)
git log --oneline | wc -l

# Each commit should have a descriptive message
git log --oneline

# The app should still work
python app.py

# Working tree should be clean
git status
```

## Reflection

1. During which round did you find the most issues with AI-generated code? What kinds of issues were they?
2. How did `git diff` help you catch problems you might have missed by just running the code?
3. When would you use `git restore` (discard everything) vs `git add -p` (keep some, discard some)?

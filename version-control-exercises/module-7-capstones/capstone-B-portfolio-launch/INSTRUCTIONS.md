# Capstone B — Portfolio Launch

**Professional presence:** Build a GitHub profile with 3 clean repositories, proper READMEs, and a profile README

## Goal

Create a professional GitHub presence that demonstrates Git competence. You'll create 3 repositories with clean histories, write proper READMEs using the templates provided, and set up a profile README.

## Estimated Time: 2-4 hours

## What You Have

```
portfolio-templates/
├── profile-readme-template.md    # Template for your GitHub profile README
└── repo-readme-template.md       # Template for each project README
```

## Phase 1: Plan Your Portfolio

### Step 1: Choose 3 projects

Pick 3 projects you've built (or will build during this exercise):
1. **A Python utility** (e.g., the weather tracker, todo app, or contact manager from exercises)
2. **A data project** (e.g., the sorting challenge, or a CSV analyzer)
3. **A web project** (e.g., the portfolio site, or a simple web page)

For each project, note:
- What it does
- What you learned building it
- What AI tools you used

### Step 2: Prepare clean versions

For each project, create a clean Git history. This might mean:
- Starting fresh (`git init`) rather than using the messy exercise history
- Writing proper commit messages from the start
- Ensuring `.gitignore` is the first thing committed

## Phase 2: Create Repository 1

### Step 3: Initialize with care
```bash
mkdir project-name && cd project-name
git init
```

### Step 4: Write the README first
Copy `repo-readme-template.md` and customize every section:
- Project name and description
- Features list
- Quick start instructions (must actually work!)
- Project structure
- What you learned
- AI disclosure

```bash
git add README.md
git commit -m "Add project README with setup instructions and AI disclosure"
```

### Step 5: Add code with structured commits
Don't dump everything in one commit. Structure it:
```bash
git add src/core.py
git commit -m "Add core logic for [feature]"

git add src/utils.py
git commit -m "Add utility functions for [purpose]"

git add tests/
git commit -m "Add tests for core logic"
```

### Step 6: Push to GitHub
```bash
gh repo create project-name --public --source=. --push
```

## Phase 3: Create Repositories 2 and 3

Repeat Phase 2 for your other two projects. Each should have:
- A customized README (not copy-paste)
- At least 4 meaningful commits
- Proper `.gitignore`
- AI disclosure section

## Phase 4: Profile README

### Step 7: Create your profile repository
GitHub shows a README.md from a repository matching your username as your profile:

```bash
mkdir YOUR-USERNAME && cd YOUR-USERNAME
git init
```

### Step 8: Customize the profile template
Copy `profile-readme-template.md` to `README.md` and customize:
- Your name and background
- What you're currently learning
- Your projects (link to the 3 repos you created)
- Your AI development philosophy

### Step 9: Push the profile
```bash
gh repo create YOUR-USERNAME --public --source=. --push
```

Visit `github.com/YOUR-USERNAME` to see your profile README.

## Phase 5: Quality Check

### Step 10: Review everything as a stranger

Visit each of your repositories on GitHub and ask:
- Can someone understand what this project does in 30 seconds?
- Are the setup instructions actually correct? (Try following them!)
- Is the commit history clean and meaningful?
- Is AI usage properly disclosed?

### Step 11: Cross-link
Make sure your profile README links to all 3 project repos, and each project repo is properly described.

## Deliverables Checklist

- [ ] 3 GitHub repositories with clean commit histories
- [ ] Each repo has a customized README (not template copy-paste)
- [ ] Each repo has proper `.gitignore`
- [ ] Each repo has AI disclosure in the README
- [ ] Profile README exists at github.com/YOUR-USERNAME
- [ ] Profile links to all 3 project repos
- [ ] All setup instructions actually work (tested!)
- [ ] No secrets in any repository

## Verification

```bash
# Check all repos exist
gh repo list --limit 10

# Check each repo has a README
for repo in project1 project2 project3; do
    gh api repos/YOUR-USERNAME/$repo/readme --jq '.name' 2>/dev/null && echo "$repo: README exists"
done

# Check profile repo exists
gh api repos/YOUR-USERNAME/YOUR-USERNAME/readme --jq '.name'
```

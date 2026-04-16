# Version Control Exercises — Safe Experimentation with Git & GitHub

**Master Git workflows for AI-assisted development through hands-on practice**

_By Muhammad Usman Akbar — Learn by Doing, Not by Reading_

---

## How This Guide Works

These exercises bridge the gap between knowing Git commands and using them confidently in real projects. Reading about `git branch` is easy; actually creating three branches to test competing AI-generated solutions and then merging the winner requires practice. That is what these exercises provide.

Every exercise uses a real Git repository. You will run actual commands, create real commits, resolve real conflicts, and push to real GitHub repositories. There are no multiple-choice questions or fill-in-the-blank forms. You work in the terminal, with Git, on real code.

The exercises come in two types. **Build exercises** (X.1) ask you to create Git workflows from scratch — initialize repos, write .gitignore files, create branches, push to GitHub, write PRs. **Debug exercises** (X.2) give you broken repositories with pre-existing problems — secrets committed, branches tangled, pushes rejected — and ask you to diagnose and fix them. Build exercises teach you to do things right. Debug exercises teach you to fix things when they go wrong.

The core skills you will develop are: **repository management** (structuring commits, protecting secrets, maintaining clean history), **safe experimentation with branches** (testing ideas without risking working code, recovering from mistakes), and **professional GitHub workflows** (pushing with purpose, writing transparent PRs, documenting team conventions).

---

## The Git Safety Framework

The chapter lessons taught individual Git skills — committing, branching, pushing, reviewing. This framework assembles those skills into a single disciplined process. Use it for every exercise. Before doing anything with Git, run through these six steps:

1. **Assess** — What is the current state? Run `git status`, `git log --oneline`, and `git branch`. Understand where you are before moving.
2. **Plan** — What needs to happen? What is the safest path to get there? What could go wrong?
3. **Protect** — Create a safety net before making risky changes. Commit your current work. Create a branch. Make a backup. Never make risky changes on your only copy.
4. **Execute** — Run the commands with intention. Know what each command does before pressing Enter.
5. **Verify** — Did it work? Check `git status`, `git diff`, `git log`. Never assume success.
6. **Document** — Record what happened and why. Write clear commit messages. Update workflow docs. Your future self will thank you.

---

## Assessment Rubric

Use this rubric to evaluate your progress. Each exercise has verification steps, but this rubric measures your overall Git fluency.

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Command Accuracy** | Runs wrong commands, needs multiple attempts | Gets right command but wrong flags/arguments | Correct commands on first try for common scenarios | Handles edge cases and combines commands fluently |
| **Safety Awareness** | Makes changes without checking state first | Checks status but doesn't create safety nets | Commits/branches before risky operations consistently | Anticipates risks and creates preemptive safety measures |
| **Diagnosis Skill** | Can't interpret git output or error messages | Understands basic status output, struggles with complex state | Reads git output fluently, diagnoses common problems | Diagnoses unusual scenarios, explains root causes clearly |
| **Workflow Discipline** | No consistent pattern, ad-hoc commands | Follows basic add-commit cycle | Uses full workflow (status, diff, add, commit, push) consistently | Adapts workflow to context, documents decisions |
| **Recovery Confidence** | Panics at errors, afraid to experiment | Uses restore/reset but hesitantly | Recovers from common mistakes quickly and confidently | Handles complex recovery (merge conflicts, history rewriting) calmly |

**Scoring guide:**
- 5-8 points: Keep practicing Modules 1-2 before moving on
- 9-13 points: Solid foundation, ready for Modules 3-4
- 14-17 points: Strong skills, tackle Modules 5-6
- 18-20 points: Ready for capstone projects

---

## Module 1: Repository Foundations

**Core Skill:** Building clean, well-structured repositories from the start

The hardest Git problems to fix are the ones created in the first 5 minutes of a project. A missing `.gitignore` means secrets get committed. A sloppy first commit means bad habits from day one. This module teaches you to start right.

---

### Exercise 1.1 — Project Kickoff

**The Problem:** You have a weather tracker project with Python files, CSV data, configuration with API keys, and personal notes. None of it is in Git yet. You need to initialize a repository, but you can't just `git add .` because that would commit your secrets and personal files.

**Your Task:** Initialize the repository with a proper `.gitignore` (created BEFORE the first commit), stage files selectively, and write commit messages that a teammate could understand six months from now.

**What You'll Learn:**
- Why `.gitignore` must exist before your first `git add`
- How to stage files selectively instead of using `git add .`
- What makes a commit message useful vs. useless

**Starter Prompt (Intentionally Vague):**
> "Set up git for my project"

**Better Prompt (Build Toward This):**
> "I need to initialize a Git repository for a Python weather tracking project. The project has source code in src/, data files in data/, a config.json with API keys that must be excluded, and a notes/ folder with personal files. Help me create a .gitignore first, then stage and commit files in logical groups with descriptive messages."

**Reflection Questions:**
1. What would happen if you ran `git add .` before creating `.gitignore`?
2. Why is it better to make 3 small commits than 1 large one?
3. If a new developer joins the project, what would they need that isn't in the repository? How would they know?

---

### Exercise 1.2 — Repo Rescue

**The Problem:** A colleague's project is a mess. The `.env` file with database credentials is committed. The `config.json` has an API key in plain text. Every commit message is either "fix", "stuff", or "asdf". There is no `.gitignore`. You need to diagnose the damage and fix what you can.

**Your Task:** Assess what went wrong, create a `.gitignore`, remove secrets from tracking (while knowing they persist in history), create safe template files, and commit the fixes with proper messages.

**What You'll Learn:**
- How to find secrets that have been committed to a repository
- The difference between removing a file from tracking vs. removing it from history
- How to create `.env.example` and config templates for safe collaboration

**Starter Prompt (Intentionally Vague):**
> "Fix this repo"

**Better Prompt (Build Toward This):**
> "This repository has .env and config.json committed with secrets. I need to: 1) create a .gitignore to prevent future commits of these files, 2) remove them from git tracking with git rm --cached, 3) create .env.example and config.template.json with placeholder values, and 4) commit with a message explaining what was fixed and why."

**Reflection Questions:**
1. After `git rm --cached .env`, is the secret safe? Why or why not?
2. For each bad commit message in commit-log.txt, write what a good message would be.
3. If this repo was already on GitHub, what additional steps would you need to take?

---

## Module 2: Change Tracking & Recovery

**Core Skill:** Fearlessly experimenting because you can always recover

The biggest barrier to using Git effectively is fear. Fear of losing work. Fear of messing up the history. Fear of merge conflicts. This module systematically destroys that fear by teaching you exactly how to recover from the three most common mistakes.

---

### Exercise 2.1 — AI Code Review Workflow

**The Problem:** You have a working todo app. You want to improve it with AI assistance, but you've learned that AI doesn't always get things right. You need a workflow where you review every change before committing, keep the good parts, and discard the bad parts.

**Your Task:** Make 3 rounds of AI-assisted improvements. For each round: ask Claude Code for a change, use `git diff` to review it line by line, use `git restore` to undo bad changes, use selective staging to keep good ones, and commit with a clear message.

**What You'll Learn:**
- The review-before-commit discipline that separates professionals from beginners
- How to use `git diff` to catch bugs before they enter your history
- How to use `git restore` and `git add -p` for surgical control over what gets committed

**Starter Prompt (Intentionally Vague):**
> "Make this better"

**Better Prompt (Build Toward This):**
> "Add due date support to the todo app with these requirements: 1) add_task should accept an optional due_date parameter, 2) list_tasks should show overdue tasks first, 3) don't modify the existing tasks.json format in a breaking way. After making changes, I'll review with git diff before committing."

**Reflection Questions:**
1. During which round did AI introduce the most issues? What kind of issues?
2. How did `git diff` help you catch problems that just running the code wouldn't reveal?
3. When would you use `git restore` (discard everything) vs. `git add -p` (keep some, discard some)?

---

### Exercise 2.2 — Recovery Room

**The Problem:** Three disaster scenarios, each requiring a different recovery technique. Scenario A: AI modified 4 files without committing, and you need to sort good changes from bad. Scenario B: you accidentally staged test files alongside production code. Scenario C: you committed a broken version and need to get back to the working state.

**Your Task:** Run each setup script to create the broken state, then fix it using the appropriate recovery tool: `git restore` for unstaged, `git restore --staged` for staged, `git revert` for committed.

**New command: `git revert`** — The chapter lessons taught `git reset HEAD~1` to undo a commit you haven't pushed. `git revert` is the safer alternative when history has been shared (pushed to GitHub) — instead of erasing the commit, it creates a new commit that reverses the changes.

**What You'll Learn:**
- The three levels of "undo" in Git (working directory, staging area, committed)
- Why `git revert` creates a new commit instead of deleting the old one — and when to use it vs `git reset HEAD~1`
- How to use `git add -p` for partial staging when changes are mixed

**Reflection Questions:**
1. What is the difference between `git restore`, `git restore --staged`, and `git revert`?
2. Why does `git revert` preserve history? When does this matter?
3. In Scenario A, you used `git add -p` for partial staging. In what real situations would this be essential?

---

## Module 3: Branch Strategies

**Core Skill:** Testing multiple ideas safely without risking working code

Branches are Git's superpower for experimentation. Instead of making changes and hoping for the best, you can create a parallel universe, try something risky, and throw it away if it doesn't work — all without touching your working code. This module teaches you to think in branches.

---

### Exercise 3.1 — Three Approaches

**The Problem:** You have unsorted data and need to sort it. There are three valid approaches (by score, by date, by name), and you don't know which will produce the cleanest code. Instead of rewriting one file three times, you'll develop each approach on its own branch, test them, merge the winner, and delete the rest.

**Your Task:** Create 3 branches from `main`, ask AI for a different sorting approach on each, test against provided test cases, pick the winner, merge it, and clean up the losing branches.

**What You'll Learn:**
- How to use branches for parallel development of competing ideas
- How to switch between branches and compare implementations
- How to merge the winner and delete the rest cleanly

**Starter Prompt (Intentionally Vague):**
> "Sort this data"

**Better Prompt (Build Toward This):**
> "I'm on the 'approach-score' branch. Write a Python script sort.py that reads data.txt (format: LastName, FirstName, Date, Score) and sorts by Score descending. On ties, sort alphabetically by last name. Output to sorted_by_score.txt. I'll test against test-cases.txt."

**Reflection Questions:**
1. Why develop on separate branches instead of rewriting the same file?
2. When you switched branches, what happened to `sort.py`?
3. How would you combine the best parts of two different approaches?

---

### Exercise 3.2 — Branch Tangle

**The Problem:** A URL shortener project has three problems. Someone committed to the wrong branch — a storage change ended up on the analytics branch. Two branches modify the same file differently, creating a merge conflict. And a useful utility branch was never merged, leaving code orphaned.

**Your Task:** Run `setup.sh` to create the tangled state, then untangle it: identify the misplaced commit, merge the orphaned branch, resolve the merge conflict, and produce a clean `main` branch with all features.

**New commands:** `git cherry-pick <commit-hash>` copies a specific commit from any branch onto your current branch. When two branches modify the same lines, Git marks the conflict with `<<<<<<<`, `=======`, `>>>>>>>` markers — resolve by choosing the correct code, deleting the markers, then `git add` and `git commit`.

**What You'll Learn:**
- How to use `git cherry-pick` to move commits between branches
- How to resolve merge conflicts by choosing the right version
- How to find and recover orphaned code from unmerged branches

**Reflection Questions:**
1. What is `git cherry-pick` and when would you use it instead of `git merge`?
2. How did you decide which storage implementation to keep during the merge conflict?
3. How would you prevent branches from being forgotten in a real project?

---

## Module 4: GitHub & Remote Workflows

**Core Skill:** Backing up work and collaborating through the cloud

Git on your local machine protects you from "oops, I deleted the file." GitHub protects you from "oops, my laptop died." This module teaches you to push with purpose, verify your backups work, and fix the common problems that arise when local and remote get out of sync.

---

### Exercise 4.1 — Cloud Safety Net

**The Problem:** You have a portfolio website project. It works locally, but if your computer dies, everything is lost. You need to push it to GitHub, but first you need to make sure your secrets file doesn't go with it.

**Your Task:** Initialize with `.gitignore` protecting secrets, push to a new GitHub repository, verify the backup works by cloning to a different folder, and establish the push-verify-pull cycle.

**What You'll Learn:**
- How to push a local repository to GitHub for the first time
- How to verify that your backup actually works (cloning to a test folder)
- The push-verify-pull cycle for ongoing development

**Starter Prompt (Intentionally Vague):**
> "Put this on GitHub"

**Better Prompt (Build Toward This):**
> "I need to push my portfolio project to a new public GitHub repo. The project has a secrets.json that must NOT be pushed. Help me: 1) verify .gitignore excludes secrets.json, 2) create the repo with gh cli, 3) push with -u flag, 4) verify the push by checking what's on GitHub."

**Reflection Questions:**
1. If you accidentally pushed secrets to GitHub, what would you need to do?
2. What is the difference between `git push -u origin main` and subsequent `git push` calls?
3. Why did we clone to a separate folder to verify the backup?

---

### Exercise 4.2 — Remote Troubles

**The Problem:** Three scenarios: (A) your local branch is "master" but GitHub expects "main," (B) your remote URL points to the wrong repository, and (C) your push is rejected because the remote has commits you don't have.

**Your Task:** Run each setup script to create the problem, diagnose it with `git branch`, `git remote -v`, and `git log`, then fix it using the appropriate command.

**What You'll Learn:**
- How to rename branches for GitHub compatibility
- How to manage remote URLs (view, change, remove)
- Why pushes get rejected and how to resolve it safely (pull before push)

**Reflection Questions:**
1. How do you configure Git to always use "main" for new repos?
2. What is the difference between `git pull` and `git pull --rebase`?
3. Why is `git push --force` almost never the right answer?

---

## Module 5: Pull Requests & Code Review

**Core Skill:** Reviewing code professionally with AI transparency

Pull requests are where individual work becomes team work. A good PR tells reviewers what changed, why it changed, and whether AI was involved. A bad PR wastes everyone's time and hides important information. This module teaches you to write PRs that people actually want to review.

---

### Exercise 5.1 — Transparent PR

**The Problem:** You have a calculator with a feature branch adding error handling. The error handling was largely generated by AI. You need to create a pull request that honestly documents which parts AI wrote, which parts you wrote, and how you verified the AI output.

**Your Task:** Create the feature branch, use AI to add error handling, review the diff, create a PR using the provided AI transparency template, and self-review your own work.

**What You'll Learn:**
- How to create a pull request with a feature branch
- How to write an honest AI disclosure section
- How to self-review a diff before asking others to review

**Starter Prompt (Intentionally Vague):**
> "Make a PR"

**Better Prompt (Build Toward This):**
> "I have a feature branch 'feature/error-handling' with AI-generated input validation. Help me write a PR description using the template in pr-template.md. I need to be specific about: which functions AI wrote the validation for, what I changed after reviewing, and how I tested the edge cases."

**Reflection Questions:**
1. Why is AI transparency in PRs important for code review?
2. Was it uncomfortable to specifically list what AI wrote? Why is that specificity valuable?
3. Did self-review catch anything you missed before?

---

### Exercise 5.2 — PR Cleanup

**The Problem:** Three bad PRs need fixing. PR #1 changes 47 files with the description "Updated code." PR #2 has sophisticated AI-generated authentication code with no AI disclosure. PR #3 has failing CI checks that the author wants to ignore.

**Your Task:** Read each PR and its simulated reviewer comments, identify all the problems, and write improved descriptions that fix the issues.

**What You'll Learn:**
- What makes a PR description useful vs. useless
- Why hiding AI usage is a transparency problem, not a quality problem
- Why merging with failing checks creates a broken window for the whole team

**Reflection Questions:**
1. Which of the three bad PRs is most dangerous? Why?
2. PR #2 has working code. Why isn't "it works" sufficient justification?
3. How can you tell a flaky test from a real performance problem?

---

## Module 6: Workflow Documentation

**Core Skill:** Capturing reusable patterns from experience

A Git workflow document is the difference between a team that collaborates smoothly and one that constantly trips over each other. This module teaches you to write workflow documents that actually prevent problems, and to audit existing documents for the gaps that cause incidents.

---

### Exercise 6.1 — Workflow Builder

**The Problem:** A new e-commerce project is starting with 4 people across 4 timezones. They need a Git workflow document before writing a single line of code. The document must handle branching, commits, PRs, AI usage, and emergency procedures — and it must be realistic for a team with minimal overlapping availability.

**Your Task:** Read the project description, requirements, and team info, then create a comprehensive `git-workflow.md` that accounts for the team's real constraints.

**What You'll Learn:**
- How to structure a workflow document that teams actually follow
- How timezone constraints affect PR review processes
- How to write AI usage policies that balance transparency with productivity

**Starter Prompt (Intentionally Vague):**
> "Write a workflow doc"

**Better Prompt (Build Toward This):**
> "I'm creating a Git workflow document for a 4-person team across UTC-5, UTC-8, UTC+0, and UTC+5:30. They have 1 hour of weekly overlap. The project is an 8-week e-commerce MVP with frontend and backend. I need sections for: branching strategy, commit conventions, PR process (accounting for async review), AI usage policy, push schedule, and emergency procedures. Focus on practical rules that work for a distributed team."

**Reflection Questions:**
1. Which section was hardest to write? Why?
2. How does limited timezone overlap change your PR review process?
3. Is your AI usage policy strict enough to prevent the problems from Exercise 5.2?

---

### Exercise 6.2 — Pattern Audit

**The Problem:** A team's Git workflow document has subtle inconsistencies and missing rules that caused three real incidents: a silent breaking change pushed directly to main, AI-generated code merged without review, and a hotfix chain that made things worse.

**Your Task:** Read the workflow document first (noting suspicions), then read each incident report, trace each incident to a specific workflow rule (or missing rule), and produce both an audit findings document and a corrected workflow.

**What You'll Learn:**
- How to find contradictions in team documentation
- How to trace incidents to root cause workflow failures
- How to write rules that prevent real problems without creating bureaucracy

**Reflection Questions:**
1. Were your initial suspicions correct before reading the incidents?
2. Why do well-intentioned "efficiency shortcuts" often cause more problems?
3. How would you introduce workflow changes to a team already using the broken version?

---

## Module 7: Capstone Projects

These capstones integrate all skills from Modules 1-6. Attempt them after completing all previous modules.

---

### Capstone A — Full Stack Git Journey

**The Problem:** You need to build a complete project from empty folder to professional GitHub repository, exercising every Git skill along the way.

**Your Task:** Build a Contact Manager (Python CLI app) through the complete lifecycle: initialize with `.gitignore`, create structured commits, develop features on branches, merge with review, push to GitHub, create a PR with AI transparency, and write workflow documentation.

**What You'll Learn:**
- How all Git workflows connect in a real project
- The rhythm of professional version control
- How to maintain quality across an entire project lifecycle

**Time estimate:** 2-4 hours

**Deliverables:** Repository with 8+ commits, 2+ merged branches, GitHub push, 1 PR with AI disclosure, CONTRIBUTING.md

---

### Capstone B — Portfolio Launch

**The Problem:** You need a professional GitHub presence with multiple clean repositories, but you've been learning — your existing work might have messy history, missing READMEs, or no AI disclosure.

**Your Task:** Create 3 GitHub repositories with clean histories and proper READMEs (using provided templates), plus a profile README that links everything together.

**What You'll Learn:**
- How to present yourself professionally on GitHub
- How to create clean history intentionally (even if your learning process was messy)
- How to write READMEs that a stranger can follow

**Time estimate:** 2-4 hours

**Deliverables:** 3 GitHub repos with READMEs and AI disclosure, profile README at github.com/USERNAME

---

### Capstone C — Git Forensics

**The Problem:** A repository has been through multiple disasters. Secrets were committed and then "deleted" (but are still in history). A force-push destroyed a junior developer's work. Feature branches were abandoned with useful code. A revert was made with no explanation.

**Your Task:** Run `setup.sh` to create the crime scene, then investigate every layer using Git forensic commands. Produce a comprehensive forensic report with timeline, findings for each problem, and a recovery plan.

**What You'll Learn:**
- Advanced Git investigation techniques (reflog, log filtering, show)
- How to find secrets in Git history even after they've been "deleted"
- How to recover lost work from force-pushes and abandoned branches
- How to write an actionable recovery plan

**Time estimate:** 2-4 hours

**Deliverables:** Forensic report with 4 findings, timeline of events, recovery plan with immediate/short-term/process improvements

---

## What's Next?

After completing these exercises, you should be able to:

- Initialize any project with proper Git structure on the first try
- Use branches to experiment fearlessly with AI-generated code
- Recover from any common Git mistake in under 2 minutes
- Push to GitHub with confidence that secrets are protected
- Write pull requests that teammates actually want to review
- Create workflow documents that prevent real problems

The next step is to use these skills in your own projects. Every time you start a new project, run through the Git Safety Framework. Every time you ask AI for help, review the diff before committing. Every time you push to GitHub, verify the push worked.

Git mastery comes from repetition, not memorization. The more you practice these workflows, the more automatic they become.

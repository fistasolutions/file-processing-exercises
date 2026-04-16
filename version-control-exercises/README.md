# Version Control & Safe Experimentation — Exercise Pack

**Exercises for the Version Control & Safe Experimentation chapter: Master Git workflows for AI-assisted development through hands-on practice**

_By Muhammad Usman Akbar — Learn by Doing, Not by Reading_

---

## Package Structure

```
claude-code-version-control-exercises/
├── EXERCISE-GUIDE.md                          # Full guide with all exercises
├── README.md                                   # This file
├── module-1-repo-foundations/
│   ├── exercise-1.1-project-kickoff/           # Build: Initialize a repo properly
│   └── exercise-1.2-repo-rescue/               # Debug: Fix a messy repo with secrets
├── module-2-change-tracking/
│   ├── exercise-2.1-ai-review-workflow/        # Build: Review-before-commit discipline
│   └── exercise-2.2-recovery-room/             # Debug: Three recovery scenarios
├── module-3-branch-strategies/
│   ├── exercise-3.1-three-approaches/          # Build: Parallel branching for competing ideas
│   └── exercise-3.2-branch-tangle/             # Debug: Untangle misplaced commits & conflicts
├── module-4-github-remote/
│   ├── exercise-4.1-cloud-safety-net/          # Build: Push to GitHub, verify backup
│   └── exercise-4.2-remote-troubles/           # Debug: Fix branch/remote/push problems
├── module-5-pull-requests/
│   ├── exercise-5.1-transparent-pr/            # Build: Create a PR with AI transparency
│   └── exercise-5.2-pr-cleanup/                # Debug: Fix three bad PR descriptions
├── module-6-workflow-docs/
│   ├── exercise-6.1-workflow-builder/          # Build: Create a team workflow document
│   └── exercise-6.2-pattern-audit/             # Debug: Find gaps that caused incidents
└── module-7-capstones/
    ├── capstone-A-full-stack-journey/          # Complete Git lifecycle in one project
    ├── capstone-B-portfolio-launch/            # Build a professional GitHub presence
    └── capstone-C-git-forensics/              # Investigate a crime-scene repository
```

## How to Get Started

### With Claude Code (Terminal) — Recommended

1. Open your terminal
2. Navigate to the exercise folder: `cd module-1-repo-foundations/exercise-1.1-project-kickoff/`
3. Read the instructions: `cat INSTRUCTIONS.md`
4. Start Claude Code and work through the exercise
5. Use Git commands directly in the terminal

## Recommended Order

Work through one module per session. Each module has two exercises:
- **X.1 (Build)** — Create something from scratch. Do this first.
- **X.2 (Debug)** — Fix something broken. Apply what you learned in X.1.

| Session | Module | Time Estimate |
|---------|--------|---------------|
| 1 | Module 1: Repository Foundations | 60-90 min |
| 2 | Module 2: Change Tracking & Recovery | 60-90 min |
| 3 | Module 3: Branch Strategies | 60-90 min |
| 4 | Module 4: GitHub & Remote Workflows | 60-90 min |
| 5 | Module 5: Pull Requests & Code Review | 60-90 min |
| 6 | Module 6: Workflow Documentation | 60-90 min |
| 7 | Module 7: Capstone (pick one) | 2-4 hours |

## The Git Safety Framework

Use this mental checklist for every exercise:

1. **Assess** — What's the current state? (`git status`, `git log`, `git branch`)
2. **Plan** — What needs to happen? What's the safest path?
3. **Protect** — Create a safety net before risky changes (commit, branch, backup)
4. **Execute** — Run the commands with intention
5. **Verify** — Did it work? Check status, diff, log
6. **Document** — Record what happened and why (commit messages, workflow docs)

## Prerequisites

- Git installed (`git --version`)
- Python 3.10+ installed (`python --version`)
- GitHub account (for Modules 4-5 and Capstones B-C)
- GitHub CLI recommended (`gh --version`)
- Claude Code access

## Important Notes

- All API keys and secrets in these exercises are FAKE. They use the pattern `FAKE-*-for-exercise`.
- Setup scripts (`setup.sh`) create isolated Git repositories. They won't affect your other work.
- Each exercise is self-contained. You can skip ahead if you already know a topic.
- The capstones integrate all skills — attempt them only after completing Modules 1-6.

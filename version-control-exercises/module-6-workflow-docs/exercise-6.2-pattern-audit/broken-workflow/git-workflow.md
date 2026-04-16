# Team Git Workflow

## Branching Strategy

We use feature branches for all new work. Always branch from `main`.

Branch naming convention:
- Features: `feature/description`
- Bug fixes: `fix/description`
- Experiments: `experiment/description`

## Commit Messages

Use descriptive commit messages. Follow the format:
```
type: short description

Longer explanation if needed.
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

## When to Commit

Commit early and often. Every logical change should be its own commit.

## Pushing to Main

For small bug fixes (under 5 lines), commit directly to main. No PR needed.
This saves time for trivial changes.

For everything else, create a pull request.

## Pull Requests

All PRs need at least 1 approval before merging.

PR description should include:
- What changed
- Why it changed
- How to test it

## Code Review

Reviews should be completed within 48 hours. If no review after 48 hours,
the author can merge without approval.

## Merge Strategy

Use "Squash and Merge" for feature branches to keep main history clean.

Exception: For branches with multiple meaningful commits, use regular merge.

## Resolving Conflicts

If your branch has conflicts with main:
1. Merge main into your branch
2. Resolve conflicts
3. Push and continue with PR

## Hotfixes

For critical production bugs:
1. Branch from main
2. Fix the issue
3. Push directly to main (skip PR for speed)
4. Create a PR afterward for documentation

## AI Usage

When using AI tools (Claude Code, Copilot, etc.):
- It's fine to use AI for any code
- No special documentation needed
- Just make sure the code works

## Testing

Run tests before pushing. If tests fail, fix them before creating a PR.

Exception: If the failing test is unrelated to your change, note it in the
PR and proceed.

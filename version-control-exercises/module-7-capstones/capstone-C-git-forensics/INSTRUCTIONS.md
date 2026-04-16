# Capstone C — Git Forensics

**Investigation:** Analyze a crime scene repository, document all findings, and write a recovery plan

## Goal

A repository has been through multiple disasters: secrets committed (then "deleted"), a force-push that destroyed work, abandoned branches, and a mysterious revert. Use Git forensic tools to investigate every layer of problems and produce a comprehensive report.

## Estimated Time: 2-4 hours

## What You Have

```
crime-scene/
└── setup.sh    # Creates the forensic scenario (run this first)
```

## Phase 1: Create the Crime Scene

```bash
cd crime-scene
chmod +x setup.sh
bash setup.sh
cd crime-scene-repo
```

## Phase 2: Initial Survey

### Step 1: Map the repository

```bash
git log --all --oneline --graph --decorate
git branch -a
git log --all --format="%H %ae %s" | head -20
```

Record:
- How many branches exist?
- How many total commits?
- How many different authors?
- What's the overall shape of the history?

### Step 2: Timeline reconstruction

```bash
git log --all --oneline --date=short --format="%ad %ae %s" | sort
```

Create a timeline of events in chronological order.

## Phase 3: Investigation

### Crime 1: Secrets in History

Even though `.env` was deleted, it's still in the git history.

```bash
# Find commits that touched .env
git log --all --diff-filter=A -- '.env'
git log --all --diff-filter=D -- '.env'

# View the original .env contents
git show <commit-that-added-env>:.env
```

Document: What secrets were exposed? When were they committed? When were they "removed"?

### Crime 2: The Force Push

```bash
# Look for signs of lost work
git branch -a
git reflog
git log backup-before-force-push --oneline
git log main --oneline

# Compare what was lost
git diff main..backup-before-force-push
```

Document: What commits were lost? Who wrote them? Can the work be recovered?

### Crime 3: Abandoned Feature Branches

```bash
# Check each branch
git log feature-departments --oneline
git log feature-export --oneline

# What code is on these branches but not on main?
git diff main..feature-departments
git diff main..feature-export
```

Document: What useful code is stranded? Should it be merged?

### Crime 4: The Mysterious Revert

```bash
# Find the revert
git log --oneline | grep -i revert

# What was reverted?
git show <revert-commit-hash>
```

Document: What was reverted and why? (Note: there's no explanation. That's part of the problem.)

## Phase 4: Write the Forensic Report

Create `forensic-report.md` in the crime scene directory with:

```markdown
# Git Forensic Report

## Executive Summary
[2-3 sentences summarizing the overall state of the repository]

## Timeline of Events
[Chronological list of everything that happened]

## Finding 1: Exposed Secrets
- What was exposed: [list all secrets found]
- When committed: [date/commit]
- When "removed": [date/commit]
- Still recoverable: [yes/no and how]
- Risk assessment: [what damage could these cause]
- Remediation: [what needs to happen]

## Finding 2: Lost Work (Force Push)
- Commits lost: [list with descriptions]
- Author affected: [who]
- Recoverable: [yes/no, from which branch]
- Code review: [was the lost code good? should it be restored?]

## Finding 3: Abandoned Branches
- Branches found: [list]
- Useful code identified: [what's worth saving]
- Recommendation: [merge, cherry-pick, or delete]

## Finding 4: Unexplained Revert
- What was reverted: [feature description]
- Commit hash: [hash]
- Documentation: [none found — this is a problem]
- Recommendation: [investigate why, potentially re-apply]

## Recovery Plan
### Immediate Actions (Do Now)
1. [action]
2. [action]

### Short-Term Actions (This Week)
1. [action]
2. [action]

### Process Improvements (Prevent Recurrence)
1. [action]
2. [action]

## Appendix: Commands Used
[List the git commands you used during investigation]
```

## Phase 5: Execute Recovery (Optional Challenge)

If you want to go further, actually implement the recovery:

1. Rotate the exposed secrets (in a real scenario)
2. Recover the lost work from `backup-before-force-push`
3. Merge useful code from abandoned branches
4. Document the revert decision (or re-apply the reverted feature)

## Deliverables Checklist

- [ ] Forensic report (`forensic-report.md`) with all 4 findings
- [ ] Timeline of events
- [ ] Recovery plan with immediate, short-term, and process improvements
- [ ] List of all git commands used during investigation
- [ ] (Optional) Recovery actually implemented

## Verification

```bash
# Report should exist and be comprehensive
wc -l forensic-report.md
# Should be 80+ lines

# Should cover all 4 findings
grep "Finding" forensic-report.md | wc -l
# Should be 4

# Should have a recovery plan
grep -c "Recovery Plan" forensic-report.md
# Should be 1
```

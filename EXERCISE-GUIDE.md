# File Processing Workflows -- Practice Exercises

## From Chaos to System: Master File Management Through Agent Collaboration

**By Muhammad Usman Akbar -- Learn by Doing, Not by Reading**

---

## How This Guide Works

Every module in this guide follows a consistent pattern: **X.1 is a Build exercise** where you apply a workflow to real files, and **X.2 is a Debug exercise** where you diagnose what went wrong in a scenario someone else created. Build exercises develop your ability to execute workflows correctly. Debug exercises develop your ability to think critically about file operations -- a skill that matters even more, because in professional work, you spend more time fixing problems than creating from scratch.

Three core skills run through every exercise. First, **problem investigation before action**: you will learn to survey, count, measure, and understand before touching a single file. Second, **safety-first operations**: you will internalize the habit of creating backups and verification checkpoints before any destructive change. Third, **systematic file workflow execution**: you will move from ad-hoc file management to repeatable, documented processes that work the same way every time.

**Tool guidance**: Use **Claude Code** for all exercises. These exercises involve real file operations -- creating, moving, renaming, comparing, and searching files in a terminal environment. Claude Code is purpose-built for this kind of work. You can optionally use **Cowork** for planning-heavy exercises (like 3.2 where you analyze conflicting rules), but Claude Code is strongly preferred since even planning exercises benefit from testing plans against real files immediately.

Every exercise includes starter files that simulate realistic scenarios. You will work with inherited codebases, freelancer file dumps, photo libraries, corrupted backups, and disorganized archives. The files are designed to contain the same kinds of edge cases and messiness you encounter in real work -- because that is where the learning happens.

---

## File Processing Framework

Every file operation in this course follows a 7-step framework. Memorize this. It becomes second nature.

### Step 1: Survey
**What files exist? How many? How big? What types?**

Before you change anything, understand what you are working with. Use `ls`, `find`, `wc`, `du`, and `file` commands to build a complete picture. Count files by type. Measure total size. Check for hidden files. Note the deepest nesting level. This step takes 2-5 minutes and prevents hours of wrong-direction work.

### Step 2: Backup
**Create a safety net before any changes.**

Copy the entire working directory to a timestamped backup location. Verify the backup by comparing file counts and sizes. A backup you have not verified is not a backup -- it is a hope. Use `cp -r` with verification, or `rsync` for more control. Document your backup location.

### Step 3: Plan
**Design rules and approach before executing.**

Write down your categorization rules, naming convention, or transformation logic BEFORE running any commands. Rules should be unambiguous, complete (with a fallback for edge cases), and testable. Save your rules in a file -- they become reusable templates.

### Step 4: Test
**Try on ONE file first.**

Pick a representative file and run your planned operation on just that one file. Check the result. Did the file end up where you expected? Is the name correct? Did permissions survive? If the test fails, fix your plan before proceeding. One failed test is cheap. A failed batch operation is expensive.

### Step 5: Execute
**Run the batch operation.**

With your plan validated on a single file, execute the full operation. Use scripts or Claude Code's batch capabilities rather than manual repetition. Log what happens -- you will need the log if anything goes wrong.

### Step 6: Verify
**Compare results against expectations.**

After execution, verify the outcome matches your plan. Count files in the destination. Check for files left behind in the source. Compare against your pre-operation survey. Verification is not optional -- it is where you catch the 5% of files that did not match your rules.

### Step 7: Document
**Save rules, logs, and templates for reuse.**

Write a brief summary of what you did, what rules you used, and any edge cases you encountered. Save your scripts. This documentation converts a one-time cleanup into a repeatable system. Next time you face a similar problem, you have a template.

---

## Assessment Rubric

Use this rubric to self-assess your work on each exercise. Be honest -- the point is growth, not grades.

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|-------------|-----------------|-----------------|---------------|
| **Investigation Quality** | Runs `ls` once and starts working | Surveys files and sizes before acting | Full inventory with types, sizes, dates, and nesting depth | Discovers hidden files, symlinks, edge cases, and potential duplicates |
| **Safety Practices** | No backup before changes | Copies some files as backup | Complete backup with file count and size verification | Timestamped backup with integrity check, rollback plan, and documented restore procedure |
| **Workflow Execution** | Random commands without clear sequence | Follows framework steps but skips verification | Complete 7-step workflow with verification at each stage | Adapts workflow dynamically when edge cases surface |
| **Problem Diagnosis** | Guesses at what went wrong | Identifies obvious problems (missing files, wrong names) | Traces root cause systematically using logs and diffs | Identifies root cause AND implements prevention measures |
| **Documentation** | No record of what was done | Basic notes about commands run | Reusable rules file and operation log | Complete system with rules, logs, recovery plan, and templates for future use |

**Scoring guide:**
- 5-8 points: Revisit the chapter material and retry the exercise
- 9-12 points: Solid foundation -- move to the next module
- 13-16 points: Strong execution -- try the capstones
- 17-20 points: Ready to build file processing workflows for others

---

## Module 1: File Investigation

> **Core Skill**: Understanding what you have before changing anything
>
> **Covers**: Lessons 0-1 (The Hidden Cost of File Chaos, Your First File Investigation)

Before you can organize, rename, backup, or search files, you need to know what you are working with. Module 1 builds the investigation habit -- the discipline of surveying a folder completely before touching anything. This is the skill that separates professionals from amateurs. Amateurs dive in and start moving files. Professionals spend 5 minutes understanding the landscape and save hours of rework.

---

### Exercise 1.1 -- The Project Handoff (Build)

**Time**: 30-45 minutes

**The Problem**: You have inherited a project folder from a departing colleague. The `messy-project/` folder has 40+ files across nested directories -- source code, configs, documentation, image assets, test data, deployment scripts, and scattered notes. There is no README explaining the project structure. There is no handoff document. Your colleague's last day was yesterday.

Before you can contribute to this project, you need a complete map of what is in the folder. You cannot afford to miss a config file with production credentials or overlook a script that the deploy process depends on.

**Your Task**: Use Claude Code to survey the entire `messy-project/` folder structure. Create a `FILE-INVENTORY.md` document that catalogs:

- Total file count (including hidden files)
- File types breakdown (how many .py, .md, .yml, .csv, etc.)
- Size analysis (total size, largest files, smallest files)
- Directory structure with depth analysis (deepest nesting level)
- Largest 5 files by size
- Any potential duplicates (files with similar names or identical sizes)
- Suspicious files (backup files, temp files, files that might contain secrets)
- Files that appear to be stale or unused

**Starter Prompt** (vague -- see what happens):
> "Look at the messy-project folder and tell me what's in it."

**Better Prompt** (specific -- compare the difference):
> "I just inherited messy-project/ from a departing colleague. Before I touch anything, I need a complete inventory. Survey the entire directory tree -- count every file including hidden ones, break down by file type, find the largest files, check nesting depth, flag any files that look like they contain secrets or credentials, and identify potential duplicates or stale files. Output everything to FILE-INVENTORY.md in a format I can reference later."

**What You Will Learn**:
1. Investigation before action prevents costly mistakes -- you might discover a `prod.env` with real credentials that needs immediate attention
2. Bash commands (`find`, `wc`, `du`, `file`) are your eyes into a project's actual state -- GUI file browsers hide critical details
3. A 5-minute survey saves hours of wrong-direction work -- knowing the project has 6 Python files vs. 60 changes your entire approach

**Reflection Questions**:
1. What did you discover in the survey that would have surprised you if you had started editing files immediately? Were there files you did not expect?
2. Compare the output from the vague prompt vs. the specific prompt. What did the specific prompt catch that the vague one missed?
3. If you had to hand this project off to someone else tomorrow, what would you add to your FILE-INVENTORY.md that your colleague failed to create?

---

### Exercise 1.2 -- The Lying Inventory (Debug)

**Time**: 20-30 minutes

**The Problem**: A previous team member left an inventory report (`wrong-inventory.md`) that supposedly documents the contents of the `actual-files/` folder. Management has been relying on this report to make decisions about storage allocation and project planning. But you have a nagging suspicion the report is outdated -- and in your experience, outdated documentation is worse than no documentation because people trust it.

Your task is forensic: compare the report against reality and find every single discrepancy.

**Your Task**: Use Claude Code to systematically compare `wrong-inventory.md` against the actual contents of `actual-files/`. For each error you find, document:
- What the report claims
- What is actually true
- How you verified it (what command you ran)

Create a `DISCREPANCY-REPORT.md` with your findings.

**What You Will Learn**:
1. Never trust documentation without verification -- reports become stale the moment files change, and no one remembers to update them
2. Diff-ing expectations against reality is a core debugging skill that transfers to code, APIs, databases, and every other technical domain
3. Systematic comparison (going claim by claim) catches errors that casual browsing misses

**Reflection Questions**:
1. How many errors did you find? Were any of them the kind that could cause real problems (like the missing .env file)?
2. What process would you put in place to keep an inventory report accurate over time? Is manual maintenance realistic?
3. Could you write a script that generates an accurate inventory automatically? What would that script need to check?

---

## Module 2: Safety-First Backup

> **Core Skill**: Creating safety nets before any destructive operation
>
> **Covers**: Lesson 2 (Backup Before You Break Things)

The most dangerous moment in file management is right before you start changing things. You have surveyed the files, you have a plan, and you are eager to execute. This is exactly when mistakes happen -- because confidence outpaces caution. Module 2 builds the backup reflex: the automatic habit of creating a verified safety net before any operation that could lose data.

---

### Exercise 2.1 -- The Migration Prep (Build)

**Time**: 30-45 minutes

**The Problem**: You are about to reorganize `migration-source/` -- a folder containing important project files. But this is not a simple folder of text files. It contains files with varied permissions, a configuration file that is actually a symlink to a shared config, one large data file (500+ rows of CSV), and hidden configuration files. A naive `cp -r` might miss hidden files, break symlinks, or silently fail on permission-restricted files.

You need a backup strategy that handles every edge case -- because you will only discover a backup is incomplete at the worst possible moment: when you need to restore from it.

**Your Task**:
1. Survey `migration-source/` completely (file count, sizes, hidden files, special files)
2. Create a timestamped backup (e.g., `migration-source-backup-2025-04-15-1430/`)
3. Verify completeness: file counts match, total sizes match, hidden files included
4. Handle edge cases: note the symlink situation, check the large file copied completely
5. Document your backup strategy in `BACKUP-STRATEGY.md` -- make it reusable for future migrations

**Note**: Git does not preserve symlinks well across platforms. The INSTRUCTIONS.md will guide you to create a symlink as part of the exercise setup.

**Starter Prompt** (vague):
> "Back up the migration-source folder."

**Better Prompt** (specific):
> "I need to create a verified backup of migration-source/ before reorganizing it. The folder has hidden files, at least one symlink, and a large CSV. Create a timestamped backup, then verify: file counts match (including hidden), sizes match, symlink is handled correctly, and the large CSV is complete. Document the strategy in BACKUP-STRATEGY.md so I can reuse it."

**What You Will Learn**:
1. Backups must be verified, not assumed -- `cp -r` can silently skip hidden files or break symlinks depending on flags used
2. Edge cases (symlinks, permissions, large files) break naive copy commands -- you need to know your tool's behavior
3. A documented backup strategy is reusable -- you built a template, not just made a copy

**Reflection Questions**:
1. What edge cases did you discover during backup that a simple `cp -r` would have missed?
2. How did you verify the backup was complete? What specific comparisons did you make?
3. If the backup needed to be restored 6 months from now by someone else, would your BACKUP-STRATEGY.md give them enough information?

---

### Exercise 2.2 -- The Incomplete Backup (Debug)

**Time**: 25-35 minutes

**The Problem**: A colleague created a backup of `original/` into `backup/`. They ran the copy command, saw no errors, and told you "everything is backed up." You are about to delete the `original/` folder to free up space. But something feels off -- the backup folder looks slightly smaller.

Before you delete anything, you need to verify the backup is actually complete. Your job is forensic: compare `original/` against `backup/`, find every discrepancy, diagnose why the backup failed, and fix it.

**Your Task**:
1. Compare `original/` against `backup/` using diff, file counts, and size comparisons
2. Identify every discrepancy (missing files, truncated files, empty files that should have content)
3. For each discrepancy, determine the likely cause (interrupted copy? hidden file missed? permission denied?)
4. Fix the backup so it matches the original exactly
5. Create a `BACKUP-AUDIT.md` documenting what you found and how you fixed it

**What You Will Learn**:
1. "I copied everything" is never enough -- always verify with systematic comparison
2. Common backup failure modes: hidden files skipped (no `-a` flag), permissions blocked copy (file created empty), interrupted operation (files missing), content truncated (disk full or timeout)
3. Forensic comparison is a transferable skill -- the same diff-and-diagnose approach works for database backups, API responses, and deployment artifacts

**Reflection Questions**:
1. How many discrepancies did you find? Which one would have caused the most damage if you had deleted the original?
2. What single command flag or approach would have prevented most of these backup failures?
3. Design a "backup verification checklist" that someone could follow after ANY backup operation. What are the minimum checks?

---

## Module 3: Organization Rules

> **Core Skill**: Designing categorization systems through collaborative refinement
>
> **Covers**: Lesson 3 (Collaborative Organization Systems)

Files do not organize themselves, and ad-hoc organization ("I'll just put it in the right folder") fails the moment you have more than 20 files or more than one person. Module 3 teaches you to design explicit, documented rules for categorization -- and more importantly, to stress-test those rules against real files before trusting them.

---

### Exercise 3.1 -- The Freelancer's Chaos (Build)

**Time**: 45-60 minutes

**The Problem**: A freelance designer's `freelancer-files/` folder has 60+ files accumulated over months of client work. Invoices (PDF), design mockups (PNG, PSD, SVG), contracts (DOCX, PDF), project assets (various formats), correspondence (TXT, MD), and miscellaneous junk are all mixed together in a single flat directory. No folders. No naming convention. No organization whatsoever.

The freelancer hired you to bring order to the chaos. But this is not just about moving files into folders -- it is about creating a SYSTEM that the freelancer can maintain after you leave.

**Your Task**: Collaborate with Claude Code to work through the complete organization workflow:
1. **Survey**: Catalog every file by type, identify clusters and patterns
2. **Design Rules**: Create categorization rules that handle ambiguity (a PDF could be an invoice OR a contract -- how do you decide?)
3. **Document Rules**: Write your rules in `organization-rules.md` with clear, unambiguous criteria
4. **Test**: Apply your rules to ONE file from each category and verify placement
5. **Execute**: Organize all 60+ files using your rules
6. **Verify**: Confirm every file ended up in the right place, no files lost

**What You Will Learn**:
1. Good rules handle ambiguity -- when a PDF could be an invoice or a contract, your rules need a tiebreaker (check filename keywords? check content? ask the user?)
2. Testing on one file per category before batch execution prevents disasters -- you discover rule gaps cheaply
3. Documented rules are reusable -- you built a system, not just cleaned up once. The freelancer can follow these rules for future files.

**Reflection Questions**:
1. Which files were hardest to categorize? What made them ambiguous, and how did your rules resolve the ambiguity?
2. If the freelancer gets 10 new files next week, can they follow your rules without asking you? What would make the rules clearer?
3. How would your rules change if this were a team of 3 freelancers sharing the same folder?

---

### Exercise 3.2 -- The Collision Course (Debug)

**Time**: 30-45 minutes

**The Problem**: An enthusiastic but inexperienced team member wrote `broken-rules.md` -- a set of file organization rules for the `unsorted-files/` folder. They were proud of their work. But when you read the rules carefully, you realize they are riddled with conflicts, gaps, and ambiguities. If someone followed these rules literally, files would end up in multiple folders, some files would have no destination, and naming collisions would destroy data.

Your job: find every problem, fix the rules, and prove your fixed version works by testing it against the actual files.

**Your Task**:
1. Read `broken-rules.md` and identify every conflict, gap, and ambiguity
2. Create `RULE-AUDIT.md` documenting each problem you found
3. Write `fixed-rules.md` with corrected, unambiguous, complete rules
4. Test the fixed rules against `unsorted-files/` to prove they work
5. For each fix, explain WHY the original rule was broken and what principle it violated

**What You Will Learn**:
1. Rule conflicts are the #1 source of organization failures -- overlapping categories mean files get duplicated or end up in arbitrary locations
2. Every rule set needs a fallback for unmatched files -- the "miscellaneous" or "unsorted" category is not a failure, it is a safety net
3. Testing rules against real data exposes problems that reading alone misses -- you cannot find gaps by staring at rules, you find them when a real .zip file has no matching rule

**Reflection Questions**:
1. How many distinct problems did you find in the original rules? Categorize them: conflicts, gaps, ambiguities, and other.
2. What is the minimum set of principles that prevents these kinds of rule failures? (Think: mutual exclusivity, completeness, fallback handling, case sensitivity)
3. Could you write a "rule validation checklist" that someone could use to audit ANY set of organization rules?

---

## Module 4: Batch Operations

> **Core Skill**: Transforming repetitive file tasks into systematic batch workflows
>
> **Covers**: Lesson 4 (Batch Rename and Transform)

One file at a time is fine for 5 files. It is not fine for 50. Module 4 builds the skill of converting manual, repetitive file operations into systematic batch workflows -- with the critical addition of preview-before-execute and rollback strategies. The difference between a batch operation and a disaster is verification at every step.

---

### Exercise 4.1 -- Photo Library Cleanup (Build)

**Time**: 40-50 minutes

**The Problem**: Your `photo-dump/` folder has 50+ photos and screenshots with wildly inconsistent names. Some have timestamps (`IMG_20250215_143022.jpg`), some have descriptive names (`2025-01-20 Project Meeting.png`), some have camera defaults (`DCIM_001.jpg`), some have no useful information at all (`unnamed.jpg`, `unnamed (1).jpg`). You want every file named with a consistent format: `YYYY-MM-DD_description.ext`.

But renaming 50+ files by hand is tedious and error-prone. And a bad batch rename can destroy your ability to find files -- or worse, overwrite files when two end up with the same name.

**Your Task**:
1. **Survey**: Catalog existing naming patterns -- how many different formats exist?
2. **Design Convention**: Define your target naming format and rules for extracting dates from different source formats
3. **Preview**: Generate a rename plan showing OLD NAME -> NEW NAME for every file WITHOUT executing
4. **Handle Edge Cases**: What about files with no date? Files that would get the same name? Files with wrong extensions?
5. **Execute**: Run the batch rename
6. **Verify**: Confirm all files renamed correctly, no files lost, no overwrites
7. **Script**: Save a reusable rename script or template for future use

**What You Will Learn**:
1. Preview before execute prevents disasters -- seeing "unnamed.jpg -> 2025-01-01_unnamed.jpg" BEFORE it happens lets you catch problems
2. Naming conventions must handle edge cases: files with no date get a fallback, duplicate names get a suffix, wrong extensions get flagged
3. A reusable script converts a one-time fix into permanent automation -- next time you dump photos, you run the script

**Reflection Questions**:
1. How many different naming formats did you find in the original files? Which was the hardest to parse?
2. What edge cases did you encounter that your initial plan did not account for? How did you adapt?
3. If you ran your rename script on a NEW batch of 50 photos, would it work without modifications? What assumptions does it make?

---

### Exercise 4.2 -- The Rename Disaster (Debug)

**Time**: 30-45 minutes

**The Problem**: Someone wrote a batch rename script and ran it on `mangled-files/`. The script had bugs. Now files have impossible dates in their names (`2025-13-45`), doubled date prefixes, stripped extensions, and -- worst of all -- some files were renamed to the same name, meaning earlier files were overwritten and lost.

Thankfully, the script generated `rename-log.txt` showing every rename operation it performed. This log is your lifeline for recovery.

**Your Task**:
1. Read `rename-log.txt` to understand what the script did
2. Identify which renames succeeded, which introduced errors, and which caused data loss
3. Categorize the bugs: date parsing errors, missing collision handling, extension stripping, double-application
4. Write a recovery script that undoes the damage where possible
5. For files that were overwritten (lost), document what happened and why recovery is impossible
6. Write `POST-MORTEM.md` explaining each bug and how to prevent it in future scripts

**What You Will Learn**:
1. Batch operations need rollback strategies -- without `rename-log.txt`, recovery would be impossible
2. Logs are not optional for batch operations -- they are your insurance policy
3. Common batch rename bugs: no collision handling (silent overwrite), wrong field parsed for date, regex that matches too broadly (strips extensions), idempotency failure (running twice doubles the date prefix)

**Reflection Questions**:
1. Which bug caused the most damage? Why? (Hint: data loss from overwrites is permanent)
2. What three safeguards would you add to any batch rename script to prevent these problems?
3. The log saved you here. Design a log format for batch operations that captures enough information for complete rollback.

---

## Module 5: Recovery and Search

> **Core Skill**: Recovering from disasters and finding needles in haystacks
>
> **Covers**: Lessons 5-6 (Recovery Workflows, Advanced Search)

Things go wrong. Files get flattened, moved to wrong locations, or buried in years of accumulation. Module 5 builds two related skills: reconstructing structure from chaos (recovery) and finding specific files in large collections (search). Both require systematic thinking -- guessing does not scale.

---

### Exercise 5.1 -- The Accidental Flatten (Build)

**Time**: 35-45 minutes

**The Problem**: Someone ran a command that moved ALL files from a nested directory structure into a single `flattened/` folder. Four levels of carefully organized nesting -- gone. Source code, tests, config files, and documentation are all jumbled together in one flat directory. Some files that had the same name in different directories (like `__init__.py`) now have numbers appended: `__init__.py`, `__init__ (1).py`, `__init__ (2).py`.

Luckily, there is a `backup/` folder that preserves the original structure. Your job: reconstruct the original directory tree from the flattened mess, using the backup as your reference.

**Your Task**:
1. **Survey the damage**: Count files in `flattened/`, identify name collisions (numbered duplicates)
2. **Study the backup**: Map the original directory structure from `backup/`
3. **Plan reconstruction**: For each file in `flattened/`, determine where it should go based on the backup structure
4. **Handle collisions**: Figure out which `__init__ (1).py` goes to which directory
5. **Execute reconstruction**: Recreate the directory structure and move files
6. **Verify**: Compare your reconstructed structure against `backup/` -- they should match exactly

**What You Will Learn**:
1. Flattening destroys information -- directory paths ARE metadata, and losing them is like losing column headers in a spreadsheet
2. Recovery requires both a reference (backup) AND systematic matching -- you cannot guess which `__init__.py` belongs where without comparing content
3. Verification after recovery is non-negotiable -- one misplaced file can break an entire project

**Reflection Questions**:
1. How did you determine which numbered file (`__init__ (1).py` vs `__init__ (2).py`) belonged in which directory?
2. What would you do if there were NO backup? What clues in the files themselves might help reconstruct the structure?
3. What command or process caused the original flattening? How would you prevent it from happening again?

---

### Exercise 5.2 -- The Tax Season Hunt (Search)

**Time**: 40-60 minutes

**The Problem**: It is tax season. Your accountant needs 5 specific documents. You have a `document-archive/` with 100+ files accumulated over 2 years, scattered across multiple subdirectories (`2024/`, `2025/`, `taxes/`, `receipts/`, `misc/`, `unsorted/`). The files are not consistently named, and some are in unexpected locations.

Your accountant described the documents they need:

1. "The PDF about Q3 dividends from my accountant" -- a summary of dividend income for Q3 2024
2. "The spreadsheet with monthly expenses from 2024" -- a tracking sheet with all monthly expenses
3. "That receipt from the office furniture purchase" -- a receipt for a desk or office equipment
4. "The contract with the freelance developer" -- an agreement with a developer named John
5. "The bank statement showing the large transfer in March" -- a March 2024 bank statement

You cannot search by exact filename because you do not know the exact names. You need to search by content, metadata, and context.

**Your Task**: For each of the 5 documents:
1. Describe your search strategy (what did you search for first?)
2. Show the search commands you used
3. Document what you found and how you confirmed it was the right file
4. If you found multiple candidates, explain how you narrowed down to the correct one

Create a `SEARCH-RESULTS.md` documenting your search process and findings.

**What You Will Learn**:
1. Descriptive search (searching by what a file IS, not what it is NAMED) is more powerful than filename search -- because file names are unreliable
2. Iterative refinement narrows results efficiently -- start broad ("all PDFs"), then narrow ("PDFs containing 'dividend'"), then verify
3. Combining file metadata (type, date modified, size) with content search (`grep`) finds needles in haystacks that neither approach alone could find

**Reflection Questions**:
1. Which document was hardest to find? What made it difficult -- misleading name, unexpected location, or ambiguous content?
2. What search strategy worked best overall: filename patterns, content grep, date-based filtering, or size-based filtering?
3. If you had to find documents in this archive regularly, what changes to file naming or folder structure would make searching easier?

---

## Module 6: Capstone Projects

> Choose one (or more). This is where everything comes together.
>
> Capstones are not graded exercises -- they are integration challenges that combine every skill from Modules 1-5.

---

### Capstone A -- The Full Pipeline

**Time**: 2-4 hours

**The Challenge**: Take the `messy-downloads/` folder (80+ files simulating a real Downloads folder) through the COMPLETE 7-step workflow:

1. **Survey**: Complete inventory of all 80+ files
2. **Backup**: Timestamped backup with verification
3. **Plan**: Design organization rules and naming conventions
4. **Test**: Apply rules to one file from each category
5. **Execute**: Organize and rename all files
6. **Verify**: Confirm everything landed correctly
7. **Document**: Save your complete system (rules, scripts, logs)

Do this in a single continuous Claude Code session. Document each step as you go.

**What You Will Learn**:
1. How the 7 steps chain together naturally -- each step's output becomes the next step's input
2. A complete pipeline is your template for any future file management task -- you are building a reusable process, not just cleaning up once
3. Real-world files are messier than exercises -- adapting your rules on the fly is the advanced skill

**Deliverable**: A fully organized folder plus a `PIPELINE-LOG.md` documenting every step.

---

### Capstone B -- The Team File System

**Time**: 2-3 hours

**The Challenge**: Read `team-scenario.md` describing a 3-person team's file management problems. Design a complete file management system:

- Folder structure (what directories exist and why)
- Naming conventions (per file type)
- Organization rules (where each type of file goes)
- Backup strategy (what, when, how)
- Search cheat sheet (how to find common files quickly)

This is not a one-time cleanup. You are designing a SYSTEM that three people with different workflows can all follow.

**What You Will Learn**:
1. Systems thinking vs. one-time fixes -- a system must work for files that do not exist yet
2. Rules must accommodate multiple people's workflows -- what works for a developer does not work for a designer
3. Documentation makes a system transferable -- if you get hit by a bus, can someone else maintain this?

**Deliverable**: A `TEAM-FILE-SYSTEM.md` document comprehensive enough for all three team members to follow independently.

---

### Capstone C -- Your Own Files

**Time**: 2-4 hours

**The Challenge**: Apply all seven workflow steps to your ACTUAL Downloads or Desktop folder. Real files. Real stakes.

**Rules**:
1. START WITH BACKUP. This is not negotiable. Back up your entire target folder before touching anything.
2. Work through all 7 steps: Survey, Backup, Plan, Test, Execute, Verify, Document.
3. Document everything in `MY-FILE-TOOLKIT.md` -- your personal file management system.
4. The goal is not just a clean folder. The goal is a documented SYSTEM for keeping it clean.

**What You Will Learn**:
1. Real files have edge cases that exercises cannot simulate -- your actual Downloads folder contains files you forgot about, files from applications you no longer use, and files with names in character sets you did not expect
2. Personal organization reveals which workflows matter most to YOU -- maybe you never batch rename, but you search constantly. Your toolkit should reflect YOUR patterns.
3. The toolkit you build is genuinely useful beyond this course -- this is not homework, it is a tool you will actually use

**Deliverable**: A clean folder AND a `MY-FILE-TOOLKIT.md` that documents your personal file management system.

---

## Assessment Summary

After completing exercises, score yourself on the rubric:

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|-------------|-----------------|-----------------|---------------|
| **Investigation Quality** | Runs `ls` once | Surveys files/sizes | Full inventory with types, sizes, dates | Discovers hidden files, symlinks, edge cases |
| **Safety Practices** | No backup | Copies some files | Complete backup with verification | Timestamped backup + integrity check + rollback plan |
| **Workflow Execution** | Random commands | Follows steps but skips verification | Complete workflow with verification | Adapts workflow to edge cases dynamically |
| **Problem Diagnosis** | Guesses at issues | Identifies obvious problems | Traces root cause systematically | Identifies root cause AND prevents recurrence |
| **Documentation** | No record | Basic notes | Reusable rules/templates | Complete system with rules + logs + recovery plan |

**Your journey**: File management is not glamorous. But the professional who can take 80 files of chaos and produce an organized, documented, maintainable system in under 2 hours has a skill that never goes out of demand. Every project you join, every team you work with, every migration you run -- the 7-step framework applies. Master it here, use it everywhere.

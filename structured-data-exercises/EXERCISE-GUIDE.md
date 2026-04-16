# Structured Data & Persistent Storage -- Practice Exercises

**From CSV chaos to production databases: build, debug, and deploy real data applications**

_By Muhammad Usman Akbar -- Learn by Building, Not by Reading_

---

## How This Guide Works

These are technical exercises for Chapter 9 of the Muhammad Usman Akbar AI-Native Development Curriculum. They cover the full arc of database development: designing data models with SQLAlchemy ORM, implementing CRUD operations, configuring relationships between entities, protecting data integrity with transactions, deploying to Neon PostgreSQL in the cloud, and verifying results using hybrid SQL+bash pipelines.

Each module contains two exercises: a **BUILD** exercise where you create something from requirements, and a **DEBUG** exercise where you fix broken code that already exists. Build exercises test your ability to translate requirements into working database code. Debug exercises test your ability to read error messages, trace root causes, and apply precise fixes without introducing new problems.

Three core skills run through every exercise: **data modeling** (choosing the right types, constraints, and relationships to represent real-world entities), **database operations** (creating, reading, updating, and deleting records with proper session management), and **production deployment** (configuring connection pooling, environment variables, and cloud databases for real applications).

All exercises require Claude Code as your development environment. You will write Python, execute SQL, run bash commands, and test your work -- all from the terminal. There is no GUI. There is no hand-holding. You read the instructions, you build the thing, you verify it works.

---

## The Database Development Framework

Use this for every exercise:

1. **Model** -- Define the data structure: what entities exist? What are their attributes and relationships?
2. **Connect** -- Establish the database connection: engine, session, connection pooling.
3. **Operate** -- Implement CRUD operations with proper session management.
4. **Protect** -- Add transaction safety: try/except, commit/rollback, validation.
5. **Verify** -- Test the implementation: run queries, check results, verify edge cases.
6. **Deploy** -- Move to production: environment variables, connection pooling, cloud database.

Not every exercise uses all six steps. Modules 1-2 focus on Model and Operate. Module 4 is all about Protect. Module 5 is Deploy. Module 6 is Verify. But the framework gives you a mental checklist to make sure nothing gets missed.

---

## Assessment Rubric

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Data Modeling** | Models have wrong types or missing constraints | Models work but miss edge cases (nullable, unique) | Models correctly represent entities with appropriate types and constraints | Models include indexes, defaults, and handle real-world edge cases |
| **Session Management** | Sessions left open or never committed | Sessions committed but no error handling | Proper context managers with try/except/rollback | Sessions optimized with flush, bulk operations, and connection reuse |
| **Relationship Design** | No relationships defined; manual ID filtering | Relationships defined but not bidirectional | Full bidirectional relationships with appropriate cascade behavior | Relationships include lazy loading strategy and optimized query patterns |
| **Transaction Safety** | No error handling around database operations | Try/except exists but rollback missing or incorrect | All multi-step operations wrapped in atomic transactions with rollback | Savepoints used for batch operations; validation before transaction starts |
| **Debugging Accuracy** | Unable to identify bugs in provided code | Identifies some bugs but misses root causes | Identifies all bugs and applies correct fixes | Identifies bugs, explains root cause, and suggests prevention patterns |

---

## Module 1: Data Modeling

> **The foundation of every database application is its data model. Get this wrong, and everything built on top of it will fight you.**

In this module, you will design SQLAlchemy models from scratch and fix broken ones. You will learn to choose the right column types, apply constraints that enforce data integrity, and connect tables using foreign keys.

---

### Exercise 1.1 -- Library Catalog

**Build**: Data Modeling -- Design SQLAlchemy models from a business requirements document

**The Problem:** Your local library needs a digital catalog system. They have been tracking books in a spreadsheet, but duplicates are everywhere, author information is inconsistent, and there is no way to filter by genre. They have written up their requirements and handed them to you. Your job: turn those requirements into a proper database schema using SQLAlchemy ORM.

**Your Task:**

1. Read the `requirements.md` file carefully. Pay attention to every attribute, every constraint, and every relationship mentioned.
2. Create a new file called `models.py` with three model classes: `Book`, `Author`, and `Genre`.
3. Choose the correct SQLAlchemy column types for each attribute (String, Integer, Text, etc.).
4. Add constraints: which fields should be unique? Which should be non-nullable? What are reasonable string lengths?
5. Add ForeignKey columns to connect Books to Authors and Books to Genres.
6. Create an in-memory SQLite engine, call `Base.metadata.create_all(engine)`, and insert at least 3 sample records to verify your models work.

**What You'll Learn:**
- How to translate business requirements into SQLAlchemy column definitions
- The difference between String, Text, Integer, and other column types -- and when to use each
- Why constraints (unique, nullable, foreign key) prevent data corruption before it happens

**Starter Prompt:**
> Read requirements.md and create SQLAlchemy models for this library system. Make sure to use appropriate column types and constraints.

**Better Prompt:**
> Read requirements.md. Then create a models.py file with SQLAlchemy ORM models for Book, Author, and Genre. For each attribute in the requirements, choose the most appropriate column type and add constraints (unique, nullable, max length) based on the business rules described. After defining the models, write a test script at the bottom of the file that creates tables in an in-memory SQLite database and inserts 3 sample records to verify everything works. Show me the output of running the file.

**Reflection Questions:**
1. Which column type decisions required judgment (not just "obviously String or Integer")? What made those decisions harder?
2. If the library later wants to allow books with multiple authors, which part of your schema would need to change?
3. What would happen if you forgot to add `nullable=False` to `Book.title`? How would that manifest as a real-world data problem?

---

### Exercise 1.2 -- Broken Pet Store

**Debug**: Data Modeling -- Find and fix 6 bugs in SQLAlchemy model definitions

**The Problem:** A pet store management system has been developed, but nothing works. The models were written by someone who was learning SQLAlchemy for the first time, and they made mistakes in imports, attribute names, column types, foreign keys, and constraints. The test suite catches all 6 bugs -- your job is to make every test pass.

**Your Task:**

1. Run `python test_models.py` and observe the errors. Read each error message carefully.
2. Open `broken_models.py` and trace each error back to the specific line causing it.
3. Fix all 6 bugs. Each bug is a different type of mistake -- do not assume they are all the same kind of error.
4. After each fix, re-run the tests to confirm that specific error is resolved.
5. Continue until all tests pass with zero errors.

**What You'll Learn:**
- How to read SQLAlchemy error messages and trace them to specific model definitions
- The six most common mistakes beginners make when defining ORM models
- Why running tests incrementally (fix one, re-run) is more effective than trying to fix everything at once

**Starter Prompt:**
> Run the tests and fix the bugs in broken_models.py.

**Better Prompt:**
> Run `python test_models.py` and show me the first error. Then open `broken_models.py` and identify the specific line causing that error. Fix it, re-run the tests, and repeat until all tests pass. For each bug you fix, tell me: (1) the error message, (2) the root cause, and (3) your fix. Do not fix multiple bugs at once -- go one at a time so I can see the progression.

**Reflection Questions:**
1. Which bug was hardest to identify from the error message alone? Why?
2. If you were writing a code review checklist for SQLAlchemy models, what 3 items would you always check?
3. How does the `__tablename__` attribute relate to what you see in the actual database? What happens if you get it wrong?

---

## Module 2: CRUD Operations

> **A model without operations is a blueprint without a building. CRUD -- Create, Read, Update, Delete -- is how your application actually interacts with data.**

In this module, you will implement the four fundamental database operations and learn proper session management. You will also debug common mistakes in query construction and session handling.

---

### Exercise 2.1 -- Recipe Book

**Build**: CRUD Operations -- Implement create, search, import, and aggregate functions for a recipe database

**The Problem:** A cooking app needs a backend database for its recipe collection. The data models are already built and a CSV file of 50+ recipes is ready to import. Your job is to write the functions that create recipes, search with filters, bulk import from CSV, and generate statistics -- all with proper session management.

**Your Task:**

1. Read `models.py` to understand the Recipe and Tag models (they are already correct -- do not modify them).
2. Read `recipes.csv` to understand the data format and column mapping.
3. Create a new file called `crud.py` with these functions:
   - `create_recipe(session, title, cuisine, prep_time_minutes, difficulty, ingredients_count, is_vegetarian)` -- creates and returns a single recipe
   - `search_recipes(session, cuisine=None, max_prep_time=None, vegetarian_only=False)` -- returns filtered results based on optional parameters
   - `import_from_csv(session, csv_path)` -- bulk loads all recipes from the CSV file
   - `get_recipe_stats(session)` -- returns a dictionary of recipe counts grouped by cuisine
4. Write a test block at the bottom that: creates an in-memory database, imports the CSV, searches for Italian recipes under 30 minutes, and prints cuisine statistics.
5. Run the file and verify all operations produce correct results.

**What You'll Learn:**
- How to structure CRUD functions with explicit session parameters (not global state)
- The difference between building a query incrementally (adding filters) versus writing one monolithic query
- Why bulk imports need different session handling than single-record operations

**Starter Prompt:**
> Read models.py and recipes.csv, then build CRUD operations for the recipe database.

**Better Prompt:**
> Read models.py to understand the Recipe model, then read the first 5 rows of recipes.csv to see the data format. Create crud.py with four functions: create_recipe (single insert), search_recipes (accepts optional filters for cuisine, max_prep_time, vegetarian_only and builds the query dynamically), import_from_csv (bulk loads from CSV with session.add_all and one commit), and get_recipe_stats (uses group_by to count recipes per cuisine). Include a test block at the bottom that imports all recipes, runs a filtered search, and prints statistics. Show me the output.

**Reflection Questions:**
1. Why is it better to pass `session` as a parameter to each function rather than creating a session inside each function?
2. What happens if `import_from_csv` fails halfway through -- do the already-added recipes persist? How would you make it all-or-nothing?
3. How would you modify `search_recipes` to support pagination (skip first N, return at most M)?

---

### Exercise 2.2 -- Broken Task Manager

**Debug**: CRUD Operations -- Find and fix 5 bugs in task management CRUD functions

**The Problem:** A task management application has CRUD functions that look reasonable at first glance, but each one has a subtle bug that causes incorrect behavior or crashes. The models are correct -- the bugs are all in the CRUD layer. The test suite validates each operation, and currently some tests fail.

**Your Task:**

1. Read `models.py` to understand the Task model (it is correct).
2. Run `python test_crud.py` and observe which tests fail and what errors they produce.
3. Open `broken_crud.py` and trace each failing test to the specific bug in the CRUD function.
4. Fix each bug. The bugs span five different categories: data persistence, query syntax, session lifecycle, error handling, and query execution.
5. Re-run tests after each fix until all pass.

**What You'll Learn:**
- The five most common CRUD implementation bugs in SQLAlchemy
- How session lifecycle (open, commit, close) affects data visibility
- The critical difference between a Query object and its results (calling `.all()`, `.first()`, etc.)

**Starter Prompt:**
> Run the tests and fix the bugs in broken_crud.py.

**Better Prompt:**
> First read models.py to understand the Task model. Then run `python test_crud.py` and show me all failures. Open broken_crud.py and for each failing test: (1) identify which CRUD function is buggy, (2) explain what the bug is, (3) fix it, and (4) re-run tests to confirm. Fix bugs one at a time in order of the test failures.

**Reflection Questions:**
1. Bug #1 (missing commit) is extremely common in real applications. What strategy would you use to make sure you never forget a commit?
2. Bug #3 (modifying after session closes) reveals a key concept about SQLAlchemy sessions. In your own words, what does "detached instance" mean?
3. If you were adding a new CRUD function to this codebase, what 3 things would you verify before considering it "done"?

---

## Module 3: Relationships

> **Real data does not exist in isolation. Artists have albums. Albums have tracks. The power of a relational database is in the "relational" part.**

In this module, you will add relationships to existing models and debug misconfigured ones. You will learn bidirectional navigation, cascade behavior, and the `back_populates` contract.

---

### Exercise 3.1 -- Music Library

**Build**: Relationships -- Add bidirectional relationships and cascade behavior to a music database

**The Problem:** A music streaming service has models for Artist, Album, and Track. The foreign keys are in place, but there are no `relationship()` definitions -- meaning you cannot navigate from an artist to their albums or from an album to its tracks using Python attributes. You need to add relationships, configure cascades, load sample data, and write queries that take advantage of the new navigation paths.

**Your Task:**

1. Read `models_no_relationships.py` to understand the current model structure. Note the foreign keys already in place.
2. Add `relationship()` with `back_populates` to all three models:
   - Artist should have an `albums` relationship (one-to-many)
   - Album should have an `artist` relationship (many-to-one) and a `tracks` relationship (one-to-many)
   - Track should have an `album` relationship (many-to-one)
3. Add `cascade="all, delete-orphan"` on the parent side of each relationship (Artist.albums, Album.tracks).
4. Load the sample data from `sample_data.csv` into the database.
5. Write and execute these queries:
   - Print all albums by a specific artist, accessed through `artist.albums`
   - Print all tracks on a specific album, accessed through `album.tracks`
   - Calculate the total track duration for each artist (sum of all track durations across all their albums)
6. Test cascade delete: delete an artist and verify their albums and tracks are also removed.

**What You'll Learn:**
- How `relationship()` and `back_populates` create bidirectional navigation between related models
- Why `cascade="all, delete-orphan"` is essential for parent-child relationships (and dangerous for peer relationships)
- The difference between navigating relationships in Python (artist.albums) versus writing manual JOIN queries

**Reflection Questions:**
1. What would happen if you set `cascade="all, delete-orphan"` on Track.album (the child side) instead of Album.tracks (the parent side)?
2. If an album could have multiple artists (a collaboration), how would you change the relationship model? What new table would you need?
3. Why does SQLAlchemy require `back_populates` on both sides? What happens if you only put it on one side?

---

### Exercise 3.2 -- Broken Blog

**Debug**: Relationships -- Find and fix 5 relationship configuration bugs in a blog system

**The Problem:** A blog platform has Author, Post, and Comment models with relationships that are incorrectly configured. The intent is clear: authors write posts, posts have comments. But the relationship definitions contain mismatches, wrong references, and missing configurations that cause crashes and data integrity issues.

**Your Task:**

1. Run `python test_relationships.py` and observe the errors. Each error points to a different relationship bug.
2. Open `broken_blog.py` and examine every `relationship()` call and every ForeignKey reference.
3. Fix all 5 bugs. Each bug is a different category of relationship misconfiguration.
4. Re-run the tests after each fix until all pass.
5. After all tests pass, verify cascade behavior: create an author with 2 posts (each with 3 comments), delete the author, and confirm everything is cleaned up.

**What You'll Learn:**
- The five most common relationship configuration mistakes in SQLAlchemy
- How `back_populates` forms a contract between two models that must match exactly
- Why `__tablename__` matters for ForeignKey references (it references the table, not the class)

**Reflection Questions:**
1. Bug #1 (back_populates mismatch) is the most common relationship error. What naming convention would prevent it?
2. Why does SQLAlchemy reference table names (lowercase, plural) in ForeignKey but class names (capitalized, singular) in relationship()?
3. What is the difference between `cascade="all"` and `cascade="all, delete-orphan"`? When would you want one but not the other?

---

## Module 4: Transactions

> **Without transactions, your database is a house of cards. One failed operation, and your data is in an inconsistent state that no amount of debugging can untangle.**

In this module, you will implement atomic operations that either succeed completely or fail cleanly. You will also debug transaction safety holes that could corrupt production data.

---

### Exercise 4.1 -- Game Inventory Trading

**Build**: Transactions -- Implement atomic item trades between game players

**The Problem:** A multiplayer game needs a trading system. Players can trade items for gold -- but if the trade fails halfway (gold deducted but item not transferred), players will riot. Every trade must be atomic: either the entire trade completes, or nothing changes. You also need a shop system and a batch trading endpoint that can handle partial failures gracefully.

**Your Task:**

1. Read `models.py` to understand the Player and Item models.
2. Create a new file called `trading.py` with these functions:
   - `trade_items(session, seller_id, buyer_id, item_id, gold_amount)` -- atomically transfers an item from the seller to the buyer in exchange for gold. Validate: item belongs to seller, buyer has enough gold. If anything fails, roll back everything.
   - `buy_from_shop(session, player_id, item_name, price)` -- creates a new item and deducts gold from the player. Atomic: if gold deduction fails, no item is created.
   - `batch_trade(session, trades_list)` -- processes a list of trades, using savepoints so that individual failed trades do not abort the entire batch. Returns a report of which trades succeeded and which failed.
3. Write a test block that:
   - Sets up 3 players with different gold amounts and items
   - Executes a successful trade
   - Attempts a trade where the buyer does not have enough gold (should fail cleanly)
   - Runs a batch of 5 trades where 2 are designed to fail
4. Verify that after all operations, player balances and item ownership are exactly correct.

**What You'll Learn:**
- How to implement atomic operations using try/except/rollback in SQLAlchemy
- The difference between rolling back an entire transaction versus using savepoints for partial failure handling
- Why validation before transaction start is cheaper and safer than validation during the transaction

**Reflection Questions:**
1. Why is it important to validate (check gold balance, verify item ownership) BEFORE starting the transaction, rather than relying on database constraints to catch problems?
2. In the `batch_trade` function, what is a savepoint and how does it differ from a full transaction rollback?
3. If two players try to buy the same item simultaneously, what could go wrong? How would you prevent it?

**The Twist:** After your trading system works, try this: start a trade, and between the gold deduction and the item transfer, raise an exception intentionally. Verify that the gold is returned to the buyer. This is the entire point of transactions.

---

### Exercise 4.2 -- Broken Bank

**Debug**: Transactions -- Find and fix 5 transaction safety holes in banking operations

**The Problem:** A banking module handles transfers, withdrawals, deposits, account closures, and interest calculations. It "works" in the happy path -- but every function has a transaction safety hole that would corrupt data under failure conditions. Your job is to find and fix all 5 holes before this code handles real money.

**Your Task:**

1. Read `broken_bank.py` carefully. Each function has a specific transaction safety problem.
2. Run `python test_bank.py` to see which tests fail. The tests intentionally trigger failure conditions to expose the safety holes.
3. Fix each function to be transaction-safe. The categories are: partial commits, missing validation, missing rollback, missing cleanup, and missing transaction wrapping.
4. Re-run tests after each fix until all pass.
5. For each bug, write a one-sentence explanation of what could go wrong in production if this bug shipped.

**What You'll Learn:**
- The five categories of transaction safety holes (partial commit, no validation, no rollback, no cleanup, no wrapping)
- How to think adversarially about database code: "What if this line throws an exception?"
- Why "works in testing" is not the same as "safe in production"

**Reflection Questions:**
1. Bug #1 (partial commit) is the most dangerous. Why is committing after each step worse than committing once at the end?
2. For Bug #2 (no balance check), should you check in Python or use a database CHECK constraint? What are the tradeoffs?
3. If you could add ONE automated check to prevent all five bug categories, what would it be?

---

## Module 5: Cloud Deployment

> **A database on your laptop is a toy. A database in the cloud is infrastructure. The gap between them is configuration, security, and connection management.**

In this module, you will deploy a working application to Neon PostgreSQL and diagnose common connection failures. You will learn environment variable management, connection pooling, and the specific quirks of serverless PostgreSQL.

---

### Exercise 5.1 -- Contact Book Deploy

**Build**: Cloud Deployment -- Configure and deploy a contact book application to Neon PostgreSQL

**The Problem:** You have a fully working contact book application that runs perfectly on in-memory SQLite. Now it needs to run against a real cloud database. This means: environment variables instead of hardcoded connection strings, connection pooling for performance, health checks for reliability, and secure credential management. The application code works -- you are only changing the infrastructure layer.

**Your Task:**

1. Read `contact_book.py` to understand the existing application (it works on SQLite).
2. Read `deployment_checklist.md` for the step-by-step deployment process.
3. Create a Neon PostgreSQL account at https://neon.tech (free tier).
4. Create a `.env` file with your `DATABASE_URL` (connection string from Neon dashboard). Add `.env` to a `.gitignore` file.
5. Modify `contact_book.py`:
   - Load `DATABASE_URL` from environment variables using `python-dotenv`
   - Replace the SQLite engine with a PostgreSQL engine using the URL
   - Add connection pooling: `pool_size=5`, `max_overflow=10`, `pool_pre_ping=True`, `pool_recycle=3600`
   - Add a `test_connection()` function that runs `SELECT 1` and prints success/failure
6. Run `test_connection()` to verify the Neon connection works.
7. Create the tables in Neon and insert 3 sample contacts.
8. Verify the data appears in the Neon SQL Editor in your browser.

**What You'll Learn:**
- How to configure SQLAlchemy for cloud PostgreSQL (connection pooling, health checks, connection recycling)
- Why environment variables are non-negotiable for database credentials (and how `.env` + `.gitignore` work together)
- The specific configuration Neon PostgreSQL needs (pool_pre_ping for auto-pause, pool_recycle for connection limits)

**Reflection Questions:**
1. What does `pool_pre_ping=True` do, and why is it specifically important for Neon (which auto-pauses after inactivity)?
2. What would happen if you committed your `.env` file to a public GitHub repository?
3. Why is `pool_recycle=3600` important for long-running applications? What happens to connections that are older than this limit?

---

### Exercise 5.2 -- Connection Doctor

**Debug**: Cloud Deployment -- Diagnose 5 different Neon connection failure scenarios

**The Problem:** Five different developers have each encountered a different connection error when deploying to Neon PostgreSQL. Each error has a specific root cause, a specific fix, and a prevention strategy. Your job is to diagnose each scenario like a database doctor: read the symptoms, identify the disease, prescribe the cure.

**Your Task:**

1. Read `error_scenarios.md` which contains 5 scenarios, each with:
   - The exact error message
   - The code that produced it
   - What the developer was doing
2. For each scenario, write:
   - **Root Cause**: One sentence explaining exactly why this error occurred
   - **Fix**: The specific code or configuration change that resolves it
   - **Prevention**: How to ensure this never happens again (configuration, testing, or process change)
3. Create a file called `diagnosis.md` with your findings for all 5 scenarios.

**What You'll Learn:**
- How to read database connection errors and map them to specific configuration problems
- The five most common Neon PostgreSQL deployment failures and their fixes
- Why connection testing should be part of every deployment checklist

**Reflection Questions:**
1. Which error message was most misleading (the message did not clearly point to the actual cause)?
2. If you were building a deployment health check script, which of these 5 scenarios could it automatically detect?
3. What is the difference between a connection error at startup versus a connection error during operation? Which is easier to debug?

---

## Module 6: Hybrid Verification

> **SQL is powerful. Bash is powerful. Together, they are a verification system that catches bugs neither tool would find alone.**

In this module, you will build a hybrid verification pipeline that cross-checks database query results against bash-computed totals. You will also analyze scenarios where developers chose the wrong tool for the job.

---

### Exercise 6.1 -- Expense Audit

**Build**: Hybrid Verification -- Build a SQL+bash pipeline that cross-checks expense report totals

**The Problem:** An expense tracking system has hundreds of records across multiple users, categories, and months. Management wants an audit report that proves the totals are correct. Your approach: compute each total two different ways (once with SQL, once with bash+awk on an exported CSV) and verify they match. If they match, the numbers are trustworthy. If they do not, something is wrong.

**Your Task:**

1. Read `models.py` to understand the User, Category, and Expense models.
2. Run `python seed_data.py` to populate the database with 200+ expense records.
3. Create a new file called `audit.py` with these functions:
   - `get_monthly_total(session, user_id, year, month)` -- uses SQLAlchemy to compute the sum of expenses for a specific user/month
   - `export_to_csv(session, user_id, year, month, output_path)` -- exports matching expenses to a CSV file
   - `verify_with_bash(csv_path)` -- uses `subprocess.run` to execute an awk command that sums the amount column of the CSV
   - `hybrid_audit(session, user_id, year, month)` -- runs both methods and compares results, printing PASS or FAIL with both values
4. Run the hybrid audit for 3 different user/month combinations and verify all match.
5. Print a summary table showing all audited periods and their results.

**What You'll Learn:**
- How to build cross-verification pipelines that catch bugs in either the SQL or the export logic
- When to use SQL (aggregation, filtering) versus bash (text processing, quick checks) versus Python (orchestration, comparison)
- Why hybrid verification is standard practice in financial systems and data pipelines

**Reflection Questions:**
1. If the SQL total and bash total disagree, how would you determine which one is wrong?
2. What floating-point issues might cause the totals to differ slightly even when both are correct? How would you handle that?
3. In what situation would hybrid verification be overkill? When is a single-tool check sufficient?

**The Extension:** Add a `full_audit(session)` function that audits every user/month combination in the database and outputs a complete audit report as a formatted table.

---

### Exercise 6.2 -- Wrong Tool

**Debug/Analysis**: Hybrid Verification -- Analyze 5 scenarios where the wrong tool was chosen

**The Problem:** Choosing the right tool -- bash, Python, SQL, or a hybrid approach -- is a skill that comes from experience. Here are 5 scenarios where a developer chose the wrong tool, leading to incorrect results, poor performance, or wasted effort. Your job is to analyze each scenario and recommend the correct approach.

**Your Task:**

1. Read `scenarios.md` which contains 5 real-world data scenarios.
2. For each scenario, write:
   - **Why it failed**: What specific limitation of the chosen tool caused the problem?
   - **Correct tool**: Which tool should have been used, and why?
   - **Consequence**: What was the real cost of the wrong choice (incorrect data, wasted time, missed bugs)?
3. Create a file called `analysis.md` with your findings.
4. At the end of your analysis, write a "Tool Selection Decision Tree" -- a set of rules that helps choose the right tool for a given task.

**What You'll Learn:**
- The strengths and limitations of bash, Python, SQL, and hybrid approaches for data tasks
- How to match a task's characteristics (data size, complexity, accuracy requirements) to the right tool
- Why "it works" is not enough -- the wrong tool can produce wrong results that look right

**Reflection Questions:**
1. Which scenario was most surprising -- where the "obvious" tool choice was actually the worst choice?
2. Is there a task where ALL four approaches (bash, Python, SQL, hybrid) would work equally well? What would make you prefer one over the others?
3. In your own work, how would you decide when to switch from a single tool to a hybrid approach?

---

## Module 7: Capstone Projects

> **Choose one (or more). This is where everything comes together.**

The capstones integrate skills from all six modules. There are no starter prompts -- you decide how to approach each one. Each capstone is designed to take 2-4 hours and produce a complete, working application.

---

### Capstone A -- Student Grade Portal

**Integration**: Full-stack database application -- modeling, CRUD, relationships, transactions, deployment

**The Problem:** A university department needs a student grade tracking system. Students enroll in courses, receive grades, and can request transcripts showing all their completed courses with a calculated GPA. The system needs to be deployed to a cloud database so department staff can access it from any computer. Grade submissions must be atomic -- a grade is either fully recorded or not at all.

Read `requirements.md` for the complete specification, including 20+ sample students and 10+ courses.

**Your Task:**

1. Design the data models: Student, Course, and Enrollment (the join table with a grade column).
2. Implement CRUD operations for students, courses, and enrollments.
3. Configure bidirectional relationships with appropriate cascade behavior.
4. Implement atomic grade submission (a transaction that creates the enrollment and records the grade).
5. Write a `generate_transcript(student_id)` function that returns all courses, grades, and calculated GPA.
6. Implement GPA calculation: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0, weighted by course credits.
7. Deploy to Neon PostgreSQL and verify the transcript function works against the cloud database.

**What You'll Learn:**
- How to design a many-to-many relationship with additional attributes (grade on the join table)
- How atomic transactions protect data integrity in grade recording
- The full deployment workflow from local SQLite to cloud PostgreSQL

---

### Capstone B -- CSV Migration

**Real-world**: Database normalization -- transform flat CSV data into a properly structured relational database

**The Problem:** A sales team has been tracking everything in a single CSV file. It has 500 rows of sales data with customer info, product info, sales rep info, and transaction details all mashed into one flat table. Duplicated customer names, inconsistent product categories, no way to query efficiently. Your job: design a normalized database, migrate all 500 rows, and prove that the new database can answer questions the CSV never could.

Read `sales_data.csv` to understand the source data.

**Your Task:**

1. Analyze the CSV: identify all entities (Customer, Product, SalesRep, Sale) and their attributes.
2. Design a normalized database schema with proper relationships between entities.
3. Write a migration script that reads the CSV and populates all tables, handling deduplication (same customer appearing in multiple rows should create one Customer record).
4. Migrate all 500 rows and verify record counts match expectations.
5. Write 5 queries that the CSV could not answer efficiently:
   - Top 5 customers by total revenue
   - Monthly sales trends by region
   - Product category revenue breakdown
   - Sales rep performance ranking
   - Customers who purchased from multiple categories

**What You'll Learn:**
- How to analyze denormalized data and identify the correct normalized structure
- The practical challenges of data migration: deduplication, foreign key resolution, data cleaning
- Why normalized databases enable queries that flat files cannot support efficiently

---

### Capstone C -- Disaster Recovery

**Forensics**: Full-system debugging -- find and fix 8+ bugs spanning models, CRUD, transactions, and deployment

**The Problem:** A "production" budget tracker has been handed to you for emergency repair. It has bugs in every layer: model definitions, CRUD operations, transaction safety, connection configuration, and query logic. The test suite exercises all functions and exposes the bugs. Your job: triage, diagnose, and fix them all, then explain what went wrong and how to prevent each category of bug.

**Your Task:**

1. Run `python test_budget_tracker.py` and observe the cascade of failures.
2. Open `broken_budget_tracker.py` and inventory all the bugs you can find.
3. Triage: which bugs block other fixes? Fix blocking bugs first.
4. Fix all 8+ bugs across all layers.
5. Re-run the test suite until all tests pass.
6. Write a `postmortem.md` file documenting: each bug found, its category (model/CRUD/transaction/deployment/query), root cause, fix applied, and prevention strategy.

**What You'll Learn:**
- How to triage a codebase with bugs at multiple layers (fix the foundation before fixing the roof)
- The discipline of systematic debugging: inventory first, prioritize second, fix third
- How to write a postmortem that prevents the same categories of bugs from recurring

---

## Progression Summary

| Module | Skill Layer | Build Exercise | Debug Exercise |
|--------|-------------|---------------|----------------|
| 1 | Data Modeling | Library Catalog | Broken Pet Store |
| 2 | CRUD Operations | Recipe Book | Broken Task Manager |
| 3 | Relationships | Music Library | Broken Blog |
| 4 | Transactions | Game Inventory | Broken Bank |
| 5 | Cloud Deployment | Contact Book Deploy | Connection Doctor |
| 6 | Hybrid Verification | Expense Audit | Wrong Tool |
| 7 | Capstone | Student Portal / CSV Migration / Disaster Recovery | |

Each module assumes you have completed the previous modules. Module 3 assumes you can write models (Module 1) and CRUD (Module 2). Module 4 assumes you understand relationships (Module 3). Module 5 requires everything from 1-4 to be working locally before deploying. Module 6 ties it all together.

The capstones are intentionally broad. There is no single "correct" solution. The rubric measures whether your implementation works, whether your code is well-structured, and whether you can explain your decisions.

---

_Built for Muhammad Usman Akbar's AI-Native Development Curriculum._

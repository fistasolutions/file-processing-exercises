# Structured Data & Persistent Storage -- Practice Exercises

**From CSV chaos to production databases: build, debug, and deploy real data applications with SQLAlchemy and Neon PostgreSQL.**

These exercises accompany Chapter 9 of the Muhammad Usman Akbar AI-Native Development Curriculum. You will design data models, implement CRUD operations, configure relationships, manage transactions, deploy to cloud databases, and verify results using hybrid SQL+bash pipelines.

---

## Package Structure

```
claude-code-structured-data-exercises/
├── .github/workflows/release.yml
├── EXERCISE-GUIDE.md
├── README.md
├── module-1-data-modeling/
│   ├── exercise-1.1-library-catalog/
│   │   ├── INSTRUCTIONS.md
│   │   └── requirements.md
│   └── exercise-1.2-broken-pet-store/
│       ├── INSTRUCTIONS.md
│       ├── broken_models.py
│       └── test_models.py
├── module-2-crud-operations/
│   ├── exercise-2.1-recipe-book/
│   │   ├── INSTRUCTIONS.md
│   │   ├── models.py
│   │   └── recipes.csv
│   └── exercise-2.2-broken-task-manager/
│       ├── INSTRUCTIONS.md
│       ├── broken_crud.py
│       ├── models.py
│       └── test_crud.py
├── module-3-relationships/
│   ├── exercise-3.1-music-library/
│   │   ├── INSTRUCTIONS.md
│   │   ├── models_no_relationships.py
│   │   └── sample_data.csv
│   └── exercise-3.2-broken-blog/
│       ├── INSTRUCTIONS.md
│       ├── broken_blog.py
│       └── test_relationships.py
├── module-4-transactions/
│   ├── exercise-4.1-game-inventory/
│   │   ├── INSTRUCTIONS.md
│   │   └── models.py
│   └── exercise-4.2-broken-bank/
│       ├── INSTRUCTIONS.md
│       ├── broken_bank.py
│       └── test_bank.py
├── module-5-cloud-deployment/
│   ├── exercise-5.1-contact-book-deploy/
│   │   ├── INSTRUCTIONS.md
│   │   ├── contact_book.py
│   │   └── deployment_checklist.md
│   └── exercise-5.2-connection-doctor/
│       ├── INSTRUCTIONS.md
│       └── error_scenarios.md
├── module-6-hybrid-verification/
│   ├── exercise-6.1-expense-audit/
│   │   ├── INSTRUCTIONS.md
│   │   ├── models.py
│   │   └── seed_data.py
│   └── exercise-6.2-wrong-tool/
│       ├── INSTRUCTIONS.md
│       └── scenarios.md
└── module-7-capstone/
    ├── capstone-A-student-portal/
    │   ├── INSTRUCTIONS.md
    │   └── requirements.md
    ├── capstone-B-csv-migration/
    │   ├── INSTRUCTIONS.md
    │   └── sales_data.csv
    └── capstone-C-disaster-recovery/
        ├── INSTRUCTIONS.md
        ├── broken_budget_tracker.py
        └── test_budget_tracker.py
```

---

## How to Get Started

1. Open Claude Code in your terminal.
2. Navigate to the exercise folder you want to work on:
   ```
   cd module-1-data-modeling/exercise-1.1-library-catalog
   ```
3. Read `INSTRUCTIONS.md` for that exercise -- it tells you exactly what to do.
4. Work through the steps using Claude Code as your development environment.
5. After completing an exercise, reflect on the questions at the bottom of the instructions before moving on.

---

## Recommended Order

Work through the modules sequentially. Each module builds on skills from the previous one.

| Module | Topic | Exercises | Time |
|--------|-------|-----------|------|
| 1 | Data Modeling | 1.1 Build, 1.2 Debug | 30-60 min |
| 2 | CRUD Operations | 2.1 Build, 2.2 Debug | 30-60 min |
| 3 | Relationships | 3.1 Build, 3.2 Debug | 30-60 min |
| 4 | Transactions | 4.1 Build, 4.2 Debug | 30-60 min |
| 5 | Cloud Deployment | 5.1 Build, 5.2 Debug | 45-90 min |
| 6 | Hybrid Verification | 6.1 Build, 6.2 Debug | 30-60 min |
| 7 | Capstone | Choose A, B, or C | 2-4 hours |

---

## The Database Development Framework

Use this six-step framework for every exercise:

1. **Model** -- Define the data structure: what entities exist? What are their attributes and relationships?
2. **Connect** -- Establish the database connection: engine, session, connection pooling.
3. **Operate** -- Implement CRUD operations with proper session management.
4. **Protect** -- Add transaction safety: try/except, commit/rollback, validation.
5. **Verify** -- Test the implementation: run queries, check results, verify edge cases.
6. **Deploy** -- Move to production: environment variables, connection pooling, cloud database.

---

## Assessment Rubric

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Data Modeling** | Wrong types or missing constraints | Works but misses edge cases | Correct types and constraints | Includes indexes, defaults, edge cases |
| **Session Management** | Sessions left open | Committed but no error handling | Context managers with try/except | Optimized with flush and bulk ops |
| **Relationships** | No relationships defined | Defined but not bidirectional | Full bidirectional with cascade | Lazy loading strategy optimized |
| **Transaction Safety** | No error handling | Try/except but no rollback | Atomic transactions with rollback | Savepoints for batch operations |
| **Debugging** | Cannot identify bugs | Finds some, misses root causes | Finds all, applies correct fixes | Finds all, explains prevention |

---

_Built for Muhammad Usman Akbar's AI-Native Development Curriculum._

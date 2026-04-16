# Exercise 1.1 -- Library Catalog

**Build**: Data Modeling -- Design SQLAlchemy models from a business requirements document

## Goal

Design and implement SQLAlchemy ORM models for a library catalog system based on a business requirements document. You will choose appropriate column types, add constraints that enforce data integrity, and connect tables using foreign keys. By the end, you will have a working schema that can store books, authors, and genres in a relational database.

## What You Have

- `requirements.md` -- A business requirements document from the library describing what data they need to track. It includes entity descriptions, attribute specifications, relationship rules, and 10+ sample data records.

## Your Tasks

### Step 1: Read and Analyze Requirements

Read `requirements.md` carefully. For each entity (Book, Author, Genre), list every attribute mentioned and its implied data type. Pay attention to constraints: which fields must be unique? Which cannot be empty? What are reasonable maximum lengths?

### Step 2: Create the Models

Create a new file called `models.py`. Define a SQLAlchemy `Base` using `declarative_base()`. Then define three model classes: `Book`, `Author`, and `Genre`. For each attribute in the requirements, choose the most appropriate SQLAlchemy column type (`String`, `Integer`, `Text`, etc.) and add constraints (`nullable=False`, `unique=True`, max length).

### Step 3: Add Foreign Keys

Add `ForeignKey` columns to the `Book` model to connect each book to its author and genre. The requirements specify that each book has exactly one author and exactly one genre.

### Step 4: Create Tables and Test

At the bottom of `models.py`, add a test block that:
1. Creates an in-memory SQLite engine (`sqlite:///:memory:`)
2. Calls `Base.metadata.create_all(engine)` to create the tables
3. Creates a `Session` and inserts at least 3 books with their authors and genres
4. Queries and prints the inserted data to verify everything works

### Step 5: Verify Edge Cases

Try inserting a book with a duplicate ISBN (should fail if you added the unique constraint). Try inserting a book without a title (should fail if you added nullable=False). These failures confirm your constraints are working.

## Expected Results

- A `models.py` file with `Book`, `Author`, and `Genre` model classes
- Each class has a `__tablename__`, a primary key `id`, and all attributes from the requirements with correct types and constraints
- `Book` has `author_id` and `genre_id` foreign key columns
- Running `python models.py` creates tables, inserts sample data, and prints it without errors
- Constraint violations produce clear error messages (not silent data corruption)

## Reflection

1. Which column type decisions required judgment (not just "obviously String or Integer")? What made those decisions harder?
2. If the library later wants to allow books with multiple authors, which part of your schema would need to change?
3. What would happen if you forgot to add `nullable=False` to `Book.title`? How would that manifest as a real-world data problem?

# Exercise 2.1 -- Recipe Book

**Build**: CRUD Operations -- Implement create, search, import, and aggregate functions for a recipe database

## Goal

Write four CRUD functions for a recipe database: creating individual recipes, searching with multiple optional filters, bulk importing from CSV, and generating statistics by cuisine. The models are already built -- you are implementing the operations layer with proper session management.

## What You Have

- `models.py` -- Working Recipe and Tag models. These are already correct -- do not modify them.
- `recipes.csv` -- 55 recipes with columns: title, cuisine, prep_time_minutes, difficulty, ingredients_count, is_vegetarian. Diverse cuisines (Italian, Mexican, Japanese, Indian, American, Thai, French, Ethiopian, Korean, Greek), varying difficulties (easy/medium/hard), mix of vegetarian and non-vegetarian.

## Your Tasks

### Step 1: Read the Models

Read `models.py` to understand the Recipe model's columns and types. Note which fields are required and which are optional.

### Step 2: Read the CSV

Read the first few rows of `recipes.csv` to understand the data format and how CSV columns map to model attributes. Pay attention to the `is_vegetarian` column format (true/false as strings).

### Step 3: Implement CRUD Functions

Create a new file called `crud.py` with these four functions:

1. **`create_recipe(session, title, cuisine, prep_time_minutes, difficulty, ingredients_count, is_vegetarian)`** -- Creates a single Recipe, adds it to the session, commits, and returns the created recipe object.

2. **`search_recipes(session, cuisine=None, max_prep_time=None, vegetarian_only=False)`** -- Builds a query dynamically based on which parameters are provided. If `cuisine` is given, filter by cuisine. If `max_prep_time` is given, filter for recipes with prep time at or below that value. If `vegetarian_only` is True, filter for vegetarian recipes only. Return all matching recipes.

3. **`import_from_csv(session, csv_path)`** -- Reads the CSV file, creates a Recipe object for each row, adds them all to the session, and commits once. Returns the count of imported recipes.

4. **`get_recipe_stats(session)`** -- Returns a dictionary where keys are cuisine names and values are the count of recipes in that cuisine. Use SQLAlchemy's `group_by` and `func.count`.

### Step 4: Write a Test Block

At the bottom of `crud.py`, add a test block that:
1. Creates an in-memory SQLite database and tables
2. Imports all recipes from `recipes.csv`
3. Prints the total number of imported recipes
4. Searches for Italian recipes under 30 minutes and prints results
5. Searches for vegetarian recipes and prints the count
6. Prints cuisine statistics (count per cuisine)

### Step 5: Run and Verify

Run `python crud.py` and verify that all operations produce correct results. Check that the recipe count matches the CSV row count.

## Expected Results

- A `crud.py` file with 4 working functions
- All 55 recipes imported from CSV
- Search queries return correctly filtered results
- Statistics show accurate counts per cuisine
- No open sessions or uncommitted transactions when the script finishes

## Reflection

1. Why is it better to pass `session` as a parameter to each function rather than creating a session inside each function?
2. What happens if `import_from_csv` fails halfway through -- do the already-added recipes persist? How would you make it all-or-nothing?
3. How would you modify `search_recipes` to support pagination (skip first N, return at most M)?

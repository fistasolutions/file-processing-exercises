# Capstone B -- CSV Migration

**Real-world**: Database normalization -- transform flat CSV data into a properly structured relational database

## Goal

Take a flat, denormalized CSV file with 500 rows of sales data and migrate it into a properly normalized relational database. The CSV has customer info, product info, sales rep info, and transaction details all mashed into one table. You will design the normalized schema, write the migration script, and prove that the database can answer questions the CSV never could.

## What You Have

- `sales_data.csv` -- 500 rows of sales data with columns: date, customer_name, customer_email, product_name, product_category, quantity, unit_price, total, sales_rep_name, region. This is a FLAT denormalized file -- the same customer name and email appear in many rows, the same product appears many times, and the same sales rep name is repeated throughout.

## Your Tasks

### Step 1: Analyze the CSV

Read the CSV and identify:
- How many unique customers are there?
- How many unique products?
- How many unique sales reps?
- What are the product categories?
- What is the date range?
- Are there any data quality issues (missing values, inconsistencies)?

### Step 2: Design the Normalized Schema

Design at least 4 SQLAlchemy models:
- **Customer** -- id, name, email (unique)
- **Product** -- id, name, category, unit_price
- **SalesRep** -- id, name, region
- **Sale** -- id, customer_id (FK), product_id (FK), sales_rep_id (FK), quantity, total, sale_date

Think about: Which fields should be unique? Which are required? What relationships exist?

### Step 3: Write the Migration Script

Create a `migrate.py` script that:
1. Reads the CSV file
2. Extracts unique customers, products, and sales reps (deduplication)
3. Creates all entity records first (customers, products, sales reps)
4. Creates sale records linking to the correct entities via foreign keys
5. Handles edge cases (same customer with slightly different names, etc.)
6. Reports migration statistics: rows read, entities created, sales imported

### Step 4: Verify the Migration

After migration, verify:
- Total number of sales matches CSV row count
- Sum of all sale totals matches the CSV sum
- Every sale links to a valid customer, product, and sales rep
- No orphaned or duplicate records

### Step 5: Write Analytical Queries

Write 5 queries that the CSV could not answer efficiently:
1. **Top 5 customers by total revenue** -- aggregate across all purchases
2. **Monthly sales trends by region** -- GROUP BY month and region
3. **Product category revenue breakdown** -- total revenue per category
4. **Sales rep performance ranking** -- total revenue per rep, sorted
5. **Cross-category customers** -- customers who purchased from 2+ categories

## Expected Results

- Normalized database with 4+ tables and proper relationships
- All 500 rows migrated with correct foreign key references
- Deduplication: fewer customers/products/reps than CSV rows
- 5 analytical queries producing correct results
- Migration script is idempotent (can run again without duplicating data)

## Reflection

1. What is the biggest advantage of the normalized database over the flat CSV? What is the biggest disadvantage?
2. During migration, how did you handle deduplication? What would you do if two rows had the same customer name but different emails?
3. Which of the 5 analytical queries would be most difficult (or impossible) to answer using only bash tools on the original CSV?

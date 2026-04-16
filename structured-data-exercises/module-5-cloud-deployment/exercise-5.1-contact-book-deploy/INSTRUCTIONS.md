# Exercise 5.1 -- Contact Book Deploy

**Build**: Cloud Deployment -- Configure and deploy a contact book application to Neon PostgreSQL

## Goal

Take a working contact book application (currently using in-memory SQLite) and configure it for production deployment on Neon PostgreSQL. You will add environment variable management, connection pooling, health checks, and secure credential handling. The application logic stays the same -- you are only changing the infrastructure layer.

## What You Have

- `contact_book.py` -- A complete, working contact book application with a Contact model (name, email, phone, notes) and CRUD functions. Currently uses `sqlite:///:memory:` as its database. All functions work correctly on SQLite.
- `deployment_checklist.md` -- A step-by-step checklist for deploying to Neon PostgreSQL, from account creation through final verification.

## Your Tasks

### Step 1: Read the Application

Read `contact_book.py` to understand the existing application. It works perfectly on SQLite -- your job is not to change what it does, but to change how it connects.

### Step 2: Follow the Deployment Checklist

Read `deployment_checklist.md` and follow it step by step:

1. Create a Neon PostgreSQL account (https://neon.tech, free tier)
2. Create a new project and database
3. Copy the connection string from the Neon dashboard

### Step 3: Add Environment Variable Management

1. Install `python-dotenv`: `pip install python-dotenv`
2. Create a `.env` file with your `DATABASE_URL`:
   ```
   DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
   ```
3. Create a `.gitignore` file with `.env` in it
4. Modify `contact_book.py` to load `DATABASE_URL` from the environment

### Step 4: Configure Connection Pooling

Replace the SQLite engine with a PostgreSQL engine configured for production:
- `pool_size=5` -- maintain 5 persistent connections
- `max_overflow=10` -- allow up to 10 additional connections under load
- `pool_pre_ping=True` -- verify connections are alive before using them (critical for Neon's auto-pause)
- `pool_recycle=3600` -- replace connections older than 1 hour

### Step 5: Add a Health Check

Add a `test_connection()` function that:
1. Creates an engine and connects
2. Executes `SELECT 1`
3. Prints "Connection successful" or "Connection failed: {error}"

### Step 6: Deploy and Verify

1. Run `test_connection()` to verify the Neon connection works
2. Create the tables in Neon (`Base.metadata.create_all(engine)`)
3. Insert 3 sample contacts
4. Verify the data appears in the Neon SQL Editor (in your browser)

## Expected Results

- `contact_book.py` connects to Neon PostgreSQL via `DATABASE_URL` environment variable
- `.env` file exists with connection string, `.gitignore` includes `.env`
- Connection pooling configured with pool_size=5, max_overflow=10, pool_pre_ping=True, pool_recycle=3600
- `test_connection()` function prints success
- Tables created in Neon with sample data visible in the SQL Editor
- Application CRUD functions work against the cloud database

## Reflection

1. What does `pool_pre_ping=True` do, and why is it specifically important for Neon (which auto-pauses after inactivity)?
2. What would happen if you committed your `.env` file to a public GitHub repository?
3. Why is `pool_recycle=3600` important for long-running applications? What happens to connections that are older than this limit?

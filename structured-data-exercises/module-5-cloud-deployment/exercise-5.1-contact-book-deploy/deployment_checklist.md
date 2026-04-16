# Neon PostgreSQL Deployment Checklist

Follow these steps in order. Check each box as you complete it.

---

## Phase 1: Create Neon Account and Database

- [ ] Go to https://neon.tech and sign up for a free account
- [ ] Create a new project (name it "contact-book" or similar)
- [ ] Note the connection details from the dashboard:
  - Host (e.g., `ep-cool-name-123456.us-east-2.aws.neon.tech`)
  - Database name (default: `neondb`)
  - Username (default: your email prefix)
  - Password (shown once at project creation -- save it securely)
- [ ] Copy the full connection string. It looks like:
  ```
  postgresql://username:password@ep-cool-name-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
  ```

## Phase 2: Configure Local Environment

- [ ] Install required packages:
  ```bash
  pip install python-dotenv psycopg2-binary
  ```
  (Use `psycopg2-binary` for development. For production, use `psycopg2`.)

- [ ] Create a `.env` file in this exercise directory:
  ```
  DATABASE_URL=postgresql://username:password@host/dbname?sslmode=require
  ```
  Replace with your actual Neon connection string.

- [ ] Create a `.gitignore` file:
  ```
  .env
  __pycache__/
  *.pyc
  ```

- [ ] Verify `.env` is not tracked by git:
  ```bash
  git status
  ```
  The `.env` file should NOT appear in the staged/tracked files.

## Phase 3: Modify Application Code

- [ ] Add environment variable loading at the top of `contact_book.py`:
  ```python
  import os
  from dotenv import load_dotenv
  load_dotenv()
  ```

- [ ] Replace the SQLite engine with a PostgreSQL engine:
  ```python
  DATABASE_URL = os.getenv("DATABASE_URL")
  if not DATABASE_URL:
      raise ValueError("DATABASE_URL environment variable is not set")
  ```

- [ ] Add connection pooling configuration:
  ```python
  engine = create_engine(
      DATABASE_URL,
      pool_size=5,           # Maintain 5 persistent connections
      max_overflow=10,       # Allow up to 10 extra connections under load
      pool_pre_ping=True,    # Verify connection is alive before using
      pool_recycle=3600,     # Replace connections older than 1 hour
  )
  ```

- [ ] Add a `test_connection()` function:
  ```python
  def test_connection():
      try:
          with engine.connect() as conn:
              conn.execute(text("SELECT 1"))
          print("Connection successful!")
          return True
      except Exception as e:
          print(f"Connection failed: {e}")
          return False
  ```
  (Do not forget to import `text` from sqlalchemy.)

## Phase 4: Deploy and Verify

- [ ] Run the connection test:
  ```bash
  python -c "from contact_book import test_connection; test_connection()"
  ```
  You should see "Connection successful!"

- [ ] Create tables in Neon:
  ```bash
  python -c "from contact_book import engine, Base; Base.metadata.create_all(engine); print('Tables created')"
  ```

- [ ] Insert sample contacts by running:
  ```bash
  python contact_book.py
  ```

- [ ] Verify in Neon dashboard:
  1. Go to your Neon project in the browser
  2. Click "SQL Editor"
  3. Run: `SELECT * FROM contacts;`
  4. You should see your sample contacts

## Phase 5: Verify Production Readiness

- [ ] Connection pooling is configured (check engine parameters)
- [ ] `pool_pre_ping=True` is set (critical for Neon's auto-pause feature)
- [ ] `.env` is in `.gitignore` (credentials are never committed)
- [ ] `DATABASE_URL` is loaded from environment, not hardcoded
- [ ] All CRUD operations work against Neon (add, search, update, delete)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'psycopg2'` | Run `pip install psycopg2-binary` |
| `Connection timed out` | Check host in connection string; verify Neon project is active |
| `password authentication failed` | Verify password in `.env` matches Neon dashboard |
| `SSL connection is required` | Add `?sslmode=require` to connection string |
| `remaining connection slots are reserved` | Reduce `pool_size` (Neon free tier limits connections) |

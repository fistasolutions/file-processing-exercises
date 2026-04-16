# Connection Error Scenarios

Five developers each hit a different connection error deploying to Neon PostgreSQL. Diagnose each one.

---

## Scenario 1: Connection Timed Out

**Error Message:**
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection timed out
	Is the server running on host "ep-cool-breeze-12345.us-east-1.aws.neon.tech" and accepting
	TCP/IP connections on port 5432?
```

**The Code:**
```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Connected!")
```

**The .env File:**
```
DATABASE_URL=postgresql://alex:mypassword123@ep-cool-breeze-12345.us-east-1.aws.neon.tech/neondb?sslmode=require
```

**Context:** Alex created a Neon project and copied the connection string, but made a small typo. The actual Neon endpoint is `ep-cool-breeze-12345.us-east-2.aws.neon.tech` (us-east-**2**, not us-east-**1**). Alex did not double-check against the dashboard.

---

## Scenario 2: Password Authentication Failed

**Error Message:**
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  password authentication failed for user "priya_dev"
```

**The Code:**
```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    print("Connected!")
```

**The .env File:**
```
DATABASE_URL=postgresql://priya_dev:OldPassword456@ep-fancy-lake-78901.us-east-2.aws.neon.tech/neondb?sslmode=require
```

**Context:** Priya reset the database password in the Neon dashboard last week for security rotation, but forgot to update the `.env` file. The new password is `NewSecurePass789`, but the `.env` still has `OldPassword456`.

---

## Scenario 3: Missing psycopg2 Driver

**Error Message:**
```
ModuleNotFoundError: No module named 'psycopg2'
```

**The Code:**
```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:pass@host/db?sslmode=require"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("Connected!")
```

**Context:** Marcus set up a new virtual environment for his project. He installed SQLAlchemy with `pip install sqlalchemy` but forgot that SQLAlchemy needs a database-specific driver to connect to PostgreSQL. His code works fine when the engine uses `sqlite:///:memory:` because Python includes SQLite support by default, but PostgreSQL requires an additional package.

**The requirements.txt:**
```
sqlalchemy==2.0.25
python-dotenv==1.0.1
```

---

## Scenario 4: Server Closed Connection Unexpectedly

**Error Message:**
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) server closed the connection unexpectedly
	This probably means the server terminated abnormally
	before or while processing the request.
```

**The Code:**
```python
import os, time
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_size=5,
    max_overflow=10,
    # pool_pre_ping is NOT set (defaults to False)
)

Session = sessionmaker(bind=engine)

# Application starts, makes initial queries (works fine)
session = Session()
result = session.execute(text("SELECT 1"))
print("Initial connection works!")
session.close()

# ... several hours pass with no database activity ...
# Neon auto-pauses the compute endpoint after 5 minutes of inactivity

# Later, application tries to use the database again
session = Session()
result = session.execute(text("SELECT * FROM contacts"))  # CRASHES HERE
```

**Context:** Dana's application worked perfectly during development when she was making frequent queries. But in production, there are periods of low activity. Neon's free tier auto-pauses the compute endpoint after 5 minutes of inactivity. When the application tries to use a pooled connection that was opened before the pause, the connection is dead but the pool does not know it.

---

## Scenario 5: Connection Slots Exhausted

**Error Message:**
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  remaining connection slots are reserved for non-replication superuser connections
```

**The Code:**
```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = create_engine(
    os.getenv("DATABASE_URL"),
    pool_size=50,
    max_overflow=20,
)

Session = sessionmaker(bind=engine)

# Simulate multiple concurrent operations
sessions = []
for i in range(50):
    session = Session()
    session.execute(text("SELECT pg_sleep(1)"))
    sessions.append(session)
    print(f"Opened connection {i + 1}")
```

**Context:** Jordan's application handles many concurrent users. They set `pool_size=50` thinking more connections means better performance. But Neon's free tier only allows a handful of concurrent connections (typically 5-10 for the free tier). The connection pool tries to open far more connections than the database allows.

---

## Your Task

For each scenario, determine:
1. **Root Cause**: What exactly caused this error?
2. **Fix**: What specific change resolves it?
3. **Prevention**: How do you prevent this from happening again?

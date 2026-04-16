"""Database connection and query utilities."""

import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "tasks.db")

"""
Budget Tracker Application -- "Production" Version
WARNING: This file contains 8+ bugs spanning every layer. This is a disaster recovery exercise.
"""

import os
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text, create_engine, func, extract
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


# ── Models ───────────────────────────────────────────────────────────

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    monthly_budget = Column(Float, default=1000.0)

    # BUG #4: back_populates="owner" but Expense has back_populates="user"
    expenses = relationship("Expense", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User: {self.name}>"


class Category(Base):
    # BUG #2: missing __tablename__ -- will default to "category" not "categories"
    # This breaks ForeignKey references that expect "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))

    expenses = relationship("Expense", back_populates="category")

    def __repr__(self):
        return f"<Category: {self.name}>"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    # BUG #1: amount uses String instead of Float -- will cause math errors
    amount = Column(String(20), nullable=False)
    description = Column(Text)
    expense_date = Column(Date, nullable=False, default=date.today)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # BUG #4 (counterpart): back_populates="user" doesn't match User's back_populates="owner"
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"<Expense: ${self.amount} - {self.description}>"


# ── Database Connection ──────────────────────────────────────────────

# BUG #6: Hardcoded database credentials -- security violation
# Should load from environment variable
DATABASE_URL = "postgresql://admin:FAKE-password-for-exercise@localhost:5432/budgetdb"

# BUG #7: Missing pool_pre_ping=True -- connections will fail after Neon auto-pause
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    # pool_pre_ping=True is missing
)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


# ── CRUD Operations ──────────────────────────────────────────────────

def create_expense(session, user_id, category_id, amount, description, expense_date=None):
    """Create a new expense record."""
    expense = Expense(
        user_id=user_id,
        category_id=category_id,
        amount=amount,
        description=description,
        expense_date=expense_date or date.today(),
    )
    session.add(expense)
    # BUG #3: missing session.commit() -- data never persists
    return expense


def get_expenses_by_user(session, user_id):
    """Get all expenses for a user."""
    return session.query(Expense).filter(Expense.user_id == user_id).all()


def get_expenses_by_category(session, user_id, category_id):
    """Get expenses for a user in a specific category."""
    return session.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.category_id == category_id,
    ).all()


# ── Transaction Operations ───────────────────────────────────────────

def transfer_budget(session, from_user_id, to_user_id, amount):
    """Transfer budget allocation from one user to another.

    BUG #5: Commits debit before credit -- not atomic.
    If credit fails, money vanishes.
    """
    from_user = session.query(User).filter(User.id == from_user_id).first()
    to_user = session.query(User).filter(User.id == to_user_id).first()

    if not from_user or not to_user:
        return {"success": False, "message": "User not found"}

    if from_user.monthly_budget < amount:
        return {"success": False, "message": "Insufficient budget"}

    from_user.monthly_budget -= amount
    session.commit()  # BUG: partial commit

    to_user.monthly_budget += amount
    session.commit()

    return {"success": True, "message": f"Transferred ${amount:.2f}"}


# ── Query Operations ─────────────────────────────────────────────────

def get_monthly_summary(session, user_id, year, month):
    """Get expense summary for a specific month.

    BUG #8: Uses > instead of >= for month comparison, causing off-by-one.
    Expenses on the first day of the month are excluded.
    Also uses < instead of <= for the end, excluding the last day.
    """
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    expenses = session.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.expense_date > start_date,   # BUG: should be >=
        Expense.expense_date < end_date,      # BUG: should be <  (actually this is correct for exclusive upper bound, but combined with > instead of >= for lower bound, the first day is always missed)
    ).all()

    total = sum(float(e.amount) for e in expenses)
    return {
        "user_id": user_id,
        "year": year,
        "month": month,
        "total": total,
        "count": len(expenses),
        "expenses": expenses,
    }


def get_category_breakdown(session, user_id, year, month):
    """Get spending breakdown by category for a specific month."""
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    results = (
        session.query(
            Category.name,
            func.count(Expense.id).label("count"),
            func.sum(Expense.amount).label("total"),
        )
        .join(Expense)
        .filter(
            Expense.user_id == user_id,
            Expense.expense_date >= start_date,
            Expense.expense_date < end_date,
        )
        .group_by(Category.name)
        .all()
    )

    return [{"category": r[0], "count": r[1], "total": float(r[2] or 0)} for r in results]


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Budget Tracker -- Running diagnostics")
    print("=" * 50)
    print(f"Database URL: {DATABASE_URL}")
    print("WARNING: This application has known bugs.")
    print("Run test_budget_tracker.py to identify them.")

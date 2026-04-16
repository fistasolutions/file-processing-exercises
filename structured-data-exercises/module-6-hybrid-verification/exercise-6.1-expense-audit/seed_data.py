"""
Seed script for Expense Audit exercise.
Run: python seed_data.py
Creates expenses.db with 3 users, 5 categories, and 200+ expense records.
"""

import os
import random
from datetime import date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Expense

# Use a file-based SQLite database so both SQL and bash can access it
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"


def seed():
    # Remove existing database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # ── Users ────────────────────────────────────────────────────────
    users = [
        User(name="Elena Rodriguez", email="elena@example.com"),
        User(name="James Chen", email="james@example.com"),
        User(name="Fatima Al-Hassan", email="fatima@example.com"),
    ]
    session.add_all(users)
    session.commit()

    # ── Categories ───────────────────────────────────────────────────
    categories = [
        Category(name="Food & Dining", description="Restaurants, groceries, coffee shops"),
        Category(name="Transportation", description="Gas, public transit, ride shares, parking"),
        Category(name="Office Supplies", description="Pens, paper, software subscriptions"),
        Category(name="Travel", description="Hotels, flights, conference fees"),
        Category(name="Utilities", description="Internet, phone, electricity"),
    ]
    session.add_all(categories)
    session.commit()

    # ── Expense descriptions by category ─────────────────────────────
    descriptions = {
        "Food & Dining": [
            "Team lunch at Sakura Sushi", "Morning coffee - Blue Bottle",
            "Grocery run at Whole Foods", "Client dinner at Osteria",
            "Catering for team meeting", "Afternoon snacks from deli",
            "Working lunch delivery", "Coffee beans for office",
            "Birthday cake for colleague", "Post-meeting drinks",
        ],
        "Transportation": [
            "Uber to client meeting", "Monthly parking pass",
            "Gas station fill-up", "Lyft to airport",
            "Bus pass renewal", "Toll charges - bridge",
            "Car wash", "Oil change service",
            "Parking meter downtown", "Taxi from hotel",
        ],
        "Office Supplies": [
            "Printer toner cartridge", "Notebooks and pens",
            "GitHub Copilot subscription", "Adobe Creative Cloud",
            "Ergonomic keyboard", "Monitor stand",
            "Whiteboard markers", "USB-C hub adapter",
            "Desk organizer", "Post-it notes bulk pack",
        ],
        "Travel": [
            "Flight to PyCon US", "Hotel - tech conference",
            "Airbnb for client visit", "Conference registration fee",
            "Train ticket to workshop", "Checked baggage fee",
            "Airport lounge access", "Travel insurance",
            "Hotel room service", "Rental car for site visit",
        ],
        "Utilities": [
            "Monthly internet bill", "Cell phone plan",
            "AWS hosting charges", "Zoom Pro subscription",
            "Slack workspace billing", "Domain name renewal",
            "SSL certificate", "Cloud storage upgrade",
            "VPN service annual", "Electricity bill - office",
        ],
    }

    # ── Amount ranges by category ────────────────────────────────────
    amount_ranges = {
        "Food & Dining": (8.50, 125.00),
        "Transportation": (5.00, 85.00),
        "Office Supplies": (12.00, 180.00),
        "Travel": (50.00, 650.00),
        "Utilities": (15.00, 120.00),
    }

    # ── Generate expenses ────────────────────────────────────────────
    random.seed(42)  # Reproducible data
    expenses = []

    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)
    days_range = (end_date - start_date).days

    for user in users:
        # Each user gets 70-90 expenses across the year
        num_expenses = random.randint(70, 90)
        for _ in range(num_expenses):
            category = random.choice(categories)
            cat_name = category.name
            desc_list = descriptions[cat_name]
            min_amt, max_amt = amount_ranges[cat_name]

            expense = Expense(
                amount=round(random.uniform(min_amt, max_amt), 2),
                description=random.choice(desc_list),
                expense_date=start_date + timedelta(days=random.randint(0, days_range)),
                user_id=user.id,
                category_id=category.id,
            )
            expenses.append(expense)

    session.add_all(expenses)
    session.commit()

    # ── Print summary ────────────────────────────────────────────────
    total_expenses = session.query(Expense).count()
    print(f"Database seeded: {DB_PATH}")
    print(f"  Users: {len(users)}")
    print(f"  Categories: {len(categories)}")
    print(f"  Expenses: {total_expenses}")
    print()

    for user in users:
        user_count = session.query(Expense).filter(Expense.user_id == user.id).count()
        print(f"  {user.name}: {user_count} expenses")

    print()
    print("Monthly distribution for Elena Rodriguez:")
    from sqlalchemy import func, extract
    monthly = (
        session.query(
            extract("month", Expense.expense_date).label("month"),
            func.count(Expense.id).label("count"),
            func.sum(Expense.amount).label("total"),
        )
        .filter(Expense.user_id == users[0].id)
        .group_by(extract("month", Expense.expense_date))
        .order_by("month")
        .all()
    )
    for row in monthly:
        month_name = date(2024, int(row.month), 1).strftime("%B")
        print(f"  {month_name}: {row.count} expenses, ${row.total:.2f}")

    session.close()
    print("\nDone! Run your audit against this database.")


if __name__ == "__main__":
    seed()

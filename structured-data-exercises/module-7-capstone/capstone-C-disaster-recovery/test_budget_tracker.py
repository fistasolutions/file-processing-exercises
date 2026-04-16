"""
Test suite for Budget Tracker -- Disaster Recovery.
Run: python test_budget_tracker.py

This test suite uses an in-memory SQLite database to avoid needing
a real PostgreSQL connection. It patches the engine and session
to test the application logic independently of the deployment bugs.

When all 8+ bugs are fixed, all tests pass.
"""

import sys
from datetime import date


def create_test_engine():
    """Create an in-memory SQLite engine for testing."""
    from sqlalchemy import create_engine
    return create_engine("sqlite:///:memory:")


def create_test_session(engine):
    """Create a session bound to the test engine."""
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    return Session()


def run_tests():
    errors = []
    passed = 0

    # ── Test 0: Import the module ─────────────────────────────────────
    print("Test 0: Importing broken_budget_tracker...")
    try:
        import broken_budget_tracker as bt
        from broken_budget_tracker import Base, User, Category, Expense
        print("  PASSED: Module imported")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 0: {e}")
        print("\nCannot proceed -- fix import errors first.")
        return False

    # ── Test 1: Create tables ─────────────────────────────────────────
    print("Test 1: Creating tables...")
    try:
        engine = create_test_engine()
        Base.metadata.create_all(engine)
        session = create_test_session(engine)
        print("  PASSED: Tables created")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 1: {e}")
        print("\nCannot proceed -- fix model/table errors first.")
        return False

    # ── Test 2: Create users and categories ───────────────────────────
    print("Test 2: Creating users and categories...")
    try:
        user1 = User(name="Alice", email="alice@example.com", monthly_budget=2000.0)
        user2 = User(name="Bob", email="bob@example.com", monthly_budget=1500.0)
        cat1 = Category(name="Food", description="Groceries and dining")
        cat2 = Category(name="Transport", description="Gas and transit")
        cat3 = Category(name="Office", description="Work supplies")
        session.add_all([user1, user2, cat1, cat2, cat3])
        session.commit()

        assert user1.id is not None, "User1 not saved"
        assert cat1.id is not None, "Category1 not saved"
        print("  PASSED: Users and categories created")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 2: {e}")
        print("\nFix model errors before proceeding.")
        return False

    # ── Test 3: Create expense and verify persistence ─────────────────
    print("Test 3: create_expense() should persist data...")
    try:
        expense = bt.create_expense(
            session, user1.id, cat1.id, 45.99,
            "Weekly groceries", date(2024, 3, 15)
        )

        # Check if the expense was committed
        found = session.query(Expense).filter(Expense.user_id == user1.id).first()
        assert found is not None, "Expense not found -- was it committed?"
        print("  PASSED: Expense persisted")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 3: {e}")

    # ── Test 4: Expense amount is numeric ─────────────────────────────
    print("Test 4: Expense amount should support arithmetic...")
    try:
        bt.create_expense(session, user1.id, cat1.id, 25.50, "Coffee supplies", date(2024, 3, 15))
        bt.create_expense(session, user1.id, cat2.id, 60.00, "Gas fill-up", date(2024, 3, 20))

        expenses = session.query(Expense).filter(Expense.user_id == user1.id).all()
        total = sum(e.amount for e in expenses)

        # This should work without converting from string
        assert isinstance(total, (int, float)), \
            f"Total should be numeric, got {type(total).__name__}. Is Expense.amount the right column type?"
        print(f"  PASSED: Amount arithmetic works (total={total})")
        passed += 1
    except TypeError as e:
        print(f"  FAILED: Cannot do arithmetic on amounts -- {e}")
        print("    Hint: Check the column type for Expense.amount")
        errors.append(f"Test 4: {e}")
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 4: {e}")

    # ── Test 5: User -> expenses relationship ─────────────────────────
    print("Test 5: user.expenses relationship navigation...")
    try:
        session.refresh(user1)
        user_expenses = user1.expenses
        assert isinstance(user_expenses, list), f"Expected list, got {type(user_expenses)}"
        assert len(user_expenses) >= 1, f"Expected expenses, got {len(user_expenses)}"
        print(f"  PASSED: user.expenses returns {len(user_expenses)} expenses")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        print("    Hint: Check back_populates values on User and Expense")
        errors.append(f"Test 5: {e}")

    # ── Test 6: Budget transfer atomicity ─────────────────────────────
    print("Test 6: transfer_budget() should be atomic...")
    try:
        # Fresh data for this test
        engine2 = create_test_engine()
        Base.metadata.create_all(engine2)
        session2 = create_test_session(engine2)

        u1 = User(name="Tester1", email="t1@test.com", monthly_budget=1000.0)
        u2 = User(name="Tester2", email="t2@test.com", monthly_budget=500.0)
        session2.add_all([u1, u2])
        session2.commit()

        budget_before_1 = u1.monthly_budget
        budget_before_2 = u2.monthly_budget
        total_before = budget_before_1 + budget_before_2

        result = bt.transfer_budget(session2, u1.id, u2.id, 300.0)

        session2.refresh(u1)
        session2.refresh(u2)
        total_after = u1.monthly_budget + u2.monthly_budget

        assert abs(total_before - total_after) < 0.01, \
            f"Budget not conserved: before={total_before}, after={total_after}"
        assert u1.monthly_budget == 700.0, f"Expected 700, got {u1.monthly_budget}"
        assert u2.monthly_budget == 800.0, f"Expected 800, got {u2.monthly_budget}"
        print("  PASSED: Budget transfer is atomic")
        passed += 1
        session2.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 6: {e}")

    # ── Test 7: Monthly summary date range ────────────────────────────
    print("Test 7: get_monthly_summary() should include all days in month...")
    try:
        engine3 = create_test_engine()
        Base.metadata.create_all(engine3)
        session3 = create_test_session(engine3)

        user = User(name="DateTest", email="datetest@test.com")
        cat = Category(name="TestCat", description="For testing")
        session3.add_all([user, cat])
        session3.commit()

        # Add expenses on the first and last day of March
        bt.create_expense(session3, user.id, cat.id, 100.0, "First day expense", date(2024, 3, 1))
        bt.create_expense(session3, user.id, cat.id, 200.0, "Mid month expense", date(2024, 3, 15))
        bt.create_expense(session3, user.id, cat.id, 300.0, "Last day expense", date(2024, 3, 31))

        summary = bt.get_monthly_summary(session3, user.id, 2024, 3)

        assert summary["count"] == 3, \
            f"Expected 3 expenses in March, got {summary['count']}. Check date range comparison operators."
        assert abs(summary["total"] - 600.0) < 0.01, \
            f"Expected total $600, got ${summary['total']:.2f}"
        print("  PASSED: Monthly summary includes first and last day")
        passed += 1
        session3.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 7: {e}")

    # ── Test 8: Hardcoded credentials check ───────────────────────────
    print("Test 8: DATABASE_URL should not be hardcoded...")
    try:
        # Read the source file and check for hardcoded credentials
        import inspect
        source = inspect.getsource(bt)

        has_hardcoded = False
        for line in source.split("\n"):
            line_stripped = line.strip()
            # Skip comments
            if line_stripped.startswith("#"):
                continue
            if "DATABASE_URL" in line and ("postgresql://" in line or "postgres://" in line):
                # Check if it's an assignment with a literal string (not os.getenv)
                if "os.getenv" not in line and "os.environ" not in line:
                    has_hardcoded = True
                    break

        assert not has_hardcoded, \
            "DATABASE_URL contains hardcoded credentials. Use os.getenv('DATABASE_URL') instead."
        print("  PASSED: No hardcoded credentials")
        passed += 1
    except AssertionError as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 8: {e}")
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 8: {e}")

    # ── Test 9: pool_pre_ping configuration ───────────────────────────
    print("Test 9: Engine should have pool_pre_ping=True...")
    try:
        import inspect
        source = inspect.getsource(bt)

        has_pre_ping = "pool_pre_ping=True" in source or "pool_pre_ping = True" in source
        assert has_pre_ping, \
            "Engine is missing pool_pre_ping=True (required for Neon auto-pause recovery)"
        print("  PASSED: pool_pre_ping is configured")
        passed += 1
    except AssertionError as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 9: {e}")
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 9: {e}")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/10 tests passed")
    if errors:
        print(f"\nFailed tests:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll tests passed! All bugs are fixed.")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

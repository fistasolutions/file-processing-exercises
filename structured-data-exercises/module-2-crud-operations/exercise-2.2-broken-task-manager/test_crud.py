"""
Test suite for Task Manager CRUD operations.
Run: python test_crud.py

When all 5 bugs in broken_crud.py are fixed, all tests pass.
"""

import sys
from datetime import date
from sqlalchemy import create_engine
from models import Base, Task


def setup_database():
    """Create a fresh in-memory database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


def run_tests():
    errors = []
    passed = 0

    # ── Test 1: create_task persists data ─────────────────────────────
    print("Test 1: create_task() should persist to database...")
    try:
        engine = setup_database()
        from broken_crud import create_task, get_session

        create_task(engine, "Write report", status="pending", priority=2)

        # Verify the task exists in a NEW session
        session = get_session(engine)
        tasks = session.query(Task).all()
        session.close()

        assert len(tasks) == 1, f"Expected 1 task in database, found {len(tasks)} -- data was not committed"
        assert tasks[0].title == "Write report", f"Expected 'Write report', got '{tasks[0].title}'"
        print("  PASSED: Task persisted to database")
        passed += 1
    except SyntaxError as e:
        print(f"  FAILED: Syntax error in broken_crud.py -- {e}")
        errors.append(f"Test 1: Syntax error -- {e}")
        print("\nFix the syntax error before other tests can run.")
        print(f"\nResults: {passed} passed, {len(errors)} failed")
        return False
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 1: {e}")

    # ── Test 2: get_tasks_by_status filters correctly ─────────────────
    print("Test 2: get_tasks_by_status() should filter by status...")
    try:
        engine = setup_database()
        from broken_crud import get_session
        session = get_session(engine)
        session.add(Task(title="Task A", status="pending", priority=1))
        session.add(Task(title="Task B", status="done", priority=2))
        session.add(Task(title="Task C", status="pending", priority=3))
        session.commit()
        session.close()

        from broken_crud import get_tasks_by_status
        pending = get_tasks_by_status(engine, "pending")

        assert isinstance(pending, list), f"Expected list, got {type(pending)}"
        assert len(pending) == 2, f"Expected 2 pending tasks, got {len(pending)}"
        titles = [t.title for t in pending]
        assert "Task A" in titles, "Task A should be in pending results"
        assert "Task C" in titles, "Task C should be in pending results"
        print("  PASSED: Status filter works correctly")
        passed += 1
    except SyntaxError as e:
        print(f"  FAILED: Syntax error -- {e}")
        errors.append(f"Test 2: Syntax error -- {e}")
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 2: {e}")

    # ── Test 3: update_task modifies and persists changes ─────────────
    print("Test 3: update_task() should modify fields and persist...")
    try:
        engine = setup_database()
        from broken_crud import get_session
        session = get_session(engine)
        task = Task(title="Original Title", status="pending", priority=3)
        session.add(task)
        session.commit()
        task_id = task.id
        session.close()

        from broken_crud import update_task
        updated = update_task(engine, task_id, title="Updated Title", status="in_progress")

        # Verify changes persisted in a new session
        session = get_session(engine)
        fetched = session.query(Task).filter(Task.id == task_id).first()
        session.close()

        assert fetched is not None, "Task not found after update"
        assert fetched.title == "Updated Title", f"Expected 'Updated Title', got '{fetched.title}'"
        assert fetched.status == "in_progress", f"Expected 'in_progress', got '{fetched.status}'"
        print("  PASSED: Task updated and persisted")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 3: {e}")

    # ── Test 4: delete_task handles non-existent ID ───────────────────
    print("Test 4: delete_task() should handle non-existent task ID...")
    try:
        engine = setup_database()

        from broken_crud import delete_task
        result = delete_task(engine, 9999)

        assert result is False, f"Expected False for non-existent task, got {result}"
        print("  PASSED: Non-existent delete handled gracefully")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 4: {e}")

    # ── Test 5: search_tasks returns a list of results ────────────────
    print("Test 5: search_tasks() should return a list of Task objects...")
    try:
        engine = setup_database()
        from broken_crud import get_session
        session = get_session(engine)
        session.add(Task(title="Buy groceries", status="pending", priority=2))
        session.add(Task(title="Buy birthday gift", status="pending", priority=1))
        session.add(Task(title="Read a book", status="done", priority=4))
        session.commit()
        session.close()

        from broken_crud import search_tasks
        results = search_tasks(engine, "Buy")

        assert isinstance(results, list), f"Expected list, got {type(results).__name__}. Did you forget .all()?"
        assert len(results) == 2, f"Expected 2 results for 'Buy', got {len(results)}"
        titles = [t.title for t in results]
        assert "Buy groceries" in titles, "'Buy groceries' should be in results"
        assert "Buy birthday gift" in titles, "'Buy birthday gift' should be in results"
        print("  PASSED: Search returns correct list of results")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 5: {e}")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/5 tests passed")
    if errors:
        print(f"\nFailed tests:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll tests passed! All 5 bugs are fixed.")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

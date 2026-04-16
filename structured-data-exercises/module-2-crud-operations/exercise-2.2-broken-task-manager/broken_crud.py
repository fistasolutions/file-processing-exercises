"""
Task Manager -- CRUD Operations
WARNING: This file contains 5 bugs. Do NOT use in production.
"""

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task


def get_session(engine):
    """Create and return a new session."""
    Session = sessionmaker(bind=engine)
    return Session()


def create_task(engine, title, status="pending", priority=3, due_date=None):
    """Create a new task and return it."""
    session = get_session(engine)
    task = Task(
        title=title,
        status=status,
        priority=priority,
        due_date=due_date,
    )
    session.add(task)
    # BUG: missing session.commit() -- data is added but never persisted
    session.close()
    return task


def get_tasks_by_status(engine, status):
    """Get all tasks with a specific status."""
    session = get_session(engine)
    # BUG: uses = (assignment) instead of == (comparison)
    # In SQLAlchemy, Task.status = status REASSIGNS the column descriptor
    # instead of creating a filter expression
    tasks = session.query(Task).filter(Task.status = status).all()
    session.close()
    return tasks


def update_task(engine, task_id, **kwargs):
    """Update a task's fields and return the updated task."""
    session = get_session(engine)
    task = session.query(Task).filter(Task.id == task_id).first()
    if task is None:
        session.close()
        return None
    session.commit()
    session.close()
    # BUG: modifying task AFTER session is closed -- detached instance error
    for key, value in kwargs.items():
        setattr(task, key, value)
    return task


def delete_task(engine, task_id):
    """Delete a task by ID. Returns True if deleted, False if not found."""
    session = get_session(engine)
    # BUG: no check for existence -- session.delete() crashes on None
    task = session.query(Task).filter(Task.id == task_id).first()
    session.delete(task)
    session.commit()
    session.close()
    return True


def search_tasks(engine, title_fragment):
    """Search for tasks whose title contains the given fragment."""
    session = get_session(engine)
    # BUG: returns the Query object, not actual results
    # Missing .all() at the end
    results = session.query(Task).filter(Task.title.contains(title_fragment))
    session.close()
    return results

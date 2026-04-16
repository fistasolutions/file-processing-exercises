"""Todo App — A simple command-line task manager."""

import json
import os
from datetime import datetime

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, priority="medium"):
    """Add a new task with a title and priority."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {title} (priority: {priority})")
    return task


def remove_task(task_id):
    """Remove a task by its ID."""
    tasks = load_tasks()
    original_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == original_count:
        print(f"Task #{task_id} not found.")
        return False
    save_tasks(tasks)
    print(f"Removed task #{task_id}")
    return True


def complete_task(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Completed: {task['title']}")
            return True
    print(f"Task #{task_id} not found.")
    return False


def list_tasks(show_done=False):
    """Display all tasks, optionally including completed ones."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: add_task('Your task')")
        return

    pending = [t for t in tasks if not t["done"]]
    done = [t for t in tasks if t["done"]]

    print(f"\n{'='*50}")
    print(f" TODO LIST — {len(pending)} pending, {len(done)} done")
    print(f"{'='*50}\n")

    priority_order = {"high": 0, "medium": 1, "low": 2}
    pending.sort(key=lambda t: priority_order.get(t["priority"], 1))

    for task in pending:
        marker = {"high": "!!!", "medium": " ! ", "low": "   "}.get(task["priority"], "   ")
        print(f"  [{marker}] #{task['id']} — {task['title']}")

    if show_done and done:
        print(f"\n  Completed:")
        for task in done:
            print(f"  [DONE] #{task['id']} — {task['title']}")

    print()


if __name__ == "__main__":
    list_tasks(show_done=True)

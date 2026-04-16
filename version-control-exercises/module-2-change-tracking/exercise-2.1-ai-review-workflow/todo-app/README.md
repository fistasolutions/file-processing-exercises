# Todo App

A simple command-line task manager written in Python.

## Features

- Add tasks with priority levels (high, medium, low)
- Mark tasks as complete
- Remove tasks by ID
- List tasks sorted by priority
- Persistent storage in JSON format

## Usage

```bash
python app.py          # List all tasks
```

To use interactively in Python:

```python
from app import add_task, complete_task, remove_task, list_tasks

add_task("Buy groceries", priority="high")
complete_task(1)
remove_task(2)
list_tasks(show_done=True)
```

## File Structure

- `app.py` — Main application code
- `tasks.json` — Task storage (auto-created)
- `README.md` — This file

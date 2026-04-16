# Task Manager API

A simple REST API for managing tasks, built with Flask and SQLite.

## Features

- Create, read, update tasks
- Filter by status and priority
- Task history tracking
- Seed data for quick setup

## Setup

1. `pip install -r requirements.txt`
2. `python -c "from src.database import init_db; init_db()"`
3. `python src/app.py`

## API Endpoints

- GET /api/tasks - List all tasks
- POST /api/tasks - Create a task
- PUT /api/tasks/:id - Update a task
- GET /health - Health check

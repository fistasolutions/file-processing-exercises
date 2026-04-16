# Setup Guide

## Prerequisites

- Python 3.10+
- PostgreSQL 14+
- Redis 7+

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and configure
5. Run migrations: `python manage.py migrate`
6. Start the server: `python main.py`

## Configuration

See `config/settings.yaml` for application settings.
See `config/database.ini` for database connection details.

.PHONY: run test init seed

run:
	python src/app.py

test:
	pytest tests/ -v

init:
	python -c "from src.database import init_db; init_db()"

seed:
	python -c "import json; from src.database import get_connection; conn = get_connection(); [conn.execute('INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)', (t['title'], t['description'], t['priority'])) for t in json.load(open('data/seed_tasks.json'))]; conn.commit()"

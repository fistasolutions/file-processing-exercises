"""API route handlers for task operations."""

from flask import request, jsonify
from .models import Task
from .database import get_connection, query_tasks

def register_routes(app):
    """Register all API routes with the Flask app."""

    @app.route("/api/tasks", methods=["GET"])
    def list_tasks():
        status = request.args.get("status")
        priority = request.args.get("priority")
        tasks = query_tasks(status=status, priority=priority)
        return jsonify({"tasks": tasks, "count": len(tasks)})

    @app.route("/api/tasks", methods=["POST"])
    def create_task():
        data = request.get_json()
        if not data or not data.get("title"):
            return jsonify({"error": "Title is required"}), 400
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (data["title"], data.get("description", ""), data.get("priority", "medium"))
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return jsonify({"id": task_id, "message": "Task created"}), 201

    @app.route("/api/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json()
        conn = get_connection()
        conn.execute(
            "UPDATE tasks SET status = ?, priority = ? WHERE id = ?",
            (data.get("status", "pending"), data.get("priority", "medium"), task_id)
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Task updated"})

from flask import Blueprint, current_app, jsonify, request

bp = Blueprint("tasks", __name__)


def _store():
    return current_app.config["TASKS"]


@bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify(error="title is required"), 400
    tasks = _store()
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return jsonify(task), 201


@bp.get("/tasks")
def list_tasks():
    return jsonify(_store())

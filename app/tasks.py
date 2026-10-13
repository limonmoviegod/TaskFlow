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
    tasks = _store()
    done = request.args.get("done")
    if done is not None:
        flag = done.lower() == "true"
        tasks = [t for t in tasks if t["done"] == flag]
    return jsonify(tasks)


@bp.patch("/tasks/<int:task_id>/done")
def mark_done(task_id):
    for task in _store():
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)
    return jsonify(error="task not found"), 404

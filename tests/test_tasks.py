from app import create_app


def make_client():
    return create_app().test_client()


def test_create_and_list():
    c = make_client()
    r = c.post("/tasks", json={"title": "A"})
    assert r.status_code == 201
    assert r.get_json() == {"id": 1, "title": "A", "done": False}
    assert len(c.get("/tasks").get_json()) == 1


def test_empty_title_rejected():
    r = make_client().post("/tasks", json={"title": "  "})
    assert r.status_code == 400

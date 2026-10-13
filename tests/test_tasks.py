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


def test_mark_done_and_filter():
    c = make_client()
    c.post("/tasks", json={"title": "A"})
    c.post("/tasks", json={"title": "B"})
    assert c.patch("/tasks/1/done").get_json()["done"] is True
    done = c.get("/tasks?done=true").get_json()
    todo = c.get("/tasks?done=false").get_json()
    assert [t["id"] for t in done] == [1]
    assert [t["id"] for t in todo] == [2]


def test_mark_done_not_found():
    assert make_client().patch("/tasks/999/done").status_code == 404

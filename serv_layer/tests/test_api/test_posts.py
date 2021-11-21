import json

import pytest

from services.post import Post as ServicePost


def test_create_post(test_app, monkeypatch):
    test_request_payload = {"title": "something", "body": "something else", "is_published": True}
    test_response_payload = {"id": 1}

    async def mock_post(**kwargs):
        return 1

    monkeypatch.setattr(ServicePost, "create", mock_post)

    response = test_app.post("/api/post", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/api/post", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_app.post("/api/post", data=json.dumps({"title": "1", "body": "2"}))
    assert response.status_code == 422


def test_read_post(test_app, monkeypatch):
    test_data = {"id": 1, "title": "something", "body": "something else", "is_published": True, "created": None, "modified": None}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(ServicePost, "get", mock_get)

    response = test_app.get("/api/post/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_post_incorrect_id(test_app, monkeypatch):

    async def mock_get(id):
        return None

    monkeypatch.setattr(ServicePost, "get", mock_get)

    response = test_app.get("/api/post/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found"

    response = test_app.get("/api/post/0")
    assert response.status_code == 422


def test_read_all_posts(test_app, monkeypatch):
    test_data = [
        {"title": "something", "body": "something else", "id": 1, "is_published" : True, "created": None, "modified": None},
        {"title": "someone", "body": "someone else", "id": 2, "is_published" : True, "created": None, "modified": None}
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(ServicePost, "get_all", mock_get_all)

    response = test_app.get("/api/post/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_post(test_app, monkeypatch):
    test_request_payload = {"title": "someone", "body": "someone else", "is_published": True}
    test_response_payload = {"id": 1}

    async def mock_get(id):
        return test_response_payload

    monkeypatch.setattr(ServicePost, "get", mock_get)

    async def mock_put(id, **kwargs):
        return None

    monkeypatch.setattr(ServicePost, "put", mock_put)

    response = test_app.put("/api/post/1", data=json.dumps(test_request_payload))
    assert response.status_code == 200
    assert response.json() == None


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"body": "bar"}, 422],
        [999, {"title": "foo", "body": "bar", "is_published": True}, 404],
        [1, {"title": "1", "body": "bar"}, 422],
        [1, {"title": "foo", "body": "1"}, 422],
        [0, {"title": "foo", "body": "bar"}, 422],
    ],
)
def test_update_post_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(ServicePost, "get", mock_get)

    response = test_app.put(f"/api/post/{id}", data=json.dumps(payload),)
    assert response.status_code == status_code


def test_remove_post(test_app, monkeypatch):
    test_data = {"title": "something", "body": "something else", "id": 1}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(ServicePost, "get", mock_get)

    async def mock_delete(id):
        return None

    monkeypatch.setattr(ServicePost, "delete", mock_delete)

    response = test_app.delete("/api/post/1")
    assert response.status_code == 200
    assert response.json() == None


def test_remove_post_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(ServicePost, "get", mock_get)

    response = test_app.delete("/api/post/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found"

    response = test_app.delete("/api/post/0")
    assert response.status_code == 422

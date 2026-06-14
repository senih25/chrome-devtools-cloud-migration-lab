import importlib
import sys
from types import SimpleNamespace

import pytest


class DummyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class FakeQuery:
    def fetch(self, *args, **kwargs):
        return ["old-key-1", "old-key-2"]


@pytest.fixture
def module(monkeypatch):
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "test-project")

    sys.modules.pop("main", None)
    main = importlib.import_module("main")
    main.app.testing = True
    return main


@pytest.fixture
def client(module):
    return module.app.test_client()


def test_trim_rejects_without_task_headers(client):
    response = client.post("/trim", data={"guestbook_name": "test"})
    assert response.status_code == 403


def test_enqueue_trim_task_calls_taskqueue_add(module, monkeypatch):
    calls = []

    def fake_add(**kwargs):
        calls.append(kwargs)

    monkeypatch.setattr(module, "taskqueue", SimpleNamespace(add=fake_add))

    assert module.enqueue_trim_task("test-book") is True
    assert len(calls) == 1
    assert calls[0]["queue_name"] == "trim-queue"
    assert calls[0]["url"] == "/trim"
    assert calls[0]["method"] == "POST"
    assert calls[0]["params"]["guestbook_name"] == "test-book"


def test_trim_accepts_task_headers_and_deletes_stale_keys(module, client, monkeypatch):
    deleted = []

    monkeypatch.setattr(module.client, "context", lambda: DummyContext())
    monkeypatch.setattr(module, "book_key", lambda guestbook_name: None)
    monkeypatch.setattr(module.Greeting, "query_book", classmethod(lambda cls, ancestor: FakeQuery()))
    monkeypatch.setattr(module.ndb, "delete_multi", lambda keys: deleted.extend(keys))

    response = client.post(
        "/trim",
        data={"guestbook_name": "test-book"},
        headers={
            "X-AppEngine-QueueName": "trim-queue",
            "X-AppEngine-TaskName": "task-123",
            "X-AppEngine-TaskRetryCount": "0",
        },
    )

    assert response.status_code == 200
    assert deleted == ["old-key-1", "old-key-2"]


def test_sign_enqueues_trim_task(module, client, monkeypatch):
    calls = []

    monkeypatch.setattr(module.client, "context", lambda: DummyContext())
    monkeypatch.setattr(module, "book_key", lambda guestbook_name: None)
    monkeypatch.setattr(module.Greeting, "put", lambda self: None)
    monkeypatch.setattr(
        module,
        "enqueue_trim_task",
        lambda guestbook_name: calls.append(guestbook_name) or True,
    )

    response = client.post(
        "/sign",
        data={
            "guestbook_name": "test-book",
            "content": "synthetic hello",
        },
    )

    assert response.status_code == 302
    assert calls == ["test-book"]
    assert response.headers["Location"] == "/?guestbook_name=test-book"

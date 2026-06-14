import importlib
import json
import sys
from types import SimpleNamespace

import pytest


class DummyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class FakeQuery:
    def __init__(self, result=None):
        self.result = result or ["old-key-1", "old-key-2"]
        self.fetch_calls = []

    def fetch(self, *args, **kwargs):
        self.fetch_calls.append({"args": args, "kwargs": kwargs})
        return self.result


class FakeCloudTasksClient:
    def __init__(self):
        self.queue_path_calls = []
        self.create_task_calls = []

    def queue_path(self, project_id, location, queue_name):
        self.queue_path_calls.append((project_id, location, queue_name))
        return f"projects/{project_id}/locations/{location}/queues/{queue_name}"

    def create_task(self, request):
        self.create_task_calls.append(request)
        return {"name": "fake-task"}


@pytest.fixture
def module(monkeypatch):
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "test-project")
    monkeypatch.setenv("CLOUD_TASKS_LOCATION", "europe-west1")
    monkeypatch.delenv("CLOUD_TASKS_QUEUE", raising=False)

    sys.modules.pop("main", None)
    main = importlib.import_module("main")
    main.app.testing = True
    return main


@pytest.fixture
def client(module):
    return module.app.test_client()


def test_build_trim_task_has_expected_shape(module):
    task = module.build_trim_task("test-book")
    request_data = task["app_engine_http_request"]

    assert request_data["relative_uri"] == "/trim"
    assert request_data["http_method"] == "POST"
    assert request_data["headers"]["Content-Type"] == "application/json"
    assert json.loads(request_data["body"].decode("utf-8")) == {
        "guestbook_name": "test-book"
    }


def test_enqueue_trim_task_calls_fake_client(module):
    fake_client = FakeCloudTasksClient()

    assert module.enqueue_trim_task("test-book", client=fake_client) is True
    assert fake_client.queue_path_calls == [
        ("test-project", "europe-west1", "trim-queue")
    ]
    assert len(fake_client.create_task_calls) == 1

    request_data = fake_client.create_task_calls[0]
    assert request_data["parent"] == (
        "projects/test-project/locations/europe-west1/queues/trim-queue"
    )
    task = request_data["task"]["app_engine_http_request"]
    assert task["relative_uri"] == "/trim"
    assert task["http_method"] == "POST"
    assert task["headers"]["Content-Type"] == "application/json"
    assert json.loads(task["body"].decode("utf-8")) == {
        "guestbook_name": "test-book"
    }


def test_trim_rejects_without_task_headers(client):
    response = client.post("/trim", json={"guestbook_name": "test"})
    assert response.status_code == 403


def test_trim_accepts_task_headers_and_preserves_keep_count(
    module, client, monkeypatch
):
    deleted = []
    fake_query = FakeQuery()

    module.client = SimpleNamespace(context=lambda: DummyContext())
    monkeypatch.setattr(module, "book_key", lambda guestbook_name: None)
    monkeypatch.setattr(
        module.Greeting,
        "query_book",
        classmethod(lambda cls, ancestor: fake_query),
    )
    monkeypatch.setattr(module.ndb, "delete_multi", lambda keys: deleted.extend(keys))

    response = client.post(
        "/trim",
        json={"guestbook_name": "test-book"},
        headers={
            "X-AppEngine-QueueName": "trim-queue",
            "X-AppEngine-TaskName": "task-123",
            "X-AppEngine-TaskRetryCount": "0",
        },
    )

    assert response.status_code == 200
    assert deleted == ["old-key-1", "old-key-2"]
    assert fake_query.fetch_calls == [
        {"args": (), "kwargs": {"offset": module.KEEP_GREETING_COUNT, "keys_only": True}}
    ]


def test_sign_writes_greeting_and_calls_enqueue_helper(module, client, monkeypatch):
    calls = []
    written_contents = []

    module.client = SimpleNamespace(context=lambda: DummyContext())
    monkeypatch.setattr(module, "book_key", lambda guestbook_name: None)
    monkeypatch.setattr(
        module.Greeting,
        "put",
        lambda self: written_contents.append(self.content),
    )
    monkeypatch.setattr(
        module,
        "enqueue_trim_task",
        lambda guestbook_name, client=None: calls.append(guestbook_name) or True,
    )

    response = client.post(
        "/sign",
        data={
            "guestbook_name": "test-book",
            "content": "synthetic hello",
        },
    )

    assert response.status_code == 302
    assert written_contents == ["synthetic hello"]
    assert calls == ["test-book"]
    assert response.headers["Location"] == "/?guestbook_name=test-book"


def test_module_08_folder_has_no_bundled_taskqueue_usage():
    source = open("main.py", "r", encoding="utf-8").read()

    forbidden_import = "google.appengine.api" + ".taskqueue"
    forbidden_call = "taskqueue" + ".add"

    assert forbidden_import not in source
    assert forbidden_call not in source


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))

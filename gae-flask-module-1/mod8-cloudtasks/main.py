import json
import logging
import os

from flask import Flask, redirect, render_template, request
from google.cloud import ndb
from google.cloud import tasks_v2


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
client = None

DEFAULT_GUESTBOOK_NAME = "default_guestbook"
TRIM_QUEUE_NAME = "trim-queue"
KEEP_GREETING_COUNT = 10


class Book(ndb.Model):
    """Guestbook ancestor entity."""


class Greeting(ndb.Model):
    """A guestbook greeting."""

    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.date)


def book_key(guestbook_name):
    safe_name = guestbook_name or DEFAULT_GUESTBOOK_NAME
    return ndb.Key("Book", safe_name)


def get_ndb_client():
    global client

    if client is None:
        client = ndb.Client()
    return client


def get_cloud_tasks_client():
    return tasks_v2.CloudTasksClient()


def build_trim_task(guestbook_name: str) -> dict:
    safe_name = guestbook_name or DEFAULT_GUESTBOOK_NAME
    body = json.dumps({"guestbook_name": safe_name}).encode("utf-8")
    return {
        "app_engine_http_request": {
            "http_method": "POST",
            "relative_uri": "/trim",
            "headers": {"Content-Type": "application/json"},
            "body": body,
        }
    }


def enqueue_trim_task(guestbook_name: str, client=None):
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("CLOUD_TASKS_LOCATION")
    queue_name = os.environ.get("CLOUD_TASKS_QUEUE", TRIM_QUEUE_NAME)

    if not project_id:
        raise RuntimeError("GOOGLE_CLOUD_PROJECT is required for Cloud Tasks.")
    if not location:
        raise RuntimeError("CLOUD_TASKS_LOCATION is required for Cloud Tasks.")

    cloud_tasks_client = client or get_cloud_tasks_client()
    parent = cloud_tasks_client.queue_path(project_id, location, queue_name)
    task = build_trim_task(guestbook_name)
    cloud_tasks_client.create_task(request={"parent": parent, "task": task})
    logging.info("Trim task enqueued for guestbook.")
    return True


@app.route("/", methods=["GET"])
def root():
    guestbook_name = request.args.get("guestbook_name", DEFAULT_GUESTBOOK_NAME)

    with get_ndb_client().context():
        greetings_query = Greeting.query_book(book_key(guestbook_name))
        greetings = greetings_query.fetch(10)

    return render_template(
        "index.html",
        greetings=greetings,
        guestbook_name=guestbook_name,
    )


@app.route("/sign", methods=["POST"])
def update_guestbook():
    guestbook_name = request.form.get("guestbook_name", DEFAULT_GUESTBOOK_NAME)

    with get_ndb_client().context():
        greeting = Greeting(
            parent=book_key(guestbook_name),
            content=request.form.get("content", ""),
        )
        greeting.put()

    enqueue_trim_task(guestbook_name)

    return redirect("/?guestbook_name={}".format(guestbook_name))


@app.route("/trim", methods=["POST"])
def trim():
    queue_name = request.headers.get("X-AppEngine-QueueName")
    task_name = request.headers.get("X-AppEngine-TaskName")

    if not queue_name or not task_name:
        logging.warning("Rejected non-task /trim request.")
        return ("forbidden", 403)

    payload = request.get_json(silent=True) or {}
    guestbook_name = (
        request.form.get("guestbook_name")
        or payload.get("guestbook_name")
        or DEFAULT_GUESTBOOK_NAME
    )

    with get_ndb_client().context():
        stale_keys = Greeting.query_book(book_key(guestbook_name)).fetch(
            offset=KEEP_GREETING_COUNT,
            keys_only=True,
        )

        if stale_keys:
            ndb.delete_multi(stale_keys)

    logging.info("Trim task completed for guestbook; deleted=%s", len(stale_keys))
    return ("ok", 200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="127.0.0.1", port=port, debug=True)

import logging
import os

from flask import Flask, redirect, render_template, request
from google.cloud import ndb

try:
    from google.appengine.api import taskqueue, wrap_wsgi_app
except ImportError:
    taskqueue = None

    def wrap_wsgi_app(wsgi_app):
        return wsgi_app


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)

client = ndb.Client()

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


def enqueue_trim_task(guestbook_name):
    """Enqueue an App Engine bundled Task Queue push task.

    In local unit tests, the bundled taskqueue API is monkeypatched.
    If the API is unavailable locally, the app logs and continues.
    """

    if taskqueue is None:
        logging.warning("Taskqueue API unavailable; skipping local enqueue.")
        return False

    taskqueue.add(
        queue_name=TRIM_QUEUE_NAME,
        url="/trim",
        method="POST",
        params={"guestbook_name": guestbook_name or DEFAULT_GUESTBOOK_NAME},
    )
    logging.info("Trim task enqueued for guestbook.")
    return True


@app.route("/", methods=["GET"])
def root():
    guestbook_name = request.args.get("guestbook_name", DEFAULT_GUESTBOOK_NAME)

    with client.context():
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

    with client.context():
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

    with client.context():
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

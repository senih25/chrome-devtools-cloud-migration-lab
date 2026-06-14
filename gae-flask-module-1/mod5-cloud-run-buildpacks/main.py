import os
from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request
from google.cloud import datastore

app = Flask(__name__)

client = datastore.Client()


def book_key(guestbook_name):
    """Create the parent key used to group guestbook entries."""
    return client.key("Book", guestbook_name or "*notitle*")


def fetch_greetings(guestbook_name, limit=20):
    """Fetch recent greetings using the Cloud Datastore client library."""
    ancestor_key = book_key(guestbook_name)
    query = client.query(kind="Greeting", ancestor=ancestor_key)
    query.order = ["-date"]
    return list(query.fetch(limit=limit))


def create_greeting(guestbook_name, content):
    """Create a Greeting entity under a Book ancestor."""
    key = client.key("Book", guestbook_name or "*notitle*", "Greeting")
    entity = datastore.Entity(key=key)
    entity.update(
        {
            "content": content,
            "date": datetime.now(timezone.utc),
        }
    )
    client.put(entity)
    return entity


@app.route("/")
def display_guestbook():
    guestbook_name = request.args.get("guestbook_name", "")
    greetings = fetch_greetings(guestbook_name)

    return render_template(
        "index.html",
        guestbook_name=guestbook_name,
        greetings=greetings,
    )


@app.route("/sign", methods=["POST"])
def update_guestbook():
    guestbook_name = request.form.get("guestbook_name", "")
    content = request.form.get("content", "")

    if content:
        create_greeting(guestbook_name, content)

    return redirect(f"/?guestbook_name={guestbook_name}")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False,
        threaded=True,
    )

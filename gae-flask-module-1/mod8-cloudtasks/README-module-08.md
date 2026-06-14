# Module 08 - Cloud Tasks Baseline

## Purpose

This module adds an isolated Cloud Tasks baseline for the guestbook sample by copying the Module 07 push-task baseline into a new folder and replacing bundled Task Queue enqueue logic with Cloud Tasks helper logic.

## Module 07 -> Module 08 Migration

- Source folder: `gae-flask-module-1/mod7-gaetasks-baseline/`
- Target folder: `gae-flask-module-1/mod8-cloudtasks/`
- Bundled Task Queue enqueue logic is replaced with `CloudTasksClient.create_task(...)`.
- Module 07 remains unchanged.

## Preserved Routes

- `GET /`
- `POST /sign`
- `POST /trim`

## Preserved Behavior

- `KEEP_GREETING_COUNT = 10`
- `TRIM_QUEUE_NAME = "trim-queue"`
- `POST /sign` stores a synthetic `Greeting` and enqueues trim work.
- `POST /trim` validates task-origin headers and deletes stale greetings.

## Cloud Tasks Helper

The helper design is intentionally testable:

- `get_cloud_tasks_client()`
- `build_trim_task(guestbook_name: str)`
- `enqueue_trim_task(guestbook_name: str, client=None)`

Runtime config:

- `GOOGLE_CLOUD_PROJECT`
- `CLOUD_TASKS_LOCATION`
- `CLOUD_TASKS_QUEUE`
- `PORT`

Payload contract:

```json
{"guestbook_name": "synthetic-book"}
```

Do not include user content, timestamps, identifiers, health data, raw logs, or secrets in the payload.

## Fake-Client Test Strategy

Unit tests must not call the real Cloud Tasks API.

Tests use a fake client to verify:

- `queue_path(...)` shape
- `create_task(...)` request payload
- `relative_uri: /trim`
- `http_method: POST`
- `Content-Type: application/json`
- payload decodes to `guestbook_name`

## Local Validation Commands

```powershell
cd gae-flask-module-1\mod8-cloudtasks
python -m pytest -q
python main_test.py
python main.py
```

## DevTools Evidence Plan

Browser-visible evidence:

- Network: `GET /` returns `200`
- Network: `POST /sign` returns redirect
- Network: local manual `POST /trim` validation request
- Console: no critical errors
- Application: no sensitive storage, cookies, or cache

## Cloud Logging Evidence Plan

Server-side evidence:

- task creation attempt or success
- Cloud Tasks dispatch to `POST /trim`
- App Engine request log for `POST /trim`
- retry or failure logs if any

Do not claim that Cloud Tasks dispatch is visible in the browser Network panel.

## Closed Gates

- no deploy
- no API enablement
- no queue creation
- no IAM

## Safety

- synthetic guestbook data only
- no PHI
- no real health data
- no e-Nabiz export
- no TCKN
- no secrets or API keys

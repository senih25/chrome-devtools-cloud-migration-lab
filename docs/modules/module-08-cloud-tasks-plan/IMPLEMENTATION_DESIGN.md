# Module 08-B - Cloud Tasks Implementation Design

## Status

Repo: `SocialRightLabs/chrome-devtools-cloud-migration-lab`

Scope:

- Plan only
- Docs only
- No code
- No deploy
- No API enablement
- No queue creation
- No IAM changes

## Goal

Design the small implementation PR that migrates the Module 07 App Engine bundled Task Queue baseline to Cloud Tasks.

Module 07 currently uses App Engine bundled `taskqueue.add(...)`.

Module 08 will use `CloudTasksClient.create_task(...)`.

## Module 07 to Module 08 Mapping

| Module 07 | Module 08 |
|---|---|
| `google.appengine.api.taskqueue` | `google.cloud.tasks_v2.CloudTasksClient` |
| `taskqueue.add(...)` | `create_task(...)` |
| `queue.yaml` | Cloud Tasks queue lifecycle |
| form params payload | JSON request body |
| App Engine bundled service | standalone Cloud Tasks API |
| `/trim` handler | preserved |
| dispatch evidence | Cloud Logging |

## Source Baseline

Module 07 source of truth:

- `gae-flask-module-1/mod7-gaetasks-baseline/`
- `Book`
- `Greeting`
- `POST /sign`
- `POST /trim`
- `trim-queue`
- `KEEP_GREETING_COUNT = 10`
- `taskqueue.add(...)`

## Proposed Implementation Target

Do not edit the Module 07 baseline in place.

Create a new isolated module folder:

- `gae-flask-module-1/mod8-cloudtasks/`

The new folder should copy the Module 07 baseline and then replace the task enqueue implementation.

## Files Expected in the Future Implementation PR

Expected future code PR scope:

- `gae-flask-module-1/mod8-cloudtasks/main.py`
- `gae-flask-module-1/mod8-cloudtasks/main_test.py`
- `gae-flask-module-1/mod8-cloudtasks/requirements.txt`
- `gae-flask-module-1/mod8-cloudtasks/README-module-08.md`
- supporting template/config files copied from Module 07 as needed

Do not modify Module 07 behavior.

## New Dependency

Expected runtime dependency:

```txt
google-cloud-tasks
```

Existing guestbook dependencies should remain scoped to the copied Module 08 folder.

## `enqueue_trim_task` Design

The public helper can remain conceptually similar:

```text
enqueue_trim_task(guestbook_name)
```

Expected responsibilities:

1. Build a Cloud Tasks client.
2. Build a queue path from explicit config.
3. Build a JSON payload.
4. Create a task targeting `POST /trim`.
5. Avoid logging raw payload content.

Expected configuration inputs:

- `GOOGLE_CLOUD_PROJECT`
- `CLOUD_TASKS_LOCATION`
- `CLOUD_TASKS_QUEUE`

Tests should inject or monkeypatch a fake Cloud Tasks client. Local unit tests must not call the real Cloud Tasks API.

## Cloud Tasks Payload Design

Minimal JSON body:

```json
{
  "guestbook_name": "test-book"
}
```

Do not include:

- user message content
- secrets
- raw logs
- health data
- personal identifiers
- large payloads

## `/trim` Handler Design

The `/trim` handler should be preserved.

Reasons:

- keeps Module 07 and Module 08 behavior comparable
- keeps the cleanup action isolated
- allows Cloud Tasks dispatch evidence to map directly to `POST /trim`

The handler should continue to validate task-origin headers and payload shape. Header assumptions must be verified against the current Cloud Tasks App Engine target behavior before implementation.

## Test Plan

Future implementation PR should include unit tests for:

1. Cloud Tasks client is called through a fake client.
2. Queue path is constructed from project, location, and queue config.
3. Task target points to `/trim`.
4. Task body is JSON and contains only `guestbook_name`.
5. `POST /trim` without task headers returns `403`.
6. `POST /trim` with valid task-style headers and JSON payload deletes stale greetings.
7. `POST /sign` stores a `Greeting` and calls `enqueue_trim_task`.
8. No real Cloud Tasks API call is made in tests.

## DevTools Evidence Plan

Browser-visible checks:

- Network: `GET /` returns `200`
- Network: `POST /sign` returns redirect
- Network: local manual `POST /trim` validation case
- Console: no critical browser errors
- Application: no sensitive storage or cookies
- Security: HTTPS and mixed content after deploy

## Cloud Logging Evidence Plan

Server-side checks:

- task creation attempted or succeeded
- Cloud Tasks dispatch to `POST /trim`
- App Engine request log for `POST /trim`
- failure/retry cases if handler returns `4xx` or `5xx`

Do not claim that Cloud Tasks dispatch appears in the browser Network panel. It is server-to-server evidence and belongs in Cloud Logging.

## Approval Gates

Do not perform these actions without explicit approval:

- `gcloud services enable cloudtasks.googleapis.com`
- Cloud Tasks queue creation
- IAM changes
- App Engine deploy
- public endpoint exposure
- billing-impacting configuration changes
- writing live URLs into public docs

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Queue missing | task creation fails | gate queue creation and document setup |
| Wrong region/project | task path invalid | explicit env/config and tests |
| Retry loop | cost/noise risk | idempotent `/trim` and log review |
| Weak `/trim` validation | endpoint abuse risk | validate task-origin headers and payload |
| Payload overlogging | data leak risk | log shape/status only, not raw payload |

## Recommended PR Split

1. `docs(module08): add Cloud Tasks implementation design`
2. `feat(module08): add Cloud Tasks baseline module`
3. `docs(module08): add DevTools and Cloud Logging evidence checklist`
4. gated deploy/API/queue/IAM PR only after explicit approval

## Portfolio Output

This design documents a safe migration path from App Engine bundled Task Queue to Cloud Tasks while preserving DevTools and Cloud Logging evidence boundaries.

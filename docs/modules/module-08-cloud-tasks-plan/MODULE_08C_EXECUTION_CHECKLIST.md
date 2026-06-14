# Module 08-C Execution Checklist

## Purpose

Finalize the implementation contract for migrating the Module 07 App Engine bundled Task Queue baseline to Cloud Tasks.

## Source Baseline

- Source folder: `gae-flask-module-1/mod7-gaetasks-baseline/`
- Target folder: `gae-flask-module-1/mod8-cloudtasks/`
- Preserved routes:
  - `GET /`
  - `POST /sign`
  - `POST /trim`
- Preserved constants:
  - `KEEP_GREETING_COUNT = 10`
  - `trim-queue`

## Normalized Target Folder

Use only:

```text
gae-flask-module-1/mod8-cloudtasks/
```

Do not use:

```text
gae-flask-module-8/mod8-cloudtasks/
```

## Normalized Payload Contract

Use this minimal JSON payload:

```json
{"guestbook_name": "synthetic-book"}
```

Do not put user content, secrets, health data, raw logs, IDs, or timestamps into the task payload.

## Preserved Behavior

- `POST /sign` writes a synthetic `Greeting`.
- `POST /sign` enqueues a trim task after write.
- `/trim` keeps only the newest `KEEP_GREETING_COUNT` greetings.
- `/trim` validates task-origin headers.
- Module 07 remains unchanged.

## Future Code PR Boundary

The future code PR may add:

- `gae-flask-module-1/mod8-cloudtasks/main.py`
- `gae-flask-module-1/mod8-cloudtasks/main_test.py`
- `gae-flask-module-1/mod8-cloudtasks/requirements.txt`
- `gae-flask-module-1/mod8-cloudtasks/app.yaml`
- `gae-flask-module-1/mod8-cloudtasks/README-module-08.md`
- required template/static files

The future code PR must not deploy or create cloud resources.

## Fake Cloud Tasks Client Strategy

Tests must not call the real Cloud Tasks API.

Use monkeypatching or dependency injection to verify:

- `CloudTasksClient.create_task(...)` is called
- parent queue path is correctly shaped
- App Engine HTTP target uses:
  - `relative_uri: /trim`
  - `http_method: POST`
  - `Content-Type: application/json`
- payload decodes to:
  - `guestbook_name`

## DevTools Evidence

Browser-visible evidence:

- `GET /` in Network panel
- `POST /sign` in Network panel
- local manual `POST /trim` validation request if applicable
- Console has no critical errors
- Application panel has no sensitive storage/cookies/cache

## Cloud Logging Evidence

Server-side evidence:

- task creation attempt/success
- Cloud Tasks dispatch to `/trim`
- App Engine request log for `POST /trim`
- retry/failure logs if any

Do not claim that Cloud Tasks dispatch is visible in the browser Network panel.

## Closed Gates

Keep these closed unless explicitly approved:

- App Engine deploy
- Cloud Tasks API enablement
- Cloud Tasks queue creation
- IAM change
- public endpoint exposure
- billing-impacting config

## Safety

- Synthetic guestbook data only
- No PHI
- No real health data
- No e-Nabiz export
- No TCKN
- No secrets or API keys
- No medical PDFs or OCR output
- Do not publish saved Google Developer Program HTML because it may contain account/profile metadata

## Validation Commands

Before future code PR:

```powershell
rg -n "gae-flask-module-8/mod8-cloudtasks|oldest timestamp|timestamp only" docs/modules/module-08-cloud-tasks-plan
rg -n "gae-flask-module-1/mod8-cloudtasks|guestbook_name|CloudTasksClient|create_task|/trim" docs/modules/module-08-cloud-tasks-plan
```

After future code PR:

```powershell
cd gae-flask-module-1/mod8-cloudtasks
pytest -q
python main_test.py
python main.py
```

## Merge Criteria

- Docs-only diff
- No blocked paths
- No secrets
- No PHI
- Module 08 target folder is normalized
- Payload contract is normalized
- Evidence split is clear
- Gates remain closed

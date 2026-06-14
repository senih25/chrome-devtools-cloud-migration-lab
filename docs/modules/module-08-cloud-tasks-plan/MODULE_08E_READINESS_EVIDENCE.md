# Module 08-E Readiness and Evidence Checklist

## Purpose

Prepare the evidence and readiness checklist for the Module 08 Cloud Tasks baseline before any gated deploy or cloud resource work.

This document does not approve deployment.

## Current Baseline

- Source module: `gae-flask-module-1/mod7-gaetasks-baseline/`
- Target module: `gae-flask-module-1/mod8-cloudtasks/`
- Current main HEAD after Module 08-D: `2634ed8 feat(module08): add Cloud Tasks baseline (#18)`

## What Is Already Implemented

- `GET /`
- `POST /sign`
- `POST /trim`
- `KEEP_GREETING_COUNT = 10`
- `trim-queue`
- `CloudTasksClient.create_task(...)`
- task payload:
  - `guestbook_name`
- fake-client unit tests
- no `queue.yaml`
- no bundled `taskqueue.add(...)`

## Local Verification Checklist

Before any deploy discussion, verify locally:

```powershell
cd C:\Users\YeniKullanici\chrome-devtools-cloud-migration-lab\gae-flask-module-1\mod8-cloudtasks

python -m pytest -q
python main_test.py
```

Expected:

```text
6 passed
6 passed
```

## Dependency Verification

Use an isolated temporary virtual environment outside the repo.

```powershell
$VENV="$env:TEMP\mod8-cloudtasks-venv"

if (Test-Path $VENV) {
  Remove-Item -Recurse -Force $VENV
}

py -3.12 -m venv $VENV

& "$VENV\Scripts\python.exe" -m pip install --upgrade pip
& "$VENV\Scripts\python.exe" -m pip install -r requirements.txt -r requirements-test.txt
& "$VENV\Scripts\python.exe" -c "import flask; import google.cloud.tasks_v2; print('deps ok')"
& "$VENV\Scripts\python.exe" -m pytest -q
& "$VENV\Scripts\python.exe" main_test.py
```

Do not create `.venv` inside the repo.

## DevTools Evidence Checklist

Browser-visible evidence only:

- `GET /` appears in Network panel.
- `POST /sign` appears in Network panel.
- Local manual `POST /trim` validation request can be tested if applicable.
- Console has no critical errors.
- Application panel has no sensitive Local Storage, Session Storage, Cookies, IndexedDB, or Cache Storage.
- Security panel is checked only after a deployed HTTPS URL exists.

Do not claim that Cloud Tasks server-side dispatch is visible in the browser Network panel.

## Cloud Logging Evidence Checklist

Server-side evidence, only after gated deploy:

- task creation attempt/success
- Cloud Tasks dispatch to `/trim`
- App Engine request log for `POST /trim`
- retry/failure logs if any
- status/shape logs only, no payload content

## Evidence Split

| Evidence Type                   | Tool                             |
| ------------------------------- | -------------------------------- |
| Browser `GET /`                 | Chrome DevTools Network          |
| Browser `POST /sign`            | Chrome DevTools Network          |
| Local manual `/trim` request    | Chrome DevTools Network          |
| App to Cloud Tasks API          | Cloud Logging                    |
| Cloud Tasks dispatch to `/trim` | Cloud Logging                    |
| Queue state                     | Cloud Console or `gcloud`, gated |
| API enablement                  | Cloud Console or `gcloud`, gated |
| IAM                             | Cloud Console or `gcloud`, gated |

## Gated Actions

These remain closed unless explicitly approved:

- App Engine deploy
- Cloud Tasks API enablement
- Cloud Tasks queue creation
- IAM change
- public endpoint exposure
- billing-impacting config
- live URL sharing

## Pre-Deploy Readiness Questions

Do not proceed to deploy until all are answered:

1. Which Google Cloud project will be used?
2. Which region/location will be used?
3. Is Cloud Tasks API already enabled?
4. Will enabling Cloud Tasks API be approved?
5. Who owns IAM approval?
6. Will the queue be created manually or with `gcloud`?
7. What queue name will be used?
8. What retry settings will be used?
9. What logs are safe to capture?
10. What evidence will be public-safe for portfolio use?

## Safety Rules

- Synthetic guestbook data only
- No PHI
- No real health data
- No e-Nabız export
- No TCKN
- No secrets or API keys
- No medical PDFs or OCR output
- Do not publish saved Google Developer Program HTML because it may contain account/profile metadata
- Do not log payload content
- Do not expose live endpoints without approval

## Portfolio Evidence Template

Use this format after safe local verification:

```markdown
# Module 08 Cloud Tasks Baseline Evidence

## Local Tests

- `python -m pytest -q`: pass/fail
- `python main_test.py`: pass/fail

## DevTools Evidence

- Network `GET /`:
- Network `POST /sign`:
- Console:
- Application storage:

## Cloud Evidence

Not collected in Module 08-E. Deploy/API/queue/IAM remain gated.

## Safety

- synthetic data only
- no secrets
- no PHI
- no deploy
```

## Merge Criteria

- Docs-only diff
- Files restricted to `docs/modules/module-08-cloud-tasks-plan/`
- No blocked paths
- No secrets
- No PHI
- Readiness checklist added
- Deploy/API/queue/IAM gates remain closed

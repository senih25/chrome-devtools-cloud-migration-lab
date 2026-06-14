# Module 08 Reconciliation Checklist

Module 08 migrates the Module 07 App Engine Push Task Queues baseline to Cloud Tasks.

## Source of Truth

Module 07 baseline:

- `gae-flask-module-1/mod7-gaetasks-baseline/`
- `Book`
- `Greeting`
- `POST /sign`
- `POST /trim`
- `trim-queue`
- `KEEP_GREETING_COUNT = 10`

## Migration Mapping

| Module 07 Task Queue | Module 08 Cloud Tasks |
|---|---|
| `taskqueue.add(...)` | `CloudTasksClient.create_task(...)` |
| `queue.yaml` | Cloud Tasks queue lifecycle via API, Console, or `gcloud` |
| App Engine bundled service | Standalone Cloud Tasks API |
| App Engine task headers | Cloud Tasks dispatch headers / Cloud Logging evidence |
| `/trim` handler | `/trim` handler preserved |

## Evidence Split

| Evidence | Tool |
|---|---|
| `GET /` | Chrome DevTools Network |
| `POST /sign` | Chrome DevTools Network |
| Manual local `POST /trim` | Chrome DevTools Network |
| Cloud Tasks dispatch to `/trim` | Cloud Logging |
| Queue creation / queue state | Google Cloud Console or `gcloud` |
| API enablement / IAM | Gated manual approval |

## Gated Actions

Do not perform these actions without explicit approval:

- App Engine deploy
- Cloud Tasks API enablement
- queue creation
- IAM changes
- public endpoint exposure
- cost-affecting configuration changes

## Safety

- Synthetic guestbook data only
- No PHI
- No real health data
- No e-Nabız export
- No TCKN
- No secrets or API keys
- No medical PDFs or OCR output

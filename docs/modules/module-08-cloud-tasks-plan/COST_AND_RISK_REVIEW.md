# Module 08 — Cost and Risk Review

This PR enables nothing and costs nothing.

## Services that may be involved later

| Service | Why | Billing surface |
|---|---|---|
| Cloud Tasks | Queue and dispatch | Operations after free tier |
| App Engine Standard | App and task handler | Instance hours, egress |
| Datastore via Cloud NDB | Visit entities | Reads, writes, storage |
| Cloud Build and Cloud Storage | App deploy staging | Build minutes and storage |
| Cloud Logging | Dispatch evidence | Log ingestion after free allotment |
| IAM | Queue access control | Free, but misconfiguration risk |

## Cost risks

1. Forgotten running app.
2. Deploy churn.
3. Retry loops.
4. Datastore growth.

Expected demo volume should remain near zero cost if mitigations are followed.

## Quota risks

The realistic risk is retry amplification, not normal manual demo traffic.

## IAM risks

Do not normalize broad grants. Do not create service account key files. Queue management remains a human operator action.

## Public endpoint risks

POST /trim is an App Engine route. It must validate input defensively and rely on platform-set App Engine task headers for deployed task-origin validation.

## Retry and amplification risks

Cloud Tasks retries non-2xx handler responses. A handler bug can create retry storms. Use capped attempts, modest dispatch rates, and pause queue as kill switch.

## Logging risks

Log payload shape, not content. Never log headers wholesale. Screenshots of logs follow screenshot safety rules.

## Safe defaults for future implementation

- max_dispatches_per_second: 1
- max_concurrent_dispatches: 1
- max_attempts: 5
- max_backoff: 300s
- App Engine F1
- no min_instances

## Manual approval gates

No gcloud services enable, no gcloud app deploy, no queue creation, no IAM change until gates G1-G6 pass.

# Module 03 — Chrome DevTools Network Verification Plan

Evidence model for the future Cloud Tasks implementation.

## Scope honesty

Cloud Tasks dispatch from queue to POST /trim is server-to-server. It does not pass through the browser and is invisible to the deployed app's Chrome DevTools Network panel.

The evidence chain is therefore split:

| Hop | Evidence tool |
|---|---|
| Browser -> GET / | DevTools Network |
| App -> Cloud Tasks CreateTask RPC | Cloud Logging and Cloud Tasks UI |
| Cloud Tasks -> POST /trim | Cloud Logging request log |
| Local manual POST /trim | DevTools Network |

Claiming DevTools shows the queue dispatch would be wrong. The portfolio value includes documenting this boundary correctly.

## What to verify in Network

- Request appears in Network Log.
- Status, Type, Initiator, Size, Time columns.
- Headers tab.
- Payload tab.
- Preview/Response tab.
- Initiator tab.
- Timing tab.
- Preserve log across reloads.
- Filter by method or domain when needed.

## Expected deployed request flow

1. GET / returns 200.
2. Server stores visit, queries recent visits, and enqueues task before response.
3. Static assets return 200 or 304.
4. No browser-visible /trim request on deployed app.

## Expected task creation

Expected server-side task shape:

- CreateTask RPC to cloudtasks.googleapis.com.
- Parent: projects/P/locations/L/queues/Q.
- AppEngineHttpRequest.
- Method: POST.
- relative_uri: /trim.
- Content-Type: application/json.
- Body: JSON with oldest timestamp only.

## Expected worker request

- POST /trim.
- Content-Type: application/json.
- JSON body with oldest timestamp.
- App Engine task headers visible in logs.
- Local simulation may POST the same shape from the page origin.

## Status codes

| Code | Meaning |
|---|---|
| 200 GET / | Page and enqueue path healthy |
| 200 POST /trim | Task handled |
| 4xx POST /trim | Bad payload or validation failure |
| 429/503 | Throttling or overload |
| 500 | App bug; retry risk |

## Payload safety rules

Payloads contain one synthetic value only: a Unix timestamp.

Forbidden in payloads, fixtures, logs, or screenshots:

- PHI
- health data
- e-Nabız exports
- patient records
- clinical text
- identifiers
- credentials
- tokens

## Timing evidence

Record GET / timing and TTFB. If a baseline exists, compare with and without enqueue.

## Failure cases

- POST /trim with non-JSON body.
- POST /trim missing oldest key.
- Request blocking for static asset graceful degradation.
- Deployed handler 500 observed through Cloud Logging only.

## Screenshot safety

- Crop or mask account emails, private URLs, project IDs beyond demo convention, cookies, and auth context.
- Use a clean browser profile.
- Do not capture sensitive repos or data.
- Store future screenshots under docs/modules/module-03-cloud-tasks/evidence/.

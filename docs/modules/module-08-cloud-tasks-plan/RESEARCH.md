# Module 08 — Cloud Tasks Migration Research

Status: Planning only. No implementation, no deployment, no paid service enablement in this increment.

Branch: docs/module-08-cloud-tasks-plan-plan
Risk level: Medium
Evidence model: Chrome DevTools Network + Cloud Logging

## Purpose

Module 08 prepares the migration of the lab sample app from legacy App Engine Task Queue push tasks to Cloud Tasks.

This document is the source-grounded research base. Implementation is deferred to a future PR gated by IMPLEMENTATION_PLAN.md.

Module 02 migrated Datastore access from App Engine NDB to Cloud NDB. Module 08 continues the same modernization arc by removing the next legacy bundled service and replacing it with a standalone Cloud product.

## Official source links

| # | Source | URL | Verified |
|---|---|---|---|
| 1 | Google Codelab — Migrate from App Engine Task Queue Push Tasks to Cloud Tasks | https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-8-cloudtasks | 2026-06-12 |
| 2 | Google Cloud — Migrate from Task Queues to Cloud Tasks | https://cloud.google.com/tasks/docs/migrating | 2026-06-12 |
| 3 | Google Cloud — Create App Engine tasks | https://cloud.google.com/tasks/docs/creating-appengine-tasks | 2026-06-12 |
| 4 | Chrome DevTools — Inspect network activity | https://developer.chrome.com/docs/devtools/network | 2026-06-12 |

## What Cloud Tasks replaces

Cloud Tasks replaces the App Engine Task Queue API for push tasks.

Task Queue and Cloud Tasks address the same underlying queue universe, but Cloud Tasks is a standalone RPC/REST product usable from second-generation App Engine runtimes and other environments with network access and IAM credentials.

## Scope boundary

Cloud Tasks replaces push tasks only.

Task Queue pull tasks migrate to Cloud Pub/Sub and are out of scope for Module 08.

## Task Queues vs Cloud Tasks

| Dimension | App Engine Task Queue push | Cloud Tasks |
|---|---|---|
| API | Bundled SDK taskqueue.add | Standalone CloudTasksClient.create_task |
| Default queue | Default queue exists automatically | No automatic queue; queue must be created explicitly |
| Region | Implicit app region | Explicit location; must match App Engine app region |
| Payload | Form-encoded params | Raw bytes body with explicit Content-Type |
| Access control | App-internal | IAM-controlled |
| Queue management | queue.yaml | API, Console, gcloud |
| Targets | App Engine handlers | App Engine handlers or HTTP endpoints |
| Transactional enqueue | Supported | Not supported |
| Deferred tasks | Supported | Not supported |
| Namespacing | Supported | Not supported |
| Local emulator | Local dev server simulated queues | No local emulator |

## Expected architecture

Browser GET / -> Flask app on App Engine -> Cloud NDB/Datastore Greeting write under a Book ancestor -> Cloud Tasks CreateTask RPC -> Cloud Tasks queue -> server-side POST /trim handler -> delete old demo Greeting entities under a Book ancestor.

The queue to handler dispatch is server-to-server and is not browser-visible.

## Low-cost approach

This PR costs nothing. It creates documentation only.

Future implementation must use:

- one queue
- one region
- one handler: POST /trim
- demo timestamp payloads only
- no recurring or scheduled tasks
- no paid service enablement without manual approval
- disable App Engine after verification

## Risks

1. The codelab is Python 2-era. Future implementation must adapt the concept to Python 3.
2. Cloud Tasks has no local emulator.
3. Cloud Tasks has no automatic default queue.
4. Region mismatch can break task creation.
5. Non-2xx handler responses can trigger retry amplification.
6. Public handler endpoints require defensive validation.

## Open questions before implementation

1. Python 3 rewrite strategy.
2. Whether to reproduce a Task Queue baseline first.
3. Queue retry/rate config.
4. Target Google Cloud project and region.
5. Whether named-task deduplication is worth demonstrating.

## Do-not-do list

- Do not implement code in this PR.
- Do not deploy.
- Do not enable Cloud Tasks API.
- Do not create queues, service accounts, or IAM bindings.
- Do not use pull queues or Pub/Sub.
- Do not put real data in task payloads.
- Do not use PHI, health data, e-Nabız exports, patient records, clinical text, secrets, credentials, or tokens.
- Do not couple this module to sensitive health repositories at runtime.

## Source verification notes

The official sources confirm the migration direction, Cloud Tasks queue model, missing Task Queue features, lack of local emulator, App Engine task request shape, region matching, and the Network panel evidence workflow.

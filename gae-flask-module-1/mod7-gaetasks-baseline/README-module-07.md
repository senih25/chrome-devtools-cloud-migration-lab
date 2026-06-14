# Module 07 — App Engine Push Task Queues Baseline

## Status

Implementation baseline.

This module adds an App Engine bundled Task Queue push task baseline to the Cloud NDB guestbook app.

## Source

Copied from:

`gae-flask-module-1/mod2-cloud-ndb/`

## Purpose

Module 07 prepares the predecessor state for Module 08 Cloud Tasks migration.

The app writes synthetic guestbook `Greeting` entities under a `Book` ancestor and enqueues a push task that calls `/trim`.

## Architecture

1. User submits a guestbook entry.
2. `POST /sign` stores a `Greeting`.
3. The app enqueues a push task on `trim-queue`.
4. App Engine dispatches `POST /trim`.
5. `/trim` validates App Engine task headers.
6. `/trim` deletes old `Greeting` entities beyond `KEEP_GREETING_COUNT`.

## Queue

Queue file:

`queue.yaml`

Queue name:

`trim-queue`

Retry and concurrency are capped for demo safety.

## DevTools Evidence Plan

Browser-visible evidence:

- Network: `GET /` returns 200.
- Network: `POST /sign` returns 302.
- Network: manual `POST /trim` with simulated task headers returns 200.
- Console: no critical errors.
- Application: no sensitive storage or cookies.
- Security: HTTPS and no mixed content after deploy.

Server-side evidence:

- Cloud Logging for task enqueue and queue dispatch.
- Push task dispatch is server-to-server and is not fully visible in browser Network.

## Safety

Public-safe synthetic guestbook data only.

Do not include:

- PHI
- real health data
- e-Nabız exports
- TCKN
- medical PDFs or OCR output
- secrets
- API keys
- `.env` files

## Deployment

Do not deploy without explicit human approval.

Before deploy, confirm:

- cost controls
- queue retry caps
- App Engine bundled services config
- no runtime coupling to sensitive repos
- repo guardrails green

# Module 03 — Cloud NDB to Cloud Datastore Migration

Status: Active planning.
Source: Google Codelab — Module 3: Google Cloud NDB to Cloud Datastore migration.
URL: https://codelabs.developers.google.com/codelabs/cloud-gae-python-migrate-3-datastore?hl=tr

## Purpose

This module aligns the repository with the official Google Serverless Migration Station numbering.

Google Codelab Module 03 is not Cloud Tasks. It is the optional migration from Cloud NDB to Cloud Datastore.

The goal is to start from the completed Module 02 Cloud NDB application and produce a Python 3 App Engine version that uses `google-cloud-datastore` instead of `google-cloud-ndb`.

## Why this follows Module 02

Module 02 completed the Cloud NDB migration. Module 03 continues from that working baseline and replaces the datastore client library:

- from Cloud NDB
- to Cloud Datastore client library

## Planned implementation folder

Future implementation branch:

`feat/module-03-cloud-datastore`

Future implementation folder:

`gae-flask-module-1/mod3-cloud-datastore/`

Baseline source folder:

`gae-flask-module-1/mod2-cloud-ndb/`

## Expected technical changes

### requirements.txt

Replace:

`google-cloud-ndb`

With:

`google-cloud-datastore`

Keep Flask, Werkzeug, and gunicorn aligned with the current Python 3.12 App Engine setup.

### main.py

Expected direction:

- replace `from google.cloud import ndb`
- add `from google.cloud import datastore`
- add `from datetime import datetime`
- replace NDB model class usage with Datastore entities
- replace `client.context()` usage with direct Datastore client operations
- manually set timestamp values because Datastore Entity does not provide NDB `auto_now_add`

## DevTools verification plan

Primary panels:

- Network
- Console
- Application
- Security

Expected checks:

- GET `/` returns 200
- POST `/sign` returns redirect
- redirected GET returns 200
- Console has no critical errors
- Application storage/cookies/cache reviewed
- live deployment uses HTTPS

## Safety boundary

This module uses only demo guestbook/visit data.

Forbidden:

- PHI
- real health data
- e-Nabız exports
- patient records
- medical PDFs
- OCR text
- clinical free text
- secrets
- `.env`
- direct runtime integration with sensitive health repositories

## Safe Reuse for Related Repositories

1. Allowed public-safe documentation/checklist pattern:
   - datastore-client migration checklist
   - DevTools Network verification checklist
   - Python dependency migration checklist

2. Needs manual review:
   - applying datastore migration patterns to sensitive local dashboards
   - using this as a template for PHI-free aggregate consumers

3. Forbidden sensitive-data coupling:
   - patient-level entities
   - raw health data
   - e-Nabız payloads
   - direct shared datastore/runtime integration

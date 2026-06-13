# Module 03 — Cloud NDB to Cloud Datastore Migration

## Purpose

This module follows the official Google Serverless Migration Station Module 03 path: migrating from Cloud NDB to the Cloud Datastore client library.

The module starts from the completed Module 02 Cloud NDB application and creates a new Python 3.12 App Engine version using `google-cloud-datastore`.

## Source Module

Source folder:

`gae-flask-module-1/mod2-cloud-ndb/`

Target folder:

`gae-flask-module-1/mod3-cloud-datastore/`

## What Changed

### requirements.txt

Replaced:

`google-cloud-ndb`

With:

`google-cloud-datastore`

### main.py

Replaced Cloud NDB model usage with Cloud Datastore client usage.

Before:

- `from google.cloud import ndb`
- `ndb.Client()`
- `ndb.Model`
- `ndb.StringProperty`
- `ndb.DateTimeProperty(auto_now_add=True)`
- `client.context()`
- `greeting.put()`

After:

- `from google.cloud import datastore`
- `datastore.Client()`
- `datastore.Entity`
- `client.query(...)`
- `client.put(entity)`
- explicit timestamp with `datetime.now(timezone.utc)`

## Local Test Evidence

Environment:

- Python 3.12.3
- Flask 3.1.3
- Werkzeug 3.1.8
- gunicorn 26.0.0
- google-cloud-datastore 2.25.0

Local server:

`python main.py`

Observed local requests:

- `GET /` → 200
- `POST /sign` → 302
- redirected `GET /?guestbook_name=` → 200
- `/favicon.ico` → 404, expected and non-blocking

## DevTools Verification Plan

Primary panels:

- Network
- Console
- Application
- Security

Expected browser evidence:

- Network: `GET /` returns 200
- Network: `POST /sign` returns 302
- Network: redirected `GET /?guestbook_name=` returns 200
- Console: no critical runtime errors
- Application: storage, cookies, and cache reviewed
- Security: HTTPS check after deployment

## Safety Boundary

This module uses only synthetic demo guestbook data.

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
   - dependency migration checklist
   - DevTools Network verification checklist

2. Needs manual review:
   - adapting this migration pattern to sensitive local dashboards
   - applying this to PHI-free aggregate consumer systems

3. Forbidden sensitive-data coupling:
   - patient-level entities
   - raw health data
   - e-Nabız payloads
   - shared datastore/runtime integration with sensitive repos

## Portfolio Output

Built a Python 3.12 App Engine module that migrates a working guestbook sample from Cloud NDB to the Cloud Datastore client library, then verified local request behavior through Flask logs and prepared Chrome DevTools Network, Console, Application, and Security evidence steps.

## CV Sentence

Migrated an App Engine Python 3 guestbook module from Cloud NDB to the Cloud Datastore client library, replacing NDB models with Datastore entities and validating GET/POST request behavior for DevTools-based verification.

## Deployment Evidence

Deployment mode:

`gcloud app deploy app.yaml --no-promote`

Deployed version URL:

`https://20260613t225129-dot-trustable-ai-100mph.ew.r.appspot.com`

Deployment result:

- Service: default
- Project: trustable-ai-100mph
- Version: 20260613t225129
- Traffic promotion: no
- Main production URL was not changed automatically

Expected live verification:

- `GET /` → 200
- `POST /sign` → 302
- redirected `GET /?guestbook_name=` → 200
- Chrome DevTools Console: no critical runtime errors
- Chrome DevTools Application: storage/cookies/cache reviewed
- Chrome DevTools Security: HTTPS verified

## Module 03 Completion Status

Module 03 is complete for the portfolio learning track:

- Code migration completed
- Local Flask verification completed
- GitHub PR merged
- App Engine no-promote deployment completed
- DevTools live verification prepared

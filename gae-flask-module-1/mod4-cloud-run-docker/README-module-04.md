# Module 04 — App Engine to Cloud Run with Docker

## Purpose

This module continues the Google Serverless Migration Station path by containerizing the completed Module 03 Python 3 Cloud Datastore Flask app and deploying it to Cloud Run with Docker.

## Source Module

Source:

`gae-flask-module-1/mod3-cloud-datastore/`

Target:

`gae-flask-module-1/mod4-cloud-run-docker/`

## What Changed

- Removed App Engine-specific runtime configuration from the Module 4 working copy.
- Added `Dockerfile`.
- Added `.dockerignore`.
- Updated `main.py` to bind to `0.0.0.0`.
- Updated `main.py` to use the `PORT` environment variable.
- Kept the Cloud Datastore client library from Module 03.
- Deployed the containerized app to Cloud Run.

## Container Files

Primary files:

- `Dockerfile`
- `.dockerignore`
- `main.py`
- `requirements.txt`
- `templates/index.html`

## Dockerfile Summary

The Dockerfile:

- uses `python:3.12-slim`
- sets `/app` as the working directory
- installs dependencies from `requirements.txt`
- copies the app source into the image
- starts the app with `python main.py`

## Cloud Run Compatibility

The app listens on:

- host: `0.0.0.0`
- port: `int(os.environ.get("PORT", 8080))`

This makes the app compatible with Cloud Run's runtime port contract.

## Deployment Evidence

Cloud Run service:

`mod4-cloud-run-docker`

Region:

`europe-west1`

Service URL:

`https://mod4-cloud-run-docker-208876353592.europe-west1.run.app`

Deployment command:

`gcloud run deploy mod4-cloud-run-docker --source . --region europe-west1 --allow-unauthenticated --min-instances 0 --max-instances 1`

Deployment result:

- Artifact Registry source deploy repository created: `cloud-run-source-deploy`
- Container built from local Dockerfile
- Revision deployed: `mod4-cloud-run-docker-00001-j27`
- Traffic: 100 percent to deployed Cloud Run revision
- Min instances: 0
- Max instances: 1

## Live Verification

Terminal verification:

- `GET /` → HTTP 200
- `POST /sign` → HTTP 302
- Redirect location: `/?guestbook_name=mod4`

Chrome DevTools verification plan:

- Network: verify `GET /`, `POST /sign`, and redirect waterfall
- Console: verify no critical browser runtime errors
- Application: review storage, cookies, and cache
- Security: verify HTTPS

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

## Portfolio Output

Containerized a Python 3.12 Flask + Cloud Datastore demo application with Docker, deployed it to Cloud Run with low-cost settings, and verified live GET/POST behavior for DevTools-based validation.

## CV Sentence

Containerized and deployed a Python 3.12 Flask + Cloud Datastore application to Cloud Run using Docker, validating live GET/POST behavior and documenting DevTools verification evidence.

## Module 04 Completion Status

Module 04 is complete for the portfolio learning track:

- Module 03 Cloud Datastore app used as source
- App Engine config removed from Module 04 working copy
- Dockerfile added
- `.dockerignore` added
- Cloud Run PORT binding added
- Cloud Run deployment completed
- Live HTTP GET/POST checks completed

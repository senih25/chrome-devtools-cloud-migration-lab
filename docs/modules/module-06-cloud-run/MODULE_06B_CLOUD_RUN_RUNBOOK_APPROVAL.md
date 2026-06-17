# Module 06-B — Cloud Run Deployment Runbook and Approval Checklist

## Purpose

This document outlines the **Cloud Run Deployment Runbook and Approval Checklist** for the modernized Python 3 / Flask application. 

It defines the exact command sequences, security parameters, verification commands, rollback procedures, and "stop conditions" that must be followed by a developer or AI agent before, during, and after any deployment.

---

## 1. Gated Approval Checklist

This checklist must be completely verified and signed off by the developer before executing any command in the deployment sequence.

### Pre-Deployment Checks
- [ ] **Code Hygiene**: Checked and confirmed that no `.env` files, credentials, service account JSON files, or patient-level logs exist in the repository.
- [ ] **Secret Manager Prep**: Target secrets (if any) are configured in GCP Secret Manager, not hardcoded in source.
- [ ] **Billing Alert Active**: Budget alerts are set in the Google Cloud Console to trigger warnings if forecast billing exceeds $5.00.
- [ ] **Custom IAM Account Ready**: A custom service account with minimal IAM roles (e.g. `roles/run.viewer`, `roles/logging.logWriter`) is created.

---

## 2. Deployment Runbook (Command Scaffolding)

The following commands are defined for staging and deploying the application. They are designed to prevent credential exposure and restrict resource consumption.

### Step 1: Cloud Build compilation (Dockerfile-free)
We use Google Cloud Build to build and push the container to Artifact Registry using Buildpacks:
```bash
gcloud builds submit --pack image=gcr.io/PROJECT_ID/flask-app-buildpack --project=PROJECT_ID
```
*Note: Replace `PROJECT_ID` with the actual project ID only inside the local execution environment; never commit the real project ID to public files.*

### Step 2: Deployment with Cost Caps and Authentication
Deploy the built image to Cloud Run using the strictest cost-limiting parameters:
```bash
gcloud run deploy flask-migration-service \
  --image gcr.io/PROJECT_ID/flask-app-buildpack \
  --platform managed \
  --region europe-west1 \
  --max-instances 1 \
  --min-instances 0 \
  --cpu-throttling \
  --memory 512MiB \
  --cpu 1 \
  --no-allow-unauthenticated \
  --service-account=run-migration-sa@PROJECT_ID.iam.gserviceaccount.com \
  --project=PROJECT_ID
```

### Safety Flags Explained:
* `--max-instances 1`: Caps active instances at 1 to prevent bill spikes from horizontal scaling.
* `--min-instances 0`: Instructs the service to scale to zero when idle, keeping costs at $0.00.
* `--no-allow-unauthenticated`: Restricts access to authorized IAM users only, preventing public-facing URL scraping and unauthorized network traffic.

---

## 3. Post-Deployment Verification Plan

Once the deploy command completes, execute the following verifications:

### 1. Endpoint Access (IAM Authed)
Since the service is private, access it using an authorized identity token:
```bash
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  https://flask-migration-service-xxxx-ew.a.run.app
```
*Verify: Response should return `200 OK` with the main page HTML.*

### 2. Chrome DevTools Audit
Inspect the auth-interceptor connection using Chrome DevTools:
* **Network Panel**: Confirm response status is `200` and all static assets load. Verify that the server returns CSP and transport security headers.
* **Performance Panel**: Record a timeline of the initial load from a scale-to-zero state to measure the exact **cold start latency**.

---

## 4. Rollback Plan and Stop Conditions

If any of the following **Stop Conditions** are met during verification or operation, the deployment must be immediately terminated and rolled back.

### Stop Conditions (Immediate Rollback Triggers)
1. **Billing Trigger**: If GCP Billing console registers any unexpected cost exceeding $1.00.
2. **Security Leak**: If any credentials, project IDs, developer emails, or unexpected debug logs appear in the response headers, console, or Cloud Logging.
3. **Crash Loop / Resource Exhaustion**: If the container enters a crash loop (`ERR_CONNECTION_REFUSED`) or memory usage spikes near the 512MiB limit.

### Rollback / Deletion Command
To immediately delete the deployed service and eliminate all potential billing and exposure:
```bash
gcloud run services delete flask-migration-service --region=europe-west1 --project=PROJECT_ID --quiet
```
Confirm service deletion:
```bash
gcloud run services list --region=europe-west1 --project=PROJECT_ID
# (Verify list is empty or service is removed)
```

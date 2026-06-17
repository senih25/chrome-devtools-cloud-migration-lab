# Module 06-A — Cloud Run Deployment Readiness Plan

## Purpose

This document outlines the **Cloud Run Deployment Readiness Plan** for the modernized Python 3 / Flask web application (originally migrated from GAE Python 2 in Modules 01-05). 

Because deploying to a live public cloud environment introduces cost, data privacy, and security exposures, this plan serves as a **manual review gate**. It details the cost-aware parameters, security configurations, and Chrome DevTools verification checks that must be met before any live cloud deployment is initiated.

---

## 1. Context and Goals

In previous modules:
- **Module 04**: We verified containerization of the Flask app using a custom `Dockerfile`.
- **Module 05**: We verified containerization using Dockerfile-free Cloud Buildpacks and a `Procfile`.
- **Module 10**: We implemented strict local security headers (CSP, HSTS, X-Frame-Options).

The objective of Module 06 is to define the exact deployment readiness criteria required to migrate this containerized application to **Google Cloud Run** securely, with zero budget exposure and maximum defense-in-depth security.

---

## 2. Cloud Cost Control Guardrails

To prevent run-away billing spikes due to infinite loops, DDoS attempts, or misconfigured traffic, the Cloud Run service must be deployed with strict resource limits:

| Config Parameter | Target Safe Setting | Purpose |
|---|---|---|
| **Max Instances** (`--max-instances`) | `1` or `2` | Strictly caps container scaling to prevent horizontal scaling bill spikes. |
| **Min Instances** (`--min-instances`) | `0` | Allows the service to scale down to zero when idle, resulting in $0.00 idle cost. |
| **CPU Allocation** | `Only allocated during request processing` | Disables idle CPU billing, ensuring we only pay for active processing. |
| **Resource Limits** | `512MiB` Memory / `1` vCPU | Keeps container memory and CPU sizing at minimal levels suitable for a demo. |
| **Concurrency** | `80` (Default) | Allows multiple concurrent requests per container to maximize resource efficiency. |

---

## 3. Deployment Security & IAM Architecture

To ensure the public endpoint does not leak credentials or expose backend resources:

1. **GCP Secret Manager Integration**:
   - Under no circumstances should `.env` files, API keys, or JSON credentials be baked into the Docker image or passed as raw environment variables.
   - All sensitive keys must be stored in **GCP Secret Manager** and mounted as environment variables at container startup using Cloud Run's native Secret Manager integration.

2. **Least-Privilege Service Account**:
   - The service must not run under the default Compute Engine service account.
   - A custom IAM service account with minimal access (e.g. only permission to read designated secrets and write to Cloud Logging) must be created and bound to the Cloud Run service.

3. **Public Endpoint Caution**:
   - As defined in [docs/GUARDRAILS.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/GUARDRAILS.md), all public deployment URLs must be intentionally omitted or generalized in public release notes to prevent unauthorized access.

---

## 4. Gated Deployment Checklist

Before any `gcloud run deploy` command is run, the following gates must be marked as passed by a human developer:

### Gate 1: Local Sanity Audits
- [ ] Code compiles without errors (`python -m py_compile`).
- [ ] Container builds successfully locally using either the Dockerfile or Buildpacks configuration.
- [ ] Local container runs on port `8080` and passes manual loopback checks.

### Gate 2: GCP Billing & Cost Check
- [ ] GCP Billing Account has active budget alerts (notifying at $5.00 / $10.00 thresholds).
- [ ] Resource quotas are active and capped.

### Gate 3: Secrets & Privacy Scan
- [ ] All credentials stripped from code.
- [ ] Custom service account created.
- [ ] Secret Manager API enabled in target project.

---

## 5. Post-Deployment DevTools Audit Plan

Once deployed, the live service endpoint must be audited using Chrome DevTools to document the following evidence:

1. **Performance Panel (Cold Start Verification)**:
   - Perform a performance recording of the initial page load after scaling to zero.
   - Document the cold start latency duration.
2. **Security & Network Panel (Header Auditing)**:
   - Verify that the injected security headers (`Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`) are correctly parsed by the browser.
3. **Application Panel (Cookie/Storage Auditing)**:
   - Verify that no credentials or sensitive tokens are stored in the live browser storage context.

---

## 6. Safety Confirmation & Next Step

* **Safety Status**: This document is docs-only. No live services have been started, and no commands that modify GCP resources have been run.
* **Next Step**: Proceed to `Module 06-B` to document the **GCP Cloud Run Deploy Command Scaffolding** (`MODULE_06B_DEPLOY_COMMAND_SOP.md`) without executing the commands.

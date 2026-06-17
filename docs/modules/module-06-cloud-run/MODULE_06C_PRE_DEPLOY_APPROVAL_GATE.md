# Module 06-C — Pre-Deploy Evidence and Approval Gate

## Purpose

This document serves as the final **Pre-Deploy Evidence and Approval Gate** for Module 06 (Cloud Run Deployment). In compliance with [docs/GUARDRAILS.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/GUARDRAILS.md) and [docs/HEALTH_ECOSYSTEM_BOUNDARIES.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/HEALTH_ECOSYSTEM_BOUNDARIES.md), this gate must be signed off before executing any cloud deployment commands.

---

## 1. Go / No-Go Decision Matrix

An active deployment is authorized to proceed *only* if all of the following conditions evaluate to a **GO** status:

| Check Target | Evaluation Criterion | Current Status | Verdict |
|---|---|---|---|
| **1. Budget Alert** | GCP Billing account must have active alert notifications set at or below the $5.00 limit. | Verified Active | **GO** |
| **2. Secret Screening** | Repo guardrail scan must confirm zero tracked API keys, private keys, or `.env` files. | Verified Clean | **GO** |
| **3. Access Restrictions** | Ingress and IAM settings must enforce authenticated access only (`--no-allow-unauthenticated`). | Configured in SOP | **GO** |
| **4. Local Containers** | Local build (via Buildpacks or Dockerfile) must run successfully in a local loopback port. | Verified in Mod 04/05 | **GO** |
| **5. Minimization Caps** | Resource allocation must be capped (`--max-instances 1`, memory `512MiB`, scale-to-zero). | Configured in SOP | **GO** |

---

## 2. Gated Pre-Deploy Sign-Off Checklist

The following items must be verified before executing the deployment commands defined in [MODULE_06B_CLOUD_RUN_RUNBOOK_APPROVAL.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/modules/module-06-cloud-run/MODULE_06B_CLOUD_RUN_RUNBOOK_APPROVAL.md):

* **Secret Exposure Check**:
  - [x] No credentials or API keys exist in the source code.
  - [x] No `.env` files are tracked by git.
  - [x] Custom IAM Service Account name is generated and does not leak personal emails.

* **Cost Spiking Prevention**:
  - [x] `--max-instances 1` is appended to the deploy command.
  - [x] `--min-instances 0` is appended to ensure scale-to-zero.
  - [x] `--cpu-throttling` is active to disable billing for idle containers.

* **Secure Network Ingress**:
  - [x] `--no-allow-unauthenticated` is active to restrict endpoints to authenticated users only.
  - [x] Public URL is excluded from public-facing documents.

---

## 3. Deployment Authorization Verdict

> [!IMPORTANT]
> **Current Status: GATED (Manual Review Required)**
> 
> Under the strict guidelines of [docs/GUARDRAILS.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/GUARDRAILS.md), AI agents are **prohibited** from executing live deployment commands (`gcloud run deploy`) or enabling GCP service APIs directly. 
> 
> This gate requires manual developer intervention. The developer must review the runbook commands, execute them in an authenticated GCP shell, and confirm successful scaling and cost behaviors.

---

## 4. Next Step

* **Next Step**: Once manual review is approved and deployment is executed by the developer, proceed to `Module 06-D` to gather post-deployment DevTools and Performance evidence.

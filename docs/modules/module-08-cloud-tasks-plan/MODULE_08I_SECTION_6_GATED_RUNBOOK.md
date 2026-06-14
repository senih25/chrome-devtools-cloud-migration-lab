# Module 08-I - Section 6 Gated Execution Runbook

## Purpose

This document defines the gated execution runbook for Module 08 before any future move into codelab section 6 deployment and verification work.

It documents the required sequence, safety controls, and approval gates for future cloud-side execution without performing any of those actions now.

## Current Position

Current status:

```text
Module 08 codelab section 5 is complete on the repository side.
Section 6 deploy / verification has not started yet.
```

The current repository baseline already includes implementation, readiness documentation, local DevTools evidence guidance, deploy-readiness review, and portfolio-ready release notes.

## Non-Execution Statement

This document is a section 6 execution plan, not execution.

The following actions have not been performed:

```text
Cloud Tasks API enablement was not performed
Queue creation was not performed
Deploy was not performed
IAM changes were not performed
Public endpoint sharing was not performed
```

## Required Explicit Approvals

The following approvals are required before any future section 6 execution:

```text
deploy approval
Cloud Tasks API enablement approval
queue creation approval
IAM review approval
Cloud Logging review approval
rollback approval
cost boundary approval
public endpoint approval
```

## Pre-Execution Local Checks

Before any future execution phase, complete the following local checks:

```text
git status -sb
git branch --show-current
git log --oneline -5
python -m pytest -q
python main_test.py
```

Expected result:

```text
clean working tree
expected branch confirmed
expected HEAD confirmed
tests passing
no blocked paths
no secret or PHI risk
```

## Pre-Execution Repository Safety Checks

Before cloud-side execution, confirm that repository state remains public-safe.

Blocked paths:

```text
.env
.venv
__pycache__
.pytest_cache
package-lock.json
python-docs-samples
.git
```

Sensitive content that must not appear:

```text
secrets
tokens
API keys
PHI
TCKN
real patient data
e-Nabiz export data
raw sensitive payloads
```

## Gated Step 1 - Confirm Cloud Project and Account

Goal:

```text
Confirm which project and authenticated account would be used in a future approved run.
```

Example commands:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud config get-value account
gcloud config get-value project
gcloud config list
```

Expected review point:

```text
account known
project known
project approval confirmed
```

## Gated Step 2 - Review Cloud Tasks API State

Goal:

```text
Check whether Cloud Tasks API is already enabled before any enablement decision.
```

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud services list --enabled | findstr cloudtasks.googleapis.com
```

Expected review point:

```text
API state known
no implicit enablement
```

## Gated Step 3 - Cloud Tasks API Enablement Gate

This step requires explicit approval before any execution.

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud services enable cloudtasks.googleapis.com
```

Gate condition:

```text
Run only if API enablement approval is explicitly granted.
```

## Gated Step 4 - Queue Creation Gate

This step requires explicit approval before any queue creation or modification.

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud tasks queues create TRIM_QUEUE_NAME --location=REGION
```

Gate condition:

```text
Run only if queue creation approval is explicitly granted.
```

## Gated Step 5 - IAM Review Gate

This step requires explicit approval before any service account or permission change.

Example review area:

```text
service account identity
least-privilege requirement
Cloud Tasks invocation permission
App Engine runtime identity behavior
```

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud projects get-iam-policy PROJECT_ID
```

Gate condition:

```text
Run only if IAM review approval is explicitly granted.
```

## Gated Step 6 - Deploy Gate

This step requires explicit approval before any deploy action.

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud app deploy
```

Gate condition:

```text
Run only if deploy approval is explicitly granted.
```

## Gated Step 7 - Browser DevTools Verification Plan

Chrome DevTools can verify only browser-originated requests:

```text
GET /
POST /sign
POST /trim if manually triggered
```

Important boundary:

```text
Cloud Tasks server-side dispatch does not appear in Chrome DevTools Network.
Server-side dispatch evidence requires Cloud Logging or Cloud Console after an explicitly approved gated deploy phase.
```

Expected browser verification areas:

```text
Network
Console
Application
Security
```

## Gated Step 8 - Cloud Logging Verification Plan

Cloud Logging evidence would be collected only after explicit approval in a future cloud-side phase.

Example command:

```text
DO NOT RUN unless explicit approval is granted for this exact action.
gcloud logging read "resource.type=gae_app"
```

Evidence categories to review:

```text
task creation attempt
task creation success/failure
handler invocation
handler status code
retry behavior
queue not found errors
permission denied errors
unexpected exceptions
```

Logs must not include:

```text
secrets
tokens
API keys
PHI
TCKN
real patient data
e-Nabiz export data
raw sensitive payloads
```

## Gated Step 9 - Rollback / Stop Criteria

Before any future section 6 execution, rollback and stop criteria must already be documented.

Minimum rollback coverage:

```text
known previous commit
known previous deploy state if applicable
how to stop execution
how to stop queue dispatch if applicable
how to inspect failure state
who approves rollback
```

Stop immediately if:

```text
unexpected public exposure occurs
sensitive data appears in logs
permission behavior is unclear
queue state is not understood
tests fail
```

## Evidence To Capture

Future approved execution should capture:

```text
local test result
branch and HEAD confirmation
DevTools Network evidence for browser requests
DevTools Console evidence
DevTools Application evidence
Security panel evidence if HTTPS endpoint exists
Cloud Logging evidence for server-side behavior
rollback decision notes
```

## No-Go Conditions

Do not proceed to section 6 if any of the following is true:

```text
working tree dirty
branch not expected
tests failing
blocked path present
secret / PHI scan risky
explicit deploy approval missing
API enablement approval missing
queue creation approval missing
IAM approval missing
rollback plan missing
cost boundary not accepted
```

## Portfolio Note

This runbook shows that section 6 can be planned professionally without prematurely executing cloud-side actions.

Key portfolio takeaway:

```text
The migration work separates browser-visible verification from backend-to-backend execution evidence, and requires explicit approval gates before API enablement, queue creation, IAM review, deployment, and logging inspection.
```

## Next Safe Step

Safe next step:

```text
Review and merge this docs-only runbook, then decide whether Module 08 should stop at the portfolio-ready gate or move into a separately approved cloud-side execution phase.
```

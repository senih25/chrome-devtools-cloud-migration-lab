# Module 06 — Pre-Deploy Readiness Decision

## Purpose

This document records the evidence-based readiness decision for Module 06.

It does not authorize deployment, API enablement, IAM mutation, billing
changes, container builds, Artifact Registry use, or Cloud Build use.

## Decision Rules

- **PASS:** Verified evidence exists and the requirement is satisfied.
- **FAIL:** The requirement is not satisfied or conflicts with a safety boundary.
- **NOT ENOUGH DATA:** Available evidence is insufficient for a reliable decision.
- **BLOCKED:** A critical FAIL or NOT ENOUGH DATA prevents progression.

## Readiness Table

| Area | Check | Status | Current Evidence | Required Action |
|---|---|---|---|---|
| Project Identity | Target project confirmed | NOT ENOUGH DATA | No verified target project recorded in this decision | Confirm project name and project ID |
| Project Identity | Demo and production boundaries separated | NOT ENOUGH DATA | Environment boundary not yet recorded | Document intended environment |
| Billing | Billing state verified | NOT ENOUGH DATA | No current read-only billing evidence attached | Perform read-only verification |
| Billing | Approved cost ceiling documented | FAIL | No explicit approved ceiling recorded | Define maximum permitted spend |
| Cloud Run API | Current API state known | NOT ENOUGH DATA | API state not yet verified | Perform read-only API state check |
| Cloud Run API | Enablement separately approved | PASS | Existing approval boundary requires explicit approval | Preserve approval gate |
| IAM | Intended runtime identity documented | NOT ENOUGH DATA | Service account decision not recorded | Document intended identity |
| IAM | Least-privilege role proposal exists | NOT ENOUGH DATA | Role proposal not yet recorded | Prepare non-mutating role matrix |
| Cost | Minimum instances policy defined | PASS | Planning boundary requires scale-to-zero | Preserve minimum instances at zero |
| Cost | Maximum instances cap defined | NOT ENOUGH DATA | Maximum cap not approved | Define safe maximum |
| Cost | Region selected and justified | NOT ENOUGH DATA | No approved region decision recorded | Compare suitable regions |
| Deployment Gate | Explicit approval required | PASS | Approval matrix requires a separate approval | Preserve gate |
| Deployment Gate | Deploy commands excluded | PASS | Current Module 06 planning scope excludes deploy commands | No action |
| Evidence | Local and live evidence separated | PASS | Evidence planning separates readiness from live execution | Preserve boundary |
| Safety | No secrets or credentials introduced | PASS | Repository guardrails passed | No action |
| Safety | No live mutation authorized | PASS | Management record limits current scope to planning/docs | No action |

## Stop Conditions

Progression must stop when any of the following remains true:

- target project identity is uncertain;
- billing state is unknown or blocked;
- approved cost ceiling is missing;
- Cloud Run API state is unknown;
- IAM identity or least-privilege scope is unclear;
- deployment approval is missing;
- a live mutation command appears in readiness-only work.

## Current Decision

**BLOCKED — PLANNING ONLY**

Current blockers:

1. Target project and environment boundary require confirmation.
2. Billing state has not been verified with current read-only evidence.
3. An explicit cost ceiling has not been approved.
4. Cloud Run API state is not yet documented.
5. Runtime identity and least-privilege roles are not yet documented.
6. Region and maximum scaling cap are not yet approved.

## Authorization Boundary

The following actions remain unauthorized:

- Cloud Run deployment
- Google Cloud API enablement
- IAM mutation
- billing account changes
- Artifact Registry creation or upload
- Cloud Build execution
- public ingress changes
- service account key creation
- any cost-bearing cloud operation

A separate explicit approval is required before any live cloud mutation.

# Module 03 — Implementation Plan

Status: Future PR only. This planning PR ships zero code and zero cloud changes.

## Proposed module scope

- Migrate the lab sample app asynchronous trim job from Task Queue push tasks to Cloud Tasks.
- Use one queue and one handler: POST /trim.
- Use synthetic timestamp payloads only.
- Produce DevTools Network evidence for browser-visible requests.
- Produce Cloud Logging evidence for server-side queue dispatch.
- Document Task Queue API call versus Cloud Tasks API call.

## Non-goals

- Pull queues and Pub/Sub migration.
- HTTP-target tasks to non-App-Engine endpoints.
- Cloud Scheduler.
- Multi-queue, multi-region, or load testing.
- Real data processing.

## Future branch strategy

| Branch | Purpose |
|---|---|
| docs/module-03-cloud-tasks-plan | This planning PR |
| feat/module-03-cloud-tasks-baseline | Optional Task Queue baseline |
| feat/module-03-cloud-tasks-migration | Actual Cloud Tasks migration |
| docs/module-03-evidence | Sanitized evidence and screenshots |

## Candidate future module layout

- gae-flask-module-3/mod7-gaetasks-baseline/
- gae-flask-module-3/mod8-cloudtasks/
- docs/modules/module-03-cloud-tasks/evidence/

## Local/dev verification plan

Cloud Tasks has no local emulator, so local verification is split:

1. Run Flask locally with a stubbed Cloud Tasks client.
2. Unit-test task construction without calling the API.
3. Test POST /trim locally with synthetic JSON.
4. Capture DevTools Network evidence for local GET / and local POST /trim.
5. Deployed Cloud verification only after decision gates pass.

## Deployment decision gates

- G1: This planning PR reviewed and merged.
- G2: Open questions resolved and recorded.
- G3: Cost/risk safe defaults applied.
- G4: Explicit human approval to enable cloudtasks.googleapis.com.
- G5: Target project confirmed demo-only and not coupled to sensitive health repos.
- G6: Repo guardrail workflow green on implementation branch.

## Rollback plan

- Revert implementation PR if needed.
- Pause Cloud Tasks queue as kill switch.
- Purge/delete queue only after review.
- Route App Engine traffic back to prior version.
- Disable app after verification.

## Cost-control steps

1. No API enablement until G4.
2. Budget alert before deploy.
3. Queue retry caps.
4. F1 instance class, no min instances.
5. Disable app between verification sessions.
6. Cleanup staging buckets after verification.

## Future implementation PR checklist

- No secrets.
- No PHI.
- No e-Nabız data.
- Synthetic timestamp payloads only.
- Unit tests for task construction and /trim handler.
- DevTools evidence captured and sanitized.
- MODULE_INDEX updated to Done only after evidence lands.

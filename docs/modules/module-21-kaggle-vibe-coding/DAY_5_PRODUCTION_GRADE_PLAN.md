# Day 5: Spec-Driven Production Grade Development

## Source Assignment

Kaggle Unit 5 focuses on "Spec-Driven Production Grade Development in the Age of Vibe Coding."

The final assignment includes:

- summary podcast review
- whitepaper review
- optional agent deployment to Google Cloud
- optional frontend web application linked to a cloud-hosted agent

The deployment and frontend codelabs are optional and may require a billing account. In this repository, those steps remain blocked by the Module 21 Stage 3 manual review gate.

## Repo Interpretation

Day 5 is mapped as a production-readiness and specification discipline exercise, not as a live deployment task.

Allowed local/documentation scope:

- map spec-driven development concepts
- define behavior-first acceptance criteria
- document Gherkin-style scenarios as source-of-truth examples
- identify production pipeline controls
- document zero-trust deployment gates
- map automated code-review and policy-server concepts to repo guardrails

Blocked pending manual review:

- Cloud Run deployment
- public endpoint exposure
- Secret Manager provisioning
- live AI Studio API integration
- frontend connected to a live cloud-hosted agent
- billing-impacting resources

## Spec-Driven Development Mapping

Day 5 reframes vibe-coded output as disposable implementation and treats behavior specifications as the durable contract.

Repository mapping:

| Course concept | Repo-safe interpretation |
|---|---|
| Gherkin behavior specs | deterministic acceptance criteria for local agent behavior |
| code as disposable | generated code must be replaceable if tests/specs stay stable |
| production-grade pipeline | branch, PR, guardrails, test evidence, and manual review gates |
| zero-trust development | no unreviewed secrets, endpoints, IAM, or cloud resources |
| automated review agents | CI guardrails and scoped review checklists |
| policy servers | documented safety boundaries and manual approval gates |

## Example Acceptance Scenarios

```gherkin
Feature: Agent safety before production deployment

  Scenario: Unsafe prompt is blocked locally
    Given a local ADK agent workflow
    When a prompt contains PHI-like or prompt-injection text
    Then the workflow routes the request to a security handler
    And the request does not reach the normal classifier path

  Scenario: Cloud deployment remains gated
    Given the Module 21 Stage 3 gate is not approved
    When a task requests Cloud Run deployment
    Then the deployment is documented as deferred
    And no cloud resource is provisioned

  Scenario: Frontend integration remains non-live
    Given there is no approved cloud-hosted agent endpoint
    When a frontend integration is planned
    Then the design remains local or documentation-only
    And no public endpoint is referenced in public docs
```

## Production Gate Checklist

Before any future live deployment, all items must be explicitly approved:

- cost review completed
- billing impact accepted
- Cloud Run exposure reviewed
- Secret Manager usage approved
- no `.env` or committed secret files
- API key scope restricted
- IAM least-privilege account defined
- public endpoint policy approved
- rollback path documented
- DevTools Network and Console evidence plan defined

## Current Evidence Status

Completed locally:

- Day 1 course mapping and Cloud Run conceptual notes
- Day 2 MCP/tooling evidence
- Day 3 ADK customer support agent prototype
- Day 4 local security guardrails and targeted tests
- Stage 3 manual review gate

Deferred:

- live Cloud Run deploy
- cloud-hosted agent URL
- live frontend-to-agent integration
- Secret Manager setup
- AI Studio API runtime integration

## Safety Boundary Confirmation

- No PHI
- No e-Nabiz export
- No patient data
- No secrets
- No `.env`
- No cloud resource provisioning
- No public endpoint
- No billing-impacting configuration

## Day 5 Completion Decision

Day 5 is complete for this repository as a documentation-first production readiness mapping.

The optional deployment and frontend codelabs are intentionally deferred until the Module 21 Stage 3 manual review gate is approved.

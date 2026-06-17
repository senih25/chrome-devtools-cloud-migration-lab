# Module 21: Kaggle AI Agents Vibe Coding

This module maps the Kaggle "5-Day AI Agents: Intensive Vibe Coding Course With Google" to a repository-safe, day-by-day implementation plan.

## Status

Needs manual review

This module includes Cloud Run, AI Studio, and API key handling decisions. Per repository guardrails, anything involving deployment, public endpoints, or secret management must remain gated until manual review is complete.

## Source Basis

This plan is derived from Kaggle's official course overview and discussion posts:

- Course overview
- Welcome + setup instructions
- Day 1 assignment
- Day 2 assignment
- Day 3 assignment

Days 4 and 5 are not planned yet because the source material has not been provided in this workspace.

## Course-to-Repo Mapping

| Day | Kaggle topic | Repo interpretation | Allowed scope |
|---|---|---|---|
| Day 1 | Introduction to Agents & Vibe Coding, AI Studio, Cloud Run, Antigravity 2.0 / IDE / CLI | Cloud-side architecture and deployment gate | Docs only until manual review |
| Day 2 | Agent Tools & Interoperability, Antigravity CLI, Google Developer Knowledge MCP server | Local interoperability and tool-calling mock workbench | Local mock implementation only |
| Day 3 | Agent Skills, Antigravity Skills, Agents CLI, ADK | Reusable skill structure and context management patterns | Local-first implementation only |
| Day 4 | Not yet sourced | Pending source material | Not planned |
| Day 5 | Not yet sourced | Pending source material | Not planned |

## Course Rules Observed

- Assignments do not need to be submitted.
- The course can be completed at your own pace.
- The first assignment begins with course onboarding and setup.
- The course is designed for learners building and understanding AI agents.
- Day 1 deployment uses Cloud Run Starter Tier and does not require a billing account.
- The course emphasizes live sessions, discussion forum support, and community guidance.

## Repository Strategy

### Stage 1: Docs-first
Document the course mapping before expanding implementation.

Expected outputs:
- module plan
- day-by-day evidence map
- security boundary note
- manual review gate

### Stage 2: Local Mock Workbench
Build a synthetic local demo that demonstrates the course ideas without live cloud dependencies.

Allowed:
- local server only
- mock agent planning endpoint
- mock agent execution endpoint
- console/network evidence collection
- no real API key usage
- no `.env`
- no PHI
- no real user data

### Stage 3: Manual Review Gate for Cloud
Only after docs and local validation are complete:

- Cloud Run deployment
- AI Studio integration
- Secret Manager-based key handling
- public endpoint review
- cost review
- security review

## Safety Boundaries

Explicitly excluded until manual review:

- PHI
- e-Nabız exports
- patient data
- real health records
- committed secrets
- `.env` files
- production endpoints
- unreviewed cloud billing impact

## Recommended Implementation Order

1. Finalize the day-by-day documentation plan.
2. Validate the local mock workbench for Day 2 and Day 3 concepts.
3. Keep Day 1 cloud behavior as documentation-only until manual review.
4. Wait for Day 4 and Day 5 source material before extending the plan.

## Expected Portfolio Outcome

A safe, reproducible, and repo-compliant Kaggle AI Agents module that demonstrates:

- vibe coding workflow understanding
- agent tools and interoperability concepts
- agent skills and context management
- local-first validation discipline
- cloud deployment readiness with explicit safety gates

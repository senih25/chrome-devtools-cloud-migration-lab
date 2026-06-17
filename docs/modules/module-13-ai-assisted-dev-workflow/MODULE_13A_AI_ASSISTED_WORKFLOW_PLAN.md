# Module 13-A — AI-Assisted Development Workflow Plan

## Purpose

This document outlines the planning phase for **Module 13 — AI-Assisted Development Workflow**. 

As AI agents (Gemini, Claude, Copilot, etc.) become core pair programmers in modern development workspaces, establishing a secure, disciplined, and standardized workflow is critical. This module formalizes the interaction protocols, branch/PR lifecycle, cross-environment synchronization (Windows <-> Cloud Shell), and safety boundaries required to maintain a portfolio-grade, public-safe engineering repository.

---

## 1. Scope and Objectives

The workflow plan establishes rules for AI agents operating within the `chrome-devtools-cloud-migration-lab` repository.

### Objectives
1. **Define Task Intake Protocol**: Establish how AI agents parse requirements, align on goals (using `/goal` or `/grill-me`), and verify safety boundaries before editing files.
2. **Standardize Git & PR Hygiene**: Codify the branch-and-PR workflow to prevent direct writes to `main` and enforce semantic commit patterns.
3. **Formalize Local-First Verification**: Specify standard commands (`py_compile`, linting, mock port testing) that must pass before opening a PR.
4. **Define Sync Routine**: Address the synchronization requirements between the local Windows environment, the GitHub origin repository, and the Cloud Shell workspace.
5. **Enforce PR Reporting Standards**: Mandate a pre-PR information package containing file diffs, risk assessments, test logs, and the safety checklist.

---

## 2. Core Workflow Components (To Be Codified)

During the implementation phase of this module, we will detail and codify the following standards:

### A. Task Intake & Analysis
* AI agents must read repository constraints (`docs/HEALTH_ECOSYSTEM_BOUNDARIES.md`, `docs/GUARDRAILS.md`, `AGENTS.md`) at the start of any conversation.
* The agent must verify the current git state and active port allocations before proposing changes.

### B. Git Branching & Commit Discipline
* **Naming Convention**: Use `feat/module-<num>-<description>` or `docs/module-<num>-<description>`.
* **Commits**: Group logically and commit with semantic headers (e.g. `feat(module13): ...` or `docs(module13): ...`).
* **Branch Lifespan**: Once merged on remote, local and remote feature branches must be deleted promptly to keep the tree clean.

### C. Multi-Environment Sync Routine
Because development occurs across local Windows machines and Cloud Shell, a strict sync process is enforced:
1. **Sync Before Code**: Always pull the latest `main` from origin on the active device.
2. **Local Branching**: Create the feature branch locally.
3. **Remote Push**: Push the branch to GitHub.
4. **Cloud Shell Pull**: Fetch the branch on Cloud Shell to verify cross-platform parity when required.

### D. Local-First Validation Rules
* No code can be submitted to a PR without passing:
  - Local syntax validation (e.g. `python -m py_compile`).
  - Runtime smoke test (resolving `200` status on target loopback ports like `127.0.0.1:8097`).
  - Active DevTools inspection (Network, Console, Application, and Security checks).

### E. Pre-PR Report Structure
Every PR description or final handoff must contain:
1. **Changed File List**: Explicit list of created or modified files.
2. **Risk Assessment**: Identify cost, credential leakage, or architectural regression risks.
3. **Validation Output**: Raw terminal or API test output proving validation passed.
4. **Safety Boundary Confirmation**: Statement asserting no secrets or PHI were handled.
5. **Reviewer Checklist**: The canonical list of checks required before merge.

---

## 3. Planned Deliverables for Module 13

| Step | Deliverable Document | Focus |
|---|---|---|
| **13-A (This Doc)** | `MODULE_13A_AI_ASSISTED_WORKFLOW_PLAN.md` | Initial plan, scope, and objectives of the workflow standardization. |
| **13-B SOP** | `MODULE_13B_AI_AGENT_SOP_HANDBOOK.md` | The actionable Standard Operating Procedures handbook for AI agents. |
| **13-C Logging** | `MODULE_13C_SYNC_AND_VALIDATION_LOG.md` | Verification logs demonstrating cross-environment sync and local-first checks. |
| **13-D Portfolio** | `MODULE_13D_AI_WORKFLOW_CASE_STUDY.md` | A portfolio-grade case study presenting the AI-assisted engineering methodology. |
| **13-E Closure** | `MODULE_13_MILESTONE_CLOSURE.md` | Official completion log closing the Module 13 branch. |

---

## 4. Safety and Cost Boundary

* **No Cloud Deployment**: This module deals strictly with repository governance, documentation, and local scripts. No GCP resources will be provisioned.
* **No Secrets/Credentials**: No API keys, tokens, or environment files are allowed.
* **No Patient Data / PHI**: The rules strictly prohibit importing or requesting real-world patient records.

---

## 5. Next Step

* **Next Step**: Proceed to `Module 13-B` to write the **AI Agent Standard Operating Procedures (SOP) Handbook** (`MODULE_13B_AI_AGENT_SOP_HANDBOOK.md`).

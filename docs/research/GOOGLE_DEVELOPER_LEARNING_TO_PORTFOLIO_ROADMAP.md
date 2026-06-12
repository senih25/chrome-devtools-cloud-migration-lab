# Google Developer Learning to Portfolio Roadmap

## 1. Executive Summary
This document provides a strategic blueprint for transforming Google Developer Program Learning items—specifically focusing on Google Cloud Serverless Migration and Chrome DevTools practice—into a portfolio-grade engineering lab. The `SocialRightLabs/chrome-devtools-cloud-migration-lab` repository will evolve into a comprehensive, public-safe, PHI-free demonstration of full-stack modernization and observability. This roadmap outlines 15–30 modules that marry backend cloud migrations with explicit frontend DevTools verification.

## 2. Extracted Learning / Codelab Inventory
*Note: A local saved HTML of the Learning page was not found in the workspace. The inventory below is synthesized from the official Google Cloud Serverless Migration Station pathways, standard Chrome DevTools documentation, and available training items. Source URLs are marked as "not visible in saved HTML" where applicable, and some dynamic items require live page inspection.*

| Title | Source URL | Type | Topic Area | Output | DevTools Panels | Cloud Services | Difficulty | Time | Career Value | Portfolio Value | DevTools Score | Cloud Score | Risk (Sec/Privacy) | Risk (Cost) | Priority | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| App Engine webapp2 to Flask | Not visible in saved HTML | Codelab | Cloud Migration | Flask App | Network, Console | App Engine | 3 | 1h | 8 | 8 | 7 | 9 | 1 | 1 | Now | Completed as Module 1. Baseline requirement. |
| App Engine NDB to Cloud NDB | Not visible in saved HTML | Codelab | Cloud Migration | Python 3 App | Application, Console | App Engine, Datastore | 5 | 2h | 9 | 9 | 8 | 10 | 1 | 2 | Now | Completed as Module 2. High data modeling value. |
| App Engine Task Queues to Cloud Tasks | Not visible in saved HTML | Codelab | Cloud Migration | Worker/Queue App | Network | App Engine, Cloud Tasks | 6 | 2h | 9 | 9 | 7 | 9 | 1 | 2 | Now | Essential asynchronous processing skill. |
| App Engine Blobstore to Cloud Storage | Not visible in saved HTML | Codelab | Cloud Migration | File Upload App | Network, Application | App Engine, GCS | 5 | 2h | 8 | 8 | 9 | 9 | 2 | 2 | Now | Great for DevTools network/payload analysis. |
| App Engine Memcache to Cloud Memorystore | Not visible in saved HTML | Codelab | Cloud Migration | Cached API | Network, Performance | App Engine, Redis | 6 | 3h | 8 | 9 | 8 | 9 | 1 | 5 | Next | High caching value but higher cost risk. |
| App Engine to Cloud Run | Not visible in saved HTML | Codelab | Cloud Migration | Containerized App | Console | Cloud Run, Artifact Reg | 7 | 3h | 10 | 10 | 7 | 10 | 2 | 3 | Now | The ultimate goal of the migration station. |
| Cloud Run to Cloud Functions (v2) | Not visible in saved HTML | Codelab | Cloud Migration | Event-driven App | Network | Cloud Functions | 6 | 2h | 8 | 8 | 7 | 8 | 1 | 2 | Later | Good alternative computing option. |
| Debugging JavaScript in DevTools | Not visible in saved HTML | Codelab | DevTools | Bugfix Demo | Sources, Console | None | 4 | 1h | 8 | 7 | 10 | 1 | 1 | 1 | Now | Core DevTools mastery. |
| Analyzing Network Performance | Not visible in saved HTML | Codelab | Web Perf | Optimized API | Network, Lighthouse | Cloud CDN | 5 | 2h | 9 | 9 | 10 | 6 | 1 | 2 | Now | Crucial for Full-Stack observability. |
| Web Security & Application Panel | Not visible in saved HTML | Pathway | Security | Secure App | Security, Application | Secret Manager | 7 | 3h | 10 | 10 | 10 | 8 | 3 | 2 | Now | High portfolio value for security awareness. |

## 3. Prioritized Module Roadmap
1. **Module 00 (`module-00-baseline`)**: App Engine Python 2.7 / webapp2 baseline. (Allowed public-safe documentation).
2. **Module 01 (`module-01-app-engine-flask`)**: webapp2 to Flask migration. (Allowed public-safe documentation).
3. **Module 02 (`module-02-cloud-ndb`)**: App Engine NDB to Cloud NDB. (Allowed public-safe documentation).
4. **Module 03 (`module-03-cloud-tasks`)**: Task Queues to Cloud Tasks. Verifies async behavior in DevTools Network panel.
5. **Module 04 (`module-04-cloud-storage`)**: Blobstore to Cloud Storage. Verifies multipart uploads in Network/Application panels.
6. **Module 05 (`module-05-containerization`)**: Dockerizing the App Engine Flask app. Local debugging with DevTools.
7. **Module 06 (`module-06-cloud-run`)**: Deploying to Cloud Run. Verifies cold starts in Performance panel.
8. **Module 07 (`module-07-ci-cd-actions`)**: GitHub Actions integration. DevTools verification of deployment health.
9. **Module 08 (`module-08-memorystore-redis`)**: Caching implementation. Network panel verification of cached vs uncached TTFB.
10. **Module 09 (`module-09-firestore-native`)**: Cloud NDB to Firestore Native mode. Console verification of real-time listeners.
11. **Module 10 (`module-10-cloud-functions`)**: Event-driven triggers. Network analysis of webhook endpoints.
12. **Module 11 (`module-11-identity-iap`)**: Identity-Aware Proxy. Security and Application (Cookies) panel verification.
13. **Module 12 (`module-12-cdn-loadbalancing`)**: Cloud CDN. Network panel verification of cache hits/misses.
14. **Module 13 (`module-13-lighthouse-ci`)**: Automated Web Vitals checking. Lighthouse panel reporting.
15. **Module 14 (`module-14-pwa-service-workers`)**: Offline capabilities. Application panel (Service Workers, Cache Storage) verification.
16. **Module 15 (`module-15-memory-leaks`)**: Profiling memory. Memory panel heap snapshots.
17. **Module 16 (`module-16-css-grid-flexbox`)**: Advanced layout debugging. Elements panel Badges and Layout tooling.
18. **Module 17 (`module-17-webauthn-passkeys`)**: Passwordless auth. WebAuthn DevTools tab.
19. **Module 18 (`module-18-api-gateway`)**: API management. Network panel API latency tracking.
20. **Module 19 (`module-19-serverless-vpc`)**: Secure network boundaries. Security panel TLS verification.
21. **Module 20 (`module-20-cloud-trace`)**: Distributed tracing. Cross-referencing DevTools Network with Cloud Trace.

## 4. Top 10 Immediate Modules
1. Module 00 (Baseline) - **Done**
2. Module 01 (Flask) - **Done**
3. Module 02 (Cloud NDB) - **Done**
4. Module 03 (Cloud Tasks)
5. Module 04 (Cloud Storage)
6. Module 05 (Containerization)
7. Module 06 (Cloud Run)
8. Module 07 (CI/CD Actions)
9. Module 08 (Memorystore Redis)
10. Module 09 (Firestore Native)

## 5. Avoid / Delay List
* **Cloud SQL Migration**: High base cost; unnecessary for current NDB/Datastore trajectory. (Delay)
* **Real User Data / PHI Integration**: Violates safety architecture. Direct integration with `enabiz-local-health-assistant` is strictly **Forbidden sensitive-data coupling**. (Avoid completely)
* **VPC Peering without Serverless**: Too infrastructure-heavy, dilutes the Chrome DevTools focus. (Delay)
* **Any module requiring Service Account Keys in Repo**: Major security risk. Rely exclusively on Workload Identity Federation or default compute service accounts. (Avoid completely)

## 6. DevTools Verification Matrix

| Verification Type | DevTools Panel | Required Checks |
|---|---|---|
| **API Endpoints** | Network | Check Status 200/201, TTFB, JSON payload structure, Headers (CORS, Cache-Control). |
| **Client Logic** | Console | No unexpected errors/warnings. Verify custom logging formats for debugging. |
| **State & Auth** | Application | Inspect Cookies (HttpOnly, Secure), Local Storage, Session Storage, IndexedDB. |
| **Security** | Security | Valid TLS certificates, secure origins, mixed content warnings. |
| **Performance** | Lighthouse | Generate report: Performance > 90, Accessibility > 90, Best Practices > 90. |
| **Rendering** | Elements / Perf | Check Layout Shifts (CLS), paint flashing, DOM node count. |

## 7. Repo Update Plan for Claude
Claude should be instructed to create or update the following files:
* `README.md`: Update to reflect the portfolio mission, the modules, and public-safe nature.
* `MODULE_INDEX.md`: Create a table of contents for all 20 planned modules.
* `ROADMAP.md`: Detailed timeline and learning objectives based on this document.
* `docs/DEVTOOLS_VERIFICATION_GUIDE.md`: Standard operating procedure for verifying deployments.
* `docs/GUARDRAILS.md`: Explicit definitions of PHI boundaries and synthetic data rules.
* `docs/DECISIONS.md`: Architectural decision records (ADRs) for migration choices.
* `templates/MODULE_README_TEMPLATE.md`: Standardized structure for each module's README.
* `templates/DEVTOOLS_CHECKLIST_TEMPLATE.md`: Markdown checklist for DevTools evidence.
* `.github/workflows/repo-guardrails.yml`: CI workflow to scan for `.env` files, secrets, or PHI keywords.
* `AGENTS.md`: Instructions for AI assistants (like Claude) operating in this repository.

## 8. v0.1.0 Release Scope
**Included:**
* Modules 00, 01, and 02 fully documented and verified.
* Boilerplate templates (README, Checklist).
* Guardrails and Decisions documentation.
* DevTools Verification Guide.
* Synthetic, non-sensitive demo data only.
**Evidence:**
* Screenshots of DevTools Network and Console panels for Modules 01 and 02.
* Lighthouse reports for Modules 01 and 02.
**Excluded/Private:**
* Any reference to actual project secrets.
* Connection to `enabiz-local-health-assistant` (remains abstract or completely isolated).

## 9. 7-Day Execution Plan
* **Day 1**: Inventory and roadmap (This document).
* **Day 2**: Repo bootstrap (Update README.md, MODULE_INDEX.md, ROADMAP.md).
* **Day 3**: Module template and DevTools checklist creation (`templates/`).
* **Day 4**: Evidence structure (Upload DevTools screenshots, fill out checklists for Mod 01/02).
* **Day 5**: CI guardrails (Implement `.github/workflows/repo-guardrails.yml`).
* **Day 6**: First public-ready README polish and review against `GUARDRAILS.md`.
* **Day 7**: Claude PR review and merge Release Candidate v0.1.0.

## 10. Agent Handoff Section
```markdown
# AGENT HANDOFF: Chrome DevTools Cloud Migration Lab

Hello Claude. You are acting as the primary engineering agent for the `SocialRightLabs/chrome-devtools-cloud-migration-lab` repository.

**Your Objective:**
Execute the 7-Day Execution Plan to bring the repository to v0.1.0. Focus on structuring the repo as a professional, public-safe portfolio artifact.

**What to Build (Next Steps):**
1. Update `README.md`, create `MODULE_INDEX.md` and `ROADMAP.md`.
2. Create `docs/DEVTOOLS_VERIFICATION_GUIDE.md`, `docs/GUARDRAILS.md`, `docs/DECISIONS.md`.
3. Create `templates/MODULE_README_TEMPLATE.md` and `templates/DEVTOOLS_CHECKLIST_TEMPLATE.md`.
4. Create `.github/workflows/repo-guardrails.yml` to prevent accidental commits of `.env` or PHI.
5. Create `AGENTS.md` containing these ongoing instructions.

**Safety Boundaries (STRICTLY ENFORCED):**
* **NO PHI:** You must never introduce, mock, or simulate Personal Health Information (PHI) or real user data.
* **NO SECRETS:** Ensure `.env`, service account JSONs, and API keys are strictly `.gitignore`d and never committed.
* **ISOLATION:** Do not write code that directly integrates at runtime with `enabiz-local-health-assistant` or other sensitive core health repos. Any connection must be documented as "Allowed public-safe documentation/checklist pattern" only.

**Workflow Constraints:**
* You MUST use a branch + PR workflow only.
* You MUST NOT modify `main` directly.
* Before opening a PR, review your changes against `docs/GUARDRAILS.md`.
```

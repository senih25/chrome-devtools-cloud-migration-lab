# Module Index

This file is the control panel for the Chrome DevTools Cloud Migration Lab.

Status values:

- Done
- Now
- Next
- Later
- Needs manual review
- Avoid

| # | Module slug | Status | Source type | Product outcome | DevTools panels | Cloud services | Risk | Evidence location | Portfolio output | Safe reuse for related repos |
|---|---|---|---|---|---|---|---|---|---|---|
| 00 | `mod0-baseline` | Done | Codelab baseline | Legacy App Engine baseline reviewed | Console, Network | App Engine legacy | Low | `gae-flask-module-1/mod0-baseline/` | Baseline migration context | Allowed public-safe documentation/checklist pattern |
| 01 | `mod1-flask` | Done | Codelab/module work | Flask/Python 3 migration baseline | Network, Console, Application | App Engine Standard | Low | `gae-flask-module-1/mod1-flask/` | Runtime modernization proof | Allowed public-safe documentation/checklist pattern |
| 02 | `mod2-cloud-ndb` | Done | Codelab/module work | Cloud NDB migration and Datastore index fix | Network, Console, Application | App Engine, Datastore | Low | `gae-flask-module-1/mod2-cloud-ndb/README-module-02.md` | Data-layer migration evidence | Allowed public-safe documentation/checklist pattern |
| 03 | `module-03-cloud-datastore` | Done | Official Google codelab / implementation planning | Cloud NDB to Cloud Datastore migration | Network, Console, Application, Security | App Engine, Cloud Datastore | Medium | `docs/modules/module-03-cloud-datastore/` | Datastore client migration module | Needs manual review |
| 04 | `module-04-cloud-run-docker` | Done | Official Google codelab / implemented | App Engine to Cloud Run with Docker | Network, Console, Application, Security | Cloud Run, Docker, Artifact Registry, Cloud Build | Medium | `gae-flask-module-1/mod4-cloud-run-docker/` | Containerized Cloud Run migration module | Needs manual review |
| 05 | `mod5-cloud-run-buildpacks` | Done | Codelab/module work | Cloud Run migration using Cloud Buildpacks and Procfile | Network, Console, Application, Security | Cloud Run, Buildpacks, Procfile, Gunicorn | Low | `gae-flask-module-1/mod5-cloud-run-buildpacks/README-module-05.md` | Buildpacks deployment evidence | Dockerfile-free Cloud Run migration path |
| 06 | `module-06-cloud-run` | Next | Research candidate | Cloud Run deployment evidence | Network, Performance, Security | Cloud Run | Medium | TBD | Serverless deployment proof | Needs manual review |
| 07 | `module-07-appengine-push-tasks` | Implemented / evidence pending | Official Google codelab / baseline implemented | App Engine Push Task Queues baseline before Module 08 Cloud Tasks | Network, Console, Cloud Logging | App Engine, Task Queue push queues | Medium | `gae-flask-module-1/mod7-gaetasks-baseline/README-module-07.md` + `docs/modules/module-07-appengine-push-tasks/` | Push Task Queue baseline with local tests; deploy/evidence deferred | Requires gated deploy/evidence PR |
| 08 | `module-08-cloud-tasks-plan` | Later | Official Google codelab / research planning | Cloud Tasks migration plan | Network, Console, Cloud Logging | App Engine, Cloud Tasks | Medium | `docs/modules/module-08-cloud-tasks-plan/` | Cloud Tasks migration planning package | Needs manual review |
| 09 | `module-09-pwa-service-worker` | Later | Research candidate | Offline-capable demo | Application, Network | Optional hosting | Medium | TBD | PWA evidence | Needs manual review |
| 10 | `module-10-security-panel` | Next | Research candidate | HTTPS, mixed content, cookie/security review | Security, Application, Network | Optional hosting | Medium | TBD | Security review practice | Allowed public-safe documentation/checklist pattern |
| 11 | `module-11-accessibility-audit` | Next | Research candidate | A11y checklist and fixes | Lighthouse, Elements, Accessibility | None | Low | TBD | Accessibility proof | Allowed public-safe documentation/checklist pattern |
| 12 | `module-12-devtools-sources-debugging` | Next | Research candidate | JS debugging scenario | Sources, Console | None | Low | TBD | Debugging portfolio scenario | Allowed public-safe documentation/checklist pattern |
| 13 | `module-13-ai-assisted-dev-workflow` | Next | Internal workflow | Agent-safe development workflow | N/A | GitHub, AI tools | Medium | TBD | AI-assisted engineering workflow | Needs manual review |
| 14 | `module-14-memorystore-redis` | Later | Research candidate | Cache behavior demo | Network, Performance | Memorystore | High cost | TBD | Caching pattern | Needs manual review |
| 15 | `module-15-firestore-native` | Later | Research candidate | Data model modernization option | Application, Console | Firestore | Medium | TBD | Data modernization research | Needs manual review |
| 16 | `module-16-iap-auth` | Needs manual review | Research candidate | Identity-aware access pattern | Security, Application | IAP/IAM | High | TBD | Auth/security architecture | Needs manual review |
| 17 | `module-17-serverless-vpc` | Needs manual review | Research candidate | Network boundary research | Security, Network | VPC | High | TBD | Cloud network architecture | Needs manual review |
| 18 | `module-18-cloud-cdn` | Needs manual review | Research candidate | Cache hit/miss analysis | Network, Lighthouse | Cloud CDN | High cost | TBD | Edge performance research | Needs manual review |
| 19 | `module-19-api-gateway` | Needs manual review | Research candidate | API boundary analysis | Network, Security | API Gateway | High | TBD | API governance research | Needs manual review |
| 20 | `module-20-cloud-trace` | Needs manual review | Research candidate | Trace correlation research | Network, Performance | Cloud Trace | Medium/high | TBD | Observability research | Needs manual review |
| 21 | `module-21-kaggle-vibe-coding` | Needs manual review | Kaggle AI Agents Codelab | AI Agent Web App | Network, Console | Cloud Run, AI Studio, Secret Manager | Medium | `docs/modules/module-21-kaggle-vibe-coding/` | AI Agent workflow & Cloud Run deployment | Needs manual review |

## Internal / non-codelab modules

These are repo-governance modules, not part of the official Google codelab numbering.

| ID | Module slug | Status | Product outcome | Evidence location | Portfolio output |
|----|-------------|--------|-----------------|-------------------|------------------|
| INT-01 | `internal-repo-guardrails` | Now | GitHub Actions repo guardrails for blocked paths and public-safe checks | `.github/workflows/repo-guardrails.yml` | Repo governance proof |


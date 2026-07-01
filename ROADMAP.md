# Roadmap

This roadmap converts Google Developer learning and Chrome DevTools practice into a portfolio-grade engineering lab.

The Gemini-generated roadmap in `docs/research/GOOGLE_DEVELOPER_LEARNING_TO_PORTFOLIO_ROADMAP.md` is treated as research input, not canonical truth. Items marked as research candidates require official-source and cost verification before implementation.

## Phase 0 — Completed baseline

- Module 00: App Engine Python 2.7 / webapp2 baseline
- Module 01: Flask / Python 3 App Engine migration
- Module 02: Cloud NDB migration and Datastore index fix

## Phase 1 — Repository system v0.1.0

- README, module index, roadmap
- DevTools verification guide
- security and guardrail docs
- agent rules
- module templates
- GitHub Actions guardrail workflow

## Phase 2 — Next implementation modules

### Module 03 — Cloud NDB to Cloud Datastore Migration (complete)

Official Google Codelab Module 03 is complete in this repository.

- The migration starts from `gae-flask-module-1/mod2-cloud-ndb/`.
- The completed target lives in `gae-flask-module-1/mod3-cloud-datastore/`.
- Planning and evidence notes live in `docs/modules/module-03-cloud-datastore/` and `gae-flask-module-1/mod3-cloud-datastore/README-module-03.md`.
- Cloud Tasks planning remains in Module 08 because it corresponds to the later Task Queue to Cloud Tasks codelab.

Next implementation target:

1. Cloud Run deployment evidence
2. Cloud Tasks migration candidate (Module 08 planning; later implementation)
3. Containerization path
4. Cloud Run deployment path
5. Lighthouse / Performance audit
6. Security panel workflow
7. Accessibility audit
8. Sources/Console debugging scenario
9. AI-assisted development workflow

## Phase 3 — Later modules

- Memorystore / Redis caching
- Firestore Native research
- PWA / Service Worker
- Memory profiling
- advanced layout debugging if tied to DevTools evidence

## Phase 4 — Needs manual review

These modules require cost, IAM, security, or architecture review before work:

- IAP
- Serverless VPC
- Cloud CDN / Load Balancing
- API Gateway
- Cloud Trace
- Secret Manager-touching security module
- any identity or production-like auth module
- module-21-kaggle-vibe-coding (Cloud Run deployment and AI Studio integration review)

## Avoid

- real health data integration
- service account keys committed to repo
- `.env` files
- direct runtime coupling to sensitive health repositories
- public endpoints without cost and security review
- badge or Google recognition claims that were not actually earned

## Module completion definition

A module is complete only when it has:

1. module README or notes
2. implementation or reproducible steps
3. DevTools verification notes
4. safety boundary note
5. safe reuse classification for related repositories
6. portfolio output
7. review-ready PR

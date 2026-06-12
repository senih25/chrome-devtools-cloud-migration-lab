# Health Ecosystem Boundaries

## Purpose

This document defines the health ecosystem boundaries for repositories related to Chrome DevTools Cloud Migration Lab.

Chrome DevTools Cloud Migration Lab is a public-safe, portfolio-grade engineering lab. It must not become a health data processing repository.

## One-Sentence Architecture Decision

Real health data is processed only inside `enabiz-local-health-assistant`, locally and deterministically. All other projects can connect to the health ecosystem only through PHI-free aggregate contracts or orchestration/documentation layers.

## Repository Classification

### enabiz-local-health-assistant

- Category: Core medical local system
- Data sensitivity: Highest
- Role: Producer / local health pipeline
- Touch level: Very restricted

This repository may contain real or real-like health data, JSON sources, PDFs, local database files, pipeline outputs, reports, trends, and exports.

Only safe outbound artifact:

`exports/anonymized/anonymized_enabiz_analytics.json`

The safe export must be PHI-free, aggregate, and contain no raw text, names, TCKN, phone numbers, addresses, doctor names, or patient-level identifiers.

Canonical categories:

- `TAHLILLER`
- `ISLEMLER`
- `TANILAR`
- `RECETELER`
- `EPIKRIZLER`
- `PATOLOJI`
- `GORUNTULEME_RAPORLARI`
- `RAPORLAR`

Category note:

`ILAC_RAPORLARI` is not a separate top-level category. Medication reports belong under `RAPORLAR` as a subtype.

### controlled-adk-data-analyst-agent

- Category: PHI-free aggregate analytics consumer
- Data sensitivity: Medium
- Role: Consumer
- Touch level: Controlled

This repository is not the health core. It must not touch raw health data.

It may only consume PHI-free aggregate export. It must not write back to the producer. It is not a decision engine.

### Chrome DevTools Cloud Migration Lab

- Category: Public-safe developer engineering lab
- Data sensitivity: Low by design
- Role: DevTools, Google Cloud, debugging, repo hygiene, documentation, portfolio system
- Touch level: Public-safe only

This repository must never import, copy, process, summarize, expose, or depend on raw health data.

## Safe Integration Model

Correct model:

enabiz-local-health-assistant -> produces PHI-free aggregate export
controlled-adk-data-analyst-agent -> consumes the PHI-free aggregate export
Chrome DevTools Cloud Migration Lab -> documents public-safe patterns, checklists, and guardrails

Incorrect model:

Chrome DevTools Cloud Migration Lab must not directly read raw health data, integrate with patient-level systems, process PDFs/OCR/free text, or produce medical/legal/disability conclusions.

## Cross-Repository Classification

Every cross-repository proposal must be classified as one of:

1. Allowed public-safe documentation/checklist pattern
2. Needs manual review
3. Forbidden sensitive-data coupling

## Allowed

- conceptual architecture references
- DevTools debugging checklists
- Lighthouse and Performance workflows
- Network/API inspection methods
- Application panel storage/cookie/cache verification
- Security panel verification
- GitHub repo hygiene patterns
- GitHub Actions guardrails
- README and portfolio templates
- synthetic demo design patterns
- cost-aware cloud deployment notes
- PHI-free aggregate contract documentation

## Needs Manual Review

- export schema suggestions
- orchestration patterns
- local endpoint design
- dashboard visibility ideas
- CI workflow changes mentioning sensitive repos
- connector hardening proposals
- any proposal involving integration boundaries

## Forbidden

- PHI
- real health data
- e-Nabız exports
- patient records
- raw JSON records
- medical PDFs
- OCR text
- clinical free text
- raw logs from sensitive systems
- private screenshots
- `.env` files
- API keys
- credentials
- tokens
- database dumps
- copied private implementation details
- diagnosis
- treatment advice
- legal conclusion
- disability percentage
- malpractice conclusion
- definitive eligibility verdict

## Agent Rules

Any AI agent working on this project must:

1. Treat health-oriented repositories as sensitive.
2. Never request real health data.
3. Never request e-Nabız exports.
4. Never suggest uploading PHI to external tools.
5. Never copy private implementation details from sensitive repos.
6. Never modify sensitive repos unless explicitly instructed in a separate scoped task.
7. Keep examples synthetic and demo-only.
8. Prefer documentation, checklists, guardrails, and public-safe templates.
9. Use branch + PR workflow.
10. Provide a review checklist before merge.

## Reviewer Checklist

- No PHI
- No real health data
- No e-Nabız export
- No patient-level data
- No medical PDFs
- No OCR/free clinical text
- No secrets
- No `.env`
- No `.venv`
- No `__pycache__`
- No nested repositories
- No copied private implementation details
- All examples are synthetic, demo-only, and public-safe

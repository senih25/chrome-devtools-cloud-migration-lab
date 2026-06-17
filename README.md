# Chrome DevTools Cloud Migration Lab

A professional, portfolio-grade engineering lab for turning Google Developer learning, App Engine modernization, Google Cloud migration work, and Chrome DevTools verification into reproducible modules.

This repository is not just a collection of learning notes. It is designed as a modular engineering system where every completed module produces:

- a working or reproducible implementation
- Chrome DevTools verification evidence
- GitHub-ready documentation
- safety and privacy guardrails
- portfolio/CV-ready technical outcomes
- safe reuse patterns for related repositories

## Current status

| Module | Status | Focus | DevTools evidence |
|---|---|---|---|
| Module 00 | Done | App Engine Python 2.7 / webapp2 baseline | Baseline review |
| Module 01 | Done | App Engine webapp2 / Python 2 toward Flask / Python 3 | Network, Console, Application |
| Module 02 | Done | App Engine NDB to Cloud NDB migration | Network, Console, Application, Datastore index evidence |
| Module 03 | Done | Cloud NDB to Cloud Datastore migration | Network, Console, Application, Security |
| Module 04 | Done | App Engine to Cloud Run with Docker | Network, Console, Application, Security |
| Module 05 | Done | Cloud Run migration using Cloud Buildpacks | Network, Console, Application, Security |
| Module 10 | Done | HTTPS, mixed content, cookie/security review | Security, Application, Network |
| Module 11 | Done | Accessibility checklist and fixes | Lighthouse, Elements, Accessibility |
| Module 12 | Done | JS debugging scenario (sources/debugging) | Sources, Console |
| Module 21 | Done | Kaggle AI Agent local workbench & graph | Network, Console |

## Evidence model

Every module should answer:

1. What changed?
2. Which Chrome DevTools panels verified it?
3. What cloud/runtime behavior was observed?
4. What risks were avoided?
5. What portfolio output did this produce?

Primary DevTools panels used across the lab:

- Network
- Console
- Sources
- Application
- Security
- Lighthouse
- Performance
- Memory
- Accessibility
- Service Worker / PWA

See [DevTools Verification Guide](docs/DEVTOOLS_VERIFICATION_GUIDE.md).

## Safety boundary

This is a public-safe engineering lab. It must not become a health data processing repository.

Forbidden by design:

- PHI
- real health data
- e-Nabız exports
- patient records
- raw medical PDFs
- OCR clinical text
- `.env` files
- API keys, tokens, credentials, or secrets
- direct runtime integration with sensitive health repositories

See [Health Ecosystem Boundaries](docs/HEALTH_ECOSYSTEM_BOUNDARIES.md) and [Guardrails](docs/GUARDRAILS.md).

## Repository map

- [MODULE_INDEX.md](MODULE_INDEX.md) — module control panel
- [ROADMAP.md](ROADMAP.md) — validated roadmap and research candidates
- [CONTRIBUTING.md](CONTRIBUTING.md) — branch and PR workflow
- [SECURITY.md](SECURITY.md) — security and privacy scope
- [AGENTS.md](AGENTS.md) — rules for Claude, Gemini, Codex, Copilot, and other agents
- [docs/DEVTOOLS_VERIFICATION_GUIDE.md](docs/DEVTOOLS_VERIFICATION_GUIDE.md) — evidence standard
- [docs/GUARDRAILS.md](docs/GUARDRAILS.md) — repo safety rules
- [docs/DECISIONS.md](docs/DECISIONS.md) — architecture decisions
- [docs/research/](docs/research/) — research inputs, not canonical roadmap

## Portfolio value

This lab demonstrates:

- App Engine modernization
- Python runtime migration
- Cloud NDB / Datastore migration
- Chrome DevTools verification discipline
- GitHub repo hygiene
- CI guardrail design
- AI-agent-safe workflow design
- public-safe documentation boundaries

Recruiter-readable summary:

> Designed a modular Chrome DevTools + Google Cloud migration lab with App Engine modernization modules, Cloud NDB migration evidence, DevTools verification workflows, GitHub Actions guardrails, and AI-agent-safe repository governance.

## Not public-ready yet

This repository is currently private-first. Public release requires final review for secrets, live endpoints, screenshots, cost exposure, and source attribution.

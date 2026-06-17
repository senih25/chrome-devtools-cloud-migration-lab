# Safety Boundary — Module 21: Kaggle AI Agents Vibe Coding

## Scope

This document defines the safety boundary for Module 21 across all five course days.

## Allowed

- Whitepaper summaries and concept notes (no copyrighted full-text reproduction)
- Local mock server implementations (`MOCK_MODE=true`)
- Synthetic test data only
- DevTools verification against local endpoints
- CLI command documentation (sanitized, no real project IDs)
- Agent architecture diagrams and concept maps
- SKILL.md structure analysis and local skill creation
- ADK / Agents CLI local experimentation
- MCP protocol concept documentation
- Context engineering pattern documentation

## Blocked (pending Stage 3 manual review)

- Cloud Run deployment (`gcloud run deploy`)
- AI Studio API key generation, storage, or commit
- Secret Manager integration
- Live public endpoint exposure
- Any `gcloud` command that provisions billable resources
- Production agent deployment

## Forbidden (hard block)

- PHI or real health data
- e-Nabız exports or patient records
- `.env` files
- API keys, tokens, credentials, or secrets committed to repo
- Private screenshots exposing accounts, emails, project IDs
- Direct runtime integration with sensitive health repositories
- Raw medical PDFs, OCR clinical text

## Mock Mode Contract

All local implementations in this module use `MOCK_MODE=true`:

- No real LLM API calls
- No real Cloud Run deployments
- Simulated agent responses using static/synthetic data
- Local HTTP server only (localhost)
- No external network dependencies for core functionality

## Validation

Before any commit or PR:

- [ ] `git diff --check` passes
- [ ] No `.env` files in changeset
- [ ] No API keys or tokens in changeset
- [ ] No private screenshots in changeset
- [ ] No PHI or health data in changeset
- [ ] `.github/workflows/repo-guardrails.yml` passes
- [ ] All endpoints are localhost or explicitly documented as mock

## Classification

- Allowed public-safe documentation/checklist pattern: whitepaper notes, concept maps, DevTools checklists, mock architecture docs
- Needs manual review: Cloud Run deployment, AI Studio integration, Secret Manager workflows
- Forbidden sensitive-data coupling: none applicable to this module

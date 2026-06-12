# Module 03 — Safe Reuse for Related Repositories

This lab is a public, PHI-free engineering artifact. Some patterns may be useful to private or sensitive repositories, but reuse flows one way only.

Public-safe patterns may be copied out of this repo. Nothing flows in from sensitive repos. Nothing here may couple to sensitive repos at runtime.

## Cross-repo classification rule

Every reuse idea must be classified as exactly one of:

1. Allowed public-safe documentation/checklist pattern.
2. Needs manual review.
3. Forbidden sensitive-data coupling.

## Classification table

| Reuse idea | Direction | Classification |
|---|---|---|
| Async job checklist | this repo -> related repos | 1 — Allowed |
| DevTools Network verification checklist | this repo -> related repos | 1 — Allowed |
| Retry/backoff documentation pattern | this repo -> related repos | 1 — Allowed |
| Queue safety checklist | this repo -> related repos | 1 — Allowed |
| Cost gate/manual approval template | this repo -> related repos | 1 — Allowed |
| Screenshot sanitization rules | this repo -> related repos | 1 — Allowed |
| Concrete queue names, project IDs, or region choices copied from private repo deployment | related repos -> this repo | 2 — Needs manual review |
| Task payload schemas modeled on real domain records | related repos -> this repo | 2 — Needs manual review, default deny |
| Sensitive architecture diagrams redrawn here | related repos -> this repo | 2 — Needs manual review |
| Raw health data, PHI, or e-Nabız export | any direction | 3 — Forbidden |
| Patient-level task payloads | any direction | 3 — Forbidden |
| Medical PDFs, OCR clinical text, clinical free text, lab results | any direction | 3 — Forbidden |
| Direct runtime integration with sensitive health repos | any direction | 3 — Forbidden |
| Credentials, tokens, .env, database dumps | any direction | 3 — Forbidden |

## Sensitive related repositories

- enabiz-local-health-assistant
- controlled-adk-data-analyst-agent
- enabiz-capture-tool
- foundry-ai-companion
- clinical-temporal-risk-engine
- ai-prompt-hub

For these repos: pattern export only. No submodules, shared packages, shared cloud resources, shared queues, or cross-repo CI triggers.

## Examples of safe reuse

1. Async job lifecycle checklist.
2. Network panel verification checklist.
3. Retry/backoff documentation pattern.
4. Queue safety checklist.

## Explicitly forbidden

- Raw health data.
- PHI.
- e-Nabız exports.
- Patient-level task payloads.
- Direct runtime integration with sensitive health repositories.

If reuse does not clearly land in classification 1, it is classification 2 at best and requires manual review.

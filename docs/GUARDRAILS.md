# Guardrails

## Purpose

These guardrails keep Chrome DevTools Cloud Migration Lab public-safe, portfolio-grade, and separated from sensitive health data systems.

## Data rules

Forbidden:

- PHI
- real health data
- e-Nabız exports
- patient records
- raw JSON patient records
- medical PDFs
- OCR clinical text
- clinical free text
- private screenshots
- raw sensitive logs

## Secret rules

Forbidden:

- `.env`
- API keys
- tokens
- credentials
- service account JSON
- private keys
- database dumps

## Repository hygiene

Do not track:

- `.venv/`
- `venv/`
- `env/`
- `__pycache__/`
- `*.pyc`
- nested `.git`
- `python-docs-samples/`
- accidental `package-lock.json`

## Cloud cost rules

Before using paid or always-on services, mark the module as `Needs manual review`.

Examples:

- Memorystore
- IAP
- VPC
- Cloud CDN
- API Gateway
- Cloud Trace
- Cloud SQL
- Secret Manager-touching workflows

## Public endpoint caution

Live endpoints can create cost, security, privacy, and maintenance risk. Public-facing docs should avoid full live URLs unless explicitly reviewed.

Use safer wording:

- deployed demo verified
- private endpoint evidence available in local notes
- endpoint intentionally omitted from public-facing docs

## Screenshot safety

Screenshots must not expose:

- accounts
- email addresses
- project IDs
- tokens
- private URLs
- patient data
- sensitive logs
- browser profiles with private data

## Related repository boundary

Safe reuse must be documentation/checklist/synthetic pattern unless manually reviewed.

Forbidden:

- direct runtime integration with health core repos
- raw data transfer
- patient-level processing
- clinical interpretation
- diagnosis, treatment, legal conclusion, or disability percentage

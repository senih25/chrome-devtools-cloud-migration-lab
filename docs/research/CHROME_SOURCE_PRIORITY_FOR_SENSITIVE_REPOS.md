# Chrome Source Priority For Sensitive Repos

## Purpose

This note records the next safe application order for the Chrome source library in `chrome_articles_2026-07-01.csv`.

The CSV is treated as a public-safe source library, not as an execution plan.

## Priority Order

1. UYAP Local Case Capture
2. e-Nabız Capture Tool / e-Nabız Local Health Assistant
3. Social Profile Assistant

## Why This Order

The first two targets have stricter data, permission, and execution boundaries:

- they are more sensitive from a privacy and security perspective
- they rely directly on permission minimization and content-script boundaries
- they benefit most from explicit user action and local-first capture discipline
- they produce the highest-value Chrome DevTools security and debugging evidence

Social Profile Assistant remains important, but it should follow the higher-risk sensitive repos so the Chrome patterns are validated first in the strictest environments.

## CSV Source Clusters Most Relevant To This Order

- Extensions
- Web Store
- DevTools
- Permissions
- `chrome.storage`
- service worker lifecycle
- content scripts
- `activeTab`
- optional host permissions
- runtime messaging
- Puppeteer
- Privacy/Security

## Cross-Repository Classification

Every cross-repository idea in this note is classified as:

- UYAP Local Case Capture: Needs manual review
- e-Nabız Capture Tool / e-Nabız Local Health Assistant: Needs manual review
- Social Profile Assistant: Allowed public-safe documentation/checklist pattern

## Recommended Milestone Flow

### UYAP

```text
permission audit
→ explicit user action
→ content-script trust boundary
→ storage schema
→ message protocol
→ Puppeteer E2E
→ DevTools evidence
```

### e-Nabız

```text
privacy boundary
→ permission audit
→ category contracts
→ session/local storage model
→ synthetic fixtures
→ export/import boundary
→ DevTools evidence
```

### Social Profile Assistant

```text
storage contract
→ service worker resilience
→ messaging protocol
→ side panel runtime verification
→ permission minimization
→ Puppeteer E2E
→ Web Store readiness
```

## Safety Boundary

- No real UYAP data
- No e-Nabız exports
- No PHI
- No credentials or tokens
- No direct runtime integration with sensitive repositories

## Notes

- This document is planning-only.
- It does not authorize live data access, deployment, or repository coupling.
- The CSV remains a source index; actual implementation work must stay inside the target repository and its own safety boundary.


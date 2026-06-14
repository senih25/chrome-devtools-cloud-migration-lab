# Module 11-G - Before / After Accessibility Validation

## Purpose

This document records the before/after Lighthouse and Chrome DevTools validation evidence for the Module 11 accessibility remediation workflow.

## Scope

This is a docs-only validation step.

No code.
No demo HTML changes.
No tests.
No deploy.
No API enablement.
No IAM changes.
No cloud resources.
No billing-impacting config.
No public endpoint exposure.
No secrets or .env files.

## Local-Only Boundary

```text
No deploy.
No public endpoint.
No cloud resource.
No API enablement.
No IAM change.
No billing impact.
No real user data.
No PHI.
No e-Nabiz export.
No TCKN.
No secrets.
No .env.
```

## Before Remediation Baseline

```text
Local URL: http://localhost:8088
Before Lighthouse Accessibility score: 93
Before failed audits:
- button-name
- heading-order
Before console:
- no errors
- no warnings
- no sensitive data logs
```

## After Remediation Evidence

```text
Local URL: http://localhost:8088
After Lighthouse Accessibility score: 100
Failed audits: none
Notable warnings: none
Passed audits summary: 26 binary accessibility audits passed
```

## Before / After Comparison

| Metric | Before | After | Result |
|---|---:|---:|---|
| Lighthouse Accessibility score | 93 | 100 | +7 improvement |
| Failed audits | 2 | 0 | All confirmed Lighthouse failures resolved |
| `button-name` | Failed | Passed | Fixed |
| `heading-order` | Failed | Passed | Fixed |
| Console errors | None | None | Clean |
| Console warnings | None | None | Clean |
| Sensitive logs | None | None | Clean |

## Lighthouse Result

- Before score: `93`
- After score: `100`
- Before failed audits: `button-name`, `heading-order`
- After failed audits: `none`
- Passed audits after remediation: `26` binary accessibility audits passed
- Run warnings after remediation: `none`

## Elements / Accessibility Tree Result

- Icon-only button accessible name: Add item
- Email input label: E-posta label is correctly associated with `for="email"`
- Heading order: `h1 -> h2 -> h2 -> h2 -> h3 -> h3 -> h3`
- Link text: Review the sample form accessibility issues
- Decorative image handling: `.hero-image` uses `aria-hidden="true"` and is hidden from the accessibility tree
- Custom chip focus style: `.custom-chip:focus-visible` uses a 3px outline with 3px outline offset

## Keyboard Result

- Tab order is logical.
- Focus visibility is present for the custom chip.
- Native links and buttons preserve keyboard semantics.
- No keyboard trap was observed.
- Custom chip has no separate JavaScript action in this static demo.

## Console Result

```text
Errors: none
Warnings: none
Sensitive data logs: none
```

## Confirmed Fixes

- Added accessible name to icon-only button.
- Fixed heading hierarchy.
- Added explicit label association for email input.
- Replaced vague link text with descriptive link text.
- Hid decorative image from accessibility tree.
- Added visible focus style for custom chip.

## Remaining Notes

- Validation stayed local-only against `http://localhost:8088`.
- The result confirms remediation effectiveness without changing deployment, cloud, or runtime boundaries.
- Manual keyboard review remains relevant even when Lighthouse reaches `100`.

## Portfolio Output

This validation demonstrates a complete evidence-based accessibility workflow: identify issues with Lighthouse and Chrome DevTools, plan prioritized remediation, implement safe local fixes, and verify the result with before/after accessibility evidence.

## Next Step

Next step: Module 11-H should create a portfolio summary and LinkedIn/CV-ready writeup for the accessibility audit workflow.

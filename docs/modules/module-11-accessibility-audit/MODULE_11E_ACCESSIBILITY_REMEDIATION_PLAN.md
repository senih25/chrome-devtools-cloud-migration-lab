# Module 11-E - Accessibility Remediation Plan

## Purpose

This document converts the real Lighthouse and Chrome DevTools evidence from Module 11-D into a prioritized remediation plan.

## Scope

This is a docs-only remediation planning step.

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

## Evidence Baseline

```text
Local URL: http://localhost:8088
Lighthouse Accessibility score: 93
Passed binary audits: 24 / 26
Failed audits:
- button-name
- heading-order

Console:
- no errors
- no warnings
- no sensitive data logs
```

## Confirmed Lighthouse Findings

- `button-name`
- `heading-order`

These are direct audit failures and should be treated as the first remediation targets.

## Confirmed Manual DevTools Findings

- decorative image placeholder is exposed as role="img" with weak aria-label="image"
- icon-only + button has no accessible name
- `#email` input has no explicit label association
- heading order breaks as `h1 -> h3 -> h2`
- `Click here` link text is vague
- custom chip uses `role="button"` and `tabindex="0"` but has no visible focus outline
- keyboard trap was not observed
- tab order was logical in the tested sequence

## Remediation Priority

| Priority | Issue | Severity | Reason |
|---:|---|---|---|
| 1 | Icon-only button has no accessible name | High | Direct Lighthouse failure and screen reader blocker |
| 2 | Broken heading order | High | Direct Lighthouse failure and document structure issue |
| 3 | Custom chip has no visible focus style | High | Keyboard users may lose orientation |
| 4 | Email input has no explicit label | Medium | Form usability and screen reader clarity issue |
| 5 | Vague `Click here` link text | Medium | Link purpose is unclear out of context |
| 6 | Weak image accessible name | Low | Named but not meaningful; may be decorative |

## Issue 1 - Icon-only Button Has No Accessible Name

Problem

```text
The icon-only + button does not expose a usable accessible name.
```

Evidence

```text
Lighthouse failed audit: button-name
Manual Elements / Accessibility tree inspection confirmed missing aria-label and missing title.
```

Impact

```text
Screen reader users hear an unlabeled control, which blocks reliable interaction.
```

Recommended Fix

```html
<button aria-label="Add item">+</button>
```

or use visible text:

```html
<button>Add item</button>
```

Validation Step

```text
Re-run Lighthouse Accessibility audit.
Inspect button in Elements > Accessibility tree.
Confirm accessible name is present.
```

Expected Result

```text
button-name failure is resolved.
```

## Issue 2 - Heading Order Is Broken

Problem

```text
Heading order breaks as h1 -> h3 -> h2.
```

Evidence

```text
Lighthouse failed audit: heading-order
Manual heading inspection confirmed the break.
```

Impact

```text
Document structure becomes less predictable for assistive technology and keyboard navigation.
```

Recommended Fix

```text
Use logical heading sequence:
h1 -> h2 -> h3
```

Validation Step

```text
Re-run Lighthouse.
Inspect heading hierarchy in Elements.
Confirm heading-order audit passes.
```

Expected Result

```text
Heading structure becomes logical and Lighthouse no longer flags heading-order.
```

## Issue 3 - Email Input Has No Explicit Label

Problem

```text
The email input has no explicit label association.
```

Evidence

```text
Manual DevTools finding:
#email input has no explicit label association.
```

Impact

```text
Form usability and screen reader clarity are reduced.
```

Recommended Fix

```html
<label for="email">Email</label>
<input id="email" name="email" type="email">
```

Validation Step

```text
Inspect input in Accessibility tree.
Confirm accessible name is Email.
```

Expected Result

```text
Email field exposes a clear accessible name.
```

## Issue 4 - Weak Image Accessible Name

Problem

```text
The decorative placeholder uses role="img" with weak aria-label="image".
```

Evidence

```text
Manual DevTools finding:
Placeholder is technically named, but the accessible name is not meaningful.
```

Impact

```text
Assistive technology users may hear low-value or confusing content.
```

Recommended Fix

Option 1:

```html
<div role="img" aria-label="Synthetic dashboard illustration"></div>
```

Option 2 if decorative:

```html
<div aria-hidden="true"></div>
```

Validation Step

```text
Confirm image is either meaningfully named or hidden from assistive technology if decorative.
```

Expected Result

```text
The image target becomes either meaningful or intentionally ignored by assistive technology.
```

## Issue 5 - Vague Link Text

Problem

```text
The link text "Click here" does not describe the destination clearly.
```

Evidence

```text
Manual DevTools finding:
Link text is vague and not descriptive out of context.
```

Impact

```text
Users scanning links, especially with assistive technology, cannot infer link purpose easily.
```

Recommended Fix

```html
<a href="#example">Review the example accessibility issue</a>
```

Validation Step

```text
Inspect link text out of context.
Confirm link purpose is understandable.
```

Expected Result

```text
Link purpose is clear without surrounding paragraph context.
```

## Issue 6 - Custom Chip Has No Visible Focus Style

Problem

```text
The custom chip is keyboard-focusable but does not show visible focus.
```

Evidence

```text
Manual DevTools finding:
custom chip uses role="button" and tabindex="0" but has no visible focus outline.
```

Impact

```text
Keyboard users may lose orientation and not know which control is active.
```

Recommended Fix

```css
.custom-chip:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Validation Step

```text
Use Tab navigation.
Confirm visible focus indicator appears.
Confirm no keyboard trap exists.
```

Expected Result

```text
Keyboard users can see focus location on the custom control.
```

## Validation Plan After Remediation

| Validation Area | Tool | Expected Result |
|---|---|---|
| Lighthouse Accessibility | Lighthouse | Score improves from 93 or failed audits decrease |
| Button name | Elements / Accessibility tree | Icon button has accessible name |
| Heading order | Lighthouse / Elements | Heading hierarchy is logical |
| Email input label | Accessibility tree | Email input has explicit accessible name |
| Link text | Manual review | Link purpose is clear |
| Focus style | Keyboard + Elements | Custom chip shows visible focus |
| Console | Console | No errors, warnings, or sensitive logs |

## DevTools Panels To Reuse

```text
Lighthouse
Elements
Accessibility tree
Console
```

## Safety Boundaries

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
No demo HTML change in this step.
```

## Portfolio Output

This remediation plan converts real Lighthouse and Chrome DevTools accessibility evidence into prioritized, testable fixes for a safe static demo page, demonstrating an evidence-based accessibility workflow suitable for a frontend portfolio.

## Next Step

Next step: Module 11-F should implement the remediation fixes in the static demo page, then Module 11-G should re-run Lighthouse and DevTools validation to compare before/after accessibility evidence.

# Module 11-H - Accessibility Portfolio Summary

## Project Summary

This module demonstrates an evidence-based accessibility workflow using Chrome DevTools and Lighthouse on a safe local static demo page. The workflow identified accessibility issues, prioritized remediation, implemented targeted HTML/CSS fixes, and validated the result with before/after evidence.

## Problem

The initial local Lighthouse audit reported an Accessibility score of 93 with two failed audits:

- button-name
- heading-order

Manual Chrome DevTools inspection also found:

- weak image accessible name
- unlabeled email input
- vague link text
- missing visible focus style on a custom chip

## Tools Used

- Chrome DevTools
- Lighthouse
- Elements panel
- Accessibility tree
- Console
- Keyboard navigation testing
- Git / GitHub pull request workflow

## Workflow

1. Created a safe static accessibility demo.
2. Collected baseline Lighthouse and DevTools evidence.
3. Documented confirmed accessibility issues.
4. Created a remediation plan.
5. Implemented targeted HTML/CSS fixes.
6. Re-ran Lighthouse and DevTools validation.
7. Documented before/after results.

## Evidence

Before remediation:

- Lighthouse Accessibility score: 93
- Failed audits: button-name, heading-order
- Console: no errors, no warnings, no sensitive data logs

After remediation:

- Lighthouse Accessibility score: 100
- Failed audits: none
- Passed audits: 26 binary accessibility audits
- Console: no errors, no warnings, no sensitive data logs

## Before / After Result

| Metric | Before | After | Result |
|---|---:|---:|---|
| Lighthouse Accessibility score | 93 | 100 | +7 improvement |
| Failed audits | 2 | 0 | All confirmed Lighthouse failures resolved |
| `button-name` | Failed | Passed | Fixed |
| `heading-order` | Failed | Passed | Fixed |
| Console errors | None | None | Clean |
| Console warnings | None | None | Clean |
| Sensitive logs | None | None | Clean |

## Technical Fixes

- Added accessible name to the icon-only button.
- Fixed heading hierarchy.
- Added explicit label association for the email input.
- Replaced vague link text with descriptive link text.
- Hid decorative image from the accessibility tree.
- Added visible focus style for the custom chip.

## DevTools Panels Used

- Lighthouse: measured Accessibility score and failed audits.
- Elements: inspected semantic HTML and heading structure.
- Accessibility tree: checked accessible names and label associations.
- Console: verified that no errors, warnings, secrets, or sensitive logs were present.
- Keyboard testing: validated tab order, focus visibility, keyboard activation, and keyboard trap absence.

## Safety Boundary

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

## GitHub Portfolio Description

Accessibility audit and remediation workflow using Chrome DevTools and Lighthouse. The project demonstrates how to identify accessibility issues, document real evidence, implement targeted HTML/CSS fixes, and validate improvements with before/after Lighthouse results. The local demo improved from 93 to 100 Accessibility score and resolved all confirmed Lighthouse failures.

## LinkedIn Post Draft

I completed a Chrome DevTools accessibility audit workflow on a safe local demo page.

Using Lighthouse, Elements, Accessibility Tree, Console, and keyboard testing, I identified accessibility issues such as an unnamed icon-only button and broken heading order.

After documenting the findings and creating a remediation plan, I implemented targeted HTML/CSS fixes and re-tested the page.

Result:

- Lighthouse Accessibility score improved from 93 to 100
- Failed audits went from 2 to 0
- Console stayed clean
- No deploy, cloud resource, secret, or real user data was involved

This was a practical exercise in evidence-based frontend accessibility debugging and remediation.

## CV Bullet

Performed an evidence-based accessibility audit and remediation workflow using Chrome DevTools and Lighthouse, improving a local static demo from 93 to 100 Accessibility score and resolving all confirmed Lighthouse failures through targeted HTML/CSS fixes.

## What I Learned

- Lighthouse can identify measurable accessibility failures.
- DevTools Accessibility tree helps verify accessible names and label associations.
- Keyboard testing is essential for focus visibility and navigation quality.
- Accessibility remediation should be documented before implementation.
- Before/after evidence makes portfolio work stronger and more credible.

## Next Step

Next step: Module 11-I should close the accessibility module with a final milestone summary and update the module index if needed.

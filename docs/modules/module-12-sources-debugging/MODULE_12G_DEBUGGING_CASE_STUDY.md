# Module 12-G — Before / After JavaScript Debugging Case Study

## Project Summary

This case study demonstrates a local JavaScript debugging workflow using Chrome DevTools Sources panel. A deliberate discount calculation bug was identified through runtime inspection, watch expressions, and source-level analysis, then fixed with a targeted one-line JavaScript change.

## Problem

The local demo calculated a shopping cart discount incorrectly.

For the default input:

- price: 100
- quantity: 2
- discount percent: 10

The expected final total was 180, but the buggy implementation returned 0.

## Tools Used

- Chrome DevTools Sources
- Breakpoints
- Call Stack
- Scope inspection
- Watch expressions
- Console
- Network
- Local Python static server
- Git / GitHub pull request workflow

## Debugging Workflow

1. Created a safe local JavaScript debugging demo.
2. Reproduced the incorrect UI result.
3. Set breakpoints around the calculation flow.
4. Inspected runtime variables in Scope.
5. Compared watch expressions for /10 and /100 behavior.
6. Identified the root cause in the discount calculation function.
7. Created a remediation plan.
8. Applied a one-line JavaScript fix.
9. Re-ran UI, Sources, Console, and Network validation.
10. Documented before/after evidence.

## Before State

| Field | Value |
|---|---:|
| Input price | 100 |
| Input quantity | 2 |
| Input discount percent | 10 |
| Observed subtotal | 200 |
| Observed discount | 200 |
| Observed final total | 0 |
| Expected final total | 180 |

## Root Cause

The discount calculation divided `discountPercent` by 10 instead of 100.

Buggy formula:

```javascript
return subtotal * (discountPercent / 10);
```

For `discountPercent = 10`:

```text
discountPercent / 10 = 1
subtotal * 1 = 200
```

This made the discount equal to 100% of the subtotal instead of 10%.

## Fix

The fix changed the percentage calculation from `/10` to `/100`.

Fixed formula:

```javascript
return subtotal * (discountPercent / 100);
```

## After State

| Field | Value |
|---|---:|
| Input price | 100 |
| Input quantity | 2 |
| Input discount percent | 10 |
| Subtotal | 200 |
| Discount | 20 |
| Final total | 180 |
| Expected final total | 180 |

## Before / After Comparison

| Metric | Before | After | Result |
|---|---:|---:|---|
| Discount | 200 | 20 | Fixed |
| Final total | 0 | 180 | Fixed |
| Formula | `/10` | `/100` | Corrected |
| Expected final total | 180 | 180 | Matches expected |
| Console errors | None | None | Clean |
| Console warnings | None | None | Clean |
| Network document request | 200 | 200 | Clean |
| app.js request | 200 | 200 | Clean |

## DevTools Evidence

Sources validation:

- Function checked: `calculateDiscountAmount(subtotal, discountPercent)`
- Fixed line: `app.js:35`
- Observed fixed formula: `return subtotal * (discountPercent / 100);`

Watch expressions:

- `discountPercent / 10 = 1`
- `discountPercent / 100 = 0.1`
- `subtotal * (discountPercent / 10) = 200`
- `subtotal * (discountPercent / 100) = 20`

Console:

- Errors: none
- Warnings: none
- Sensitive data logs: none

Network:

- `http://127.0.0.1:8089/` -> 200
- `app.js` -> 200

## Safety Boundary

No deploy.
No public endpoint.
No cloud resource.
No API enablement.
No IAM change.
No billing impact.
No real user data.
No PHI.
No e-Nabız export.
No TCKN.
No secrets.
No .env.
No external API.

## Portfolio Output

This module produced a portfolio-ready JavaScript debugging case study showing how to reproduce a bug, inspect runtime state with Chrome DevTools Sources, identify the root cause, apply a focused fix, and validate before/after results.

## LinkedIn Post Draft

I completed a Chrome DevTools JavaScript debugging workflow using the Sources panel.

The demo had a deliberate discount calculation bug:

- Expected final total: 180
- Buggy final total: 0

Using breakpoints, scope inspection, call stack reasoning, watch expressions, Console, and Network checks, I traced the issue to a percentage calculation error.

Root cause:
discountPercent was divided by 10 instead of 100.

After a focused one-line fix:

- Discount changed from 200 to 20
- Final total changed from 0 to 180
- Console stayed clean
- Static files loaded locally with 200 responses
- No deploy, cloud resource, secret, or real user data was involved

This was a practical exercise in evidence-based JavaScript debugging with Chrome DevTools.

## CV Bullet

Built and documented an evidence-based JavaScript debugging workflow using Chrome DevTools Sources, identifying a discount calculation bug through breakpoints, scope inspection, watch expressions, and before/after validation, then resolving it with a targeted one-line fix.

## What I Learned

- Breakpoints help pause code at the exact calculation path.
- Scope inspection reveals real runtime variable values.
- Watch expressions are useful for comparing suspected formulas.
- Console and Network checks confirm the local app remains clean after a fix.
- Before/after evidence makes debugging work portfolio-ready.

## Next Step

Next step: Module 12-H should create a final milestone closure for the DevTools Sources Debugging module.

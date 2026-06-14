# Module 12-C - Sources Debugging Evidence

## Purpose

This document records real local debugging evidence collected from the Module 12 safe JavaScript debugging demo. The goal is to document how Chrome DevTools Sources-style debugging evidence was used to identify the root cause of a deliberate discount calculation bug.

## Scope

This is an evidence-only step. No bug fix is performed in Module 12-C.

## Local URL

http://localhost:8089

## Initial Bug Behavior

| Field | Value |
|---|---:|
| Input price | 100 |
| Input quantity | 2 |
| Input discount percent | 10 |
| Observed subtotal | 200 |
| Observed discount | 200 |
| Observed final total | 0 |
| Expected final total | 180 |

## Breakpoints

Breakpoint 1: the calculate flow entry in the demo script, at `runCalculation()` around line 52.

Breakpoint 2: the discount calculation line in the demo script, at `calculateDiscountAmount()` around line 33, specifically:

```javascript
return subtotal * (discountPercent / 10);
```

## Call Stack

Observed call stack:

```text
submit handler
-> runCalculation()
-> calculateSubtotal()
-> calculateDiscountAmount()
-> calculateFinalTotal()
```

The evidence records the observed runtime/source mapping from the local demo.

## Scope And Variables

| Variable | Observed Value |
|---|---:|
| price | 100 |
| quantity | 2 |
| discountPercent | 10 |
| subtotal | 200 |
| discount | 200 |

## Watch Expressions

| Watch Expression | Observed Value |
|---|---:|
| discountPercent / 10 | 1 |
| discountPercent / 100 | 0.1 |
| subtotal * (discountPercent / 10) | 200 |
| subtotal * (discountPercent / 100) | 20 |

## Root Cause

`calculateDiscountAmount()` divides `discountPercent` by `10` instead of `100`. For the sample input, `discountPercent` is `10`, so `discountPercent / 10` becomes `1`. This makes the discount equal to 100% of the subtotal instead of 10%.

Correct logic should use `discountPercent / 100`.

## Console Evidence

```text
Errors: none
Warnings: none
Sensitive data logs: none
Normal demo log observed: Module 12 demo calculation complete Object
```

## Notes

The live demo produced one normal console log from the calculation path.

The Sources-panel UI itself was not directly exposed through the browser backend, so this evidence records the live runtime values and source-line mapping observed from the same local code path.

No fix was applied in this step.

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
No e-Nabız export.
No TCKN.
No secrets.
No .env.
No external API.
```

## Next Step

Next step: Module 12-D should create a remediation plan for the confirmed discount calculation bug. Module 12-E should implement the fix in a separate small PR.

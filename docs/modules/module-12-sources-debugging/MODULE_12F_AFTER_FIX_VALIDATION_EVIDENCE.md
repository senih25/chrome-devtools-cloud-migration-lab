# Module 12-F — After-Fix Sources / UI Validation Evidence

## Purpose
Record the post-fix validation for the confirmed JavaScript discount calculation issue after Module 12-E.

## Scope
This is an evidence-only documentation step.

No bug fix is made here.
No HTML change is made here.
No deploy is performed.
No API enablement is performed.
No IAM change is performed.
No cloud resource is created.

## UI Result

| Field | Value |
|---|---:|
| Input price | 100 |
| Input quantity | 2 |
| Input discount percent | 10 |
| Subtotal | 200 |
| Discount | 20 |
| Final total | 180 |
| Expected final total | 180 |

## Sources Validation
- Function checked: `calculateDiscountAmount(subtotal, discountPercent)`
- Fixed line: `app.js:35`
- Breakpoint location: return statement inside `calculateDiscountAmount()`
- Observed formula: `return subtotal * (discountPercent / 100);`

## Watch Expressions

| Watch expression | Observed value |
|---|---:|
| `discountPercent / 10` | 1 |
| `discountPercent / 100` | 0.1 |
| `subtotal * (discountPercent / 10)` | 200 |
| `subtotal * (discountPercent / 100)` | 20 |

## Before / After Comparison
- Before observed discount: 200
- After observed discount: 20
- Before final total: 0
- After final total: 180
- Root cause fixed: the calculation now divides `discountPercent` by `100` instead of `10`

## Console
- Errors: none
- Warnings: none
- Sensitive data logs: none
- Normal logs: `Module 12 demo calculation complete {price: 100, quantity: 2, discountPercent: 10, subtotal: 200, discountAmount: 20}`

## Network Evidence

| Resource | Status |
|---|---:|
| `http://127.0.0.1:8089/` | 200 |
| `app.js` | 200 |

The local static server responded successfully. No failed document or script request was observed during the after-fix validation.

## Safety Boundary
No PHI.
No real health data.
No e-Nabız export.
No TCKN.
No secrets.
No `.env`.
No deploy.
No public endpoint exposure.
No cloud resource changes.
No external API.

## Out of Scope
- No additional bug fix.
- No production debugging.
- No remote debugging.
- No cloud logging.
- No dependency changes.
- No screenshot artifacts added to the repo.

## Portfolio Output
This evidence confirms the local debugging workflow: Sources inspection, runtime validation, and UI confirmation all align with the expected JavaScript fix.

## Next Step
Next step: create a short docs-only summary of the after-fix validation and then continue with the next Module 12 evidence or closure task.

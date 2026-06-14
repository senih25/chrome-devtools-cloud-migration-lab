# Module 12-D — JavaScript Bug Remediation Plan

## Purpose
This document converts the Module 12-C Sources debugging evidence into a clear remediation plan for the confirmed JavaScript discount calculation bug.

## Scope
This is a planning-only step. No JavaScript fix is implemented in Module 12-D.

## Evidence Baseline

| Field | Value |
|---|---:|
| Input price | 100 |
| Input quantity | 2 |
| Input discount percent | 10 |
| Observed subtotal | 200 |
| Observed discount | 200 |
| Observed final total | 0 |
| Expected final total | 180 |

## Confirmed Bug
The discount calculation returns 200 instead of 20 for the sample input.

## Root Cause
`calculateDiscountAmount()` divides `discountPercent` by `10` instead of `100`.

Observed expression:

```javascript
return subtotal * (discountPercent / 10);
```

For `discountPercent = 10`:

```text
discountPercent / 10 = 1
subtotal * 1 = 200
```

## Expected Correct Behavior
Correct percentage calculation should divide by 100.

Expected expression:

```javascript
return subtotal * (discountPercent / 100);
```

For `discountPercent = 10`:

```text
discountPercent / 100 = 0.1
subtotal * 0.1 = 20
```

## Proposed Fix

```javascript
function calculateDiscountAmount(subtotal, discountPercent) {
  return subtotal * (discountPercent / 100);
}
```

The fix should be implemented in Module 12-E, not in this planning PR.

## Validation Plan

| Validation Area | Tool | Expected Result |
|---|---|---|
| Local page load | Browser / Network | `index.html` and `app.js` load locally |
| Calculation result | UI | Final total becomes 180 for default input |
| Debugging confirmation | Sources | Watch expression `subtotal * (discountPercent / 100)` evaluates to 20 |
| Console | Console | No errors or warnings |
| Sensitive data | Console / Diff scan | No secrets, PHI, TCKN, API keys, or `.env` |

## DevTools Panels To Reuse
- Sources: verify the corrected formula and step through the calculation.
- Scope: inspect subtotal and discountPercent.
- Watch expressions: compare `/10` and `/100` behavior if needed.
- Call Stack: confirm calculation path.
- Console: verify no runtime errors.
- Network: optionally confirm local static files return 200.

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
No `.env`.
No external API.

## Out of Scope
- No bug fix in this step.
- No production debugging.
- No remote debugging.
- No cloud logging.
- No external API.
- No dependency changes.

## Portfolio Output
This remediation plan shows how runtime debugging evidence from Chrome DevTools Sources can be translated into a targeted, testable JavaScript fix plan.

## Next Step
Next step: Module 12-E should implement the one-line JavaScript fix and perform a local smoke check. Module 12-F should collect after-fix Sources and UI validation evidence.

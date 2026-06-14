# Module 11-C - Safe Static Demo Accessibility Evidence

## Purpose

This document prepares evidence collection for a safe synthetic static accessibility demo using Chrome DevTools and Lighthouse.

## Scope

This module adds a local-only demo target and a matching evidence structure for future manual review.

## Demo Target

Primary demo target:

```text
experiments/module-11-accessibility-demo/index.html
```

## Local-Only Boundary

```text
No deploy.
No public endpoint.
No cloud resource.
No API.
No IAM.
No billing impact.
No real user data.
No PHI.
No e-Nabiz export.
No TCKN.
No secrets.
No .env.
```

## How To Run Locally

Option 1:

```powershell
Start-Process .\experiments\module-11-accessibility-demo\index.html
```

Option 2:

```powershell
python -m http.server 8088 --directory experiments\module-11-accessibility-demo
```

Target URL:

```text
http://localhost:8088
```

## DevTools Panels Used

```text
Lighthouse
Elements
Accessibility tree
Console
Rendering / contrast-related inspection where applicable
```

## Lighthouse Accessibility Evidence

Capture:

```text
Accessibility score
Failed audits
Passed audit summary
Selectors or elements mentioned in Lighthouse output
Notes for remediation
```

## Elements / Accessibility Tree Evidence

Check:

```text
image accessible text
button accessible names
form labels
heading structure
landmarks
link clarity
tabindex usage
role usage
```

## Keyboard Navigation Evidence

Capture notes for:

```text
tab order
keyboard activation
keyboard trap check
reachable interactive elements
```

## Focus Visibility Evidence

Verify:

```text
default focus visibility
custom control focus visibility
focus consistency across controls
```

## Color Contrast Evidence

Review:

```text
helper text contrast
button contrast
link contrast
focus indicator contrast
```

## Forms / Labels Evidence

Review:

```text
explicit labels
missing labels
placeholder misuse
submit button meaning
textarea labeling
```

## Console Evidence

Confirm:

```text
no client-side errors
no accessibility-related runtime warnings if any appear
```

## Findings Table

| Area | Tool / Panel | Status | Finding | Severity | Recommendation |
|---|---|---:|---|---|---|
| Lighthouse score | Lighthouse | Pending manual audit | TBD | TBD | Run Lighthouse Accessibility audit locally |
| Image alt text | Elements / Accessibility tree | Pending manual audit | TBD | TBD | Check image accessible name |
| Button name | Elements / Accessibility tree | Pending manual audit | TBD | TBD | Check button accessible name |
| Form labels | Elements / Accessibility tree | Pending manual audit | TBD | TBD | Check label association |
| Color contrast | Lighthouse / Elements | Pending manual audit | TBD | TBD | Check text/background contrast |
| Keyboard navigation | Keyboard + DevTools | Pending manual audit | TBD | TBD | Verify logical tab order and activation |
| Focus visibility | Elements | Pending manual audit | TBD | TBD | Verify visible focus state |
| Console errors | Console | Pending manual audit | TBD | TBD | Confirm no client-side errors |

## Remediation Plan

Expected remediation themes:

```text
add meaningful accessible text
restore proper labeling
fix heading hierarchy
improve contrast
replace unclear link wording
restore visible focus styling
```

## Portfolio Note

This module creates a safe static accessibility audit target and prepares evidence collection using Chrome DevTools Lighthouse, Elements, Accessibility tree, keyboard navigation, focus visibility, color contrast, and Console checks.

## Next Step

After this work is reviewed and merged, the next safe step is to open the local demo in Chrome and collect actual Lighthouse and DevTools evidence in Module 11-D.

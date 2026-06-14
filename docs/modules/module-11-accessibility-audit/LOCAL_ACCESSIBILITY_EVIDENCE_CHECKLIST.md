# Module 11-B - Local Accessibility Evidence Checklist

## Purpose

This document defines the evidence checklist for a future local accessibility audit using Chrome DevTools and Lighthouse.

## Scope

This is a docs-only evidence checklist.
No audit is executed in this step.
No deploy is performed.
No cloud resource is changed.
No API is enabled.
No IAM change is made.
No secrets or .env files are created.
No real user data or PHI is used.

## Non-Execution Statement

This document prepares evidence capture only. It does not execute an accessibility audit.

## Target Page Selection

Use only a local, static, synthetic, or public-safe demo page.
Do not use real user data.
Do not use health data.
Do not use e-Nabiz data.
Do not use private dashboards.
Do not use authenticated sensitive pages.

## Chrome DevTools Panels

Use the following panels and views where relevant:

```text
Lighthouse
Elements
Accessibility tree
Console
Rendering / contrast-related inspection where applicable
```

## Lighthouse Accessibility Evidence

Collect:

```text
Accessibility score
Failed audits
Passed audits summary
Affected element selectors
Screenshot or note reference
Recommended remediation
```

## Elements / Accessibility Tree Evidence

Check:

```text
heading order
button accessible names
link text clarity
image alt text
form labels
landmarks
tabindex usage
ARIA role usage
visible focus styles
```

## Keyboard Navigation Evidence

Check:

```text
Can the page be used with Tab?
Is focus order logical?
Is focus visible?
Can interactive elements be activated with keyboard?
Is there a keyboard trap?
Can modal/dialog content be navigated safely if present?
```

## Focus Visibility Evidence

Review whether keyboard focus is clearly visible across:

```text
links
buttons
form fields
menus
dialogs if present
```

## Color Contrast Evidence

Check:

```text
text/background contrast
button contrast
link contrast
focus indicator contrast
disabled state clarity
```

## Semantic HTML Evidence

Verify:

```text
proper heading structure
semantic buttons vs clickable divs
semantic links
form structure
landmark elements
meaningful document structure
```

## ARIA Evidence

Verify:

```text
ARIA used only when needed
correct aria-label or aria-labelledby usage
no conflicting roles
no redundant ARIA on native controls
accessible naming consistency
```

## Forms / Labels Evidence

Check:

```text
visible labels
programmatic labels
placeholder misuse
error message clarity
required field communication
button meaning and submission clarity
```

## Console Evidence

Check whether Console shows:

```text
accessibility-related warnings
unexpected client-side errors
rendering issues that affect usability
```

## Evidence Table Template

| Check Area | Tool / Panel | Status | Finding | Severity | Recommendation |
|---|---|---:|---|---|---|
| Lighthouse score | Lighthouse | Pending | TBD | TBD | TBD |
| Heading order | Elements / Accessibility tree | Pending | TBD | TBD | TBD |
| Keyboard navigation | Keyboard + DevTools | Pending | TBD | TBD | TBD |
| Focus visibility | Elements / Rendering | Pending | TBD | TBD | TBD |
| Color contrast | Elements / Lighthouse | Pending | TBD | TBD | TBD |
| Form labels | Elements / Accessibility tree | Pending | TBD | TBD | TBD |
| Console errors | Console | Pending | TBD | TBD | TBD |

## Finding Severity Guide

```text
Critical: blocks keyboard or screen reader access.
High: major navigation, labeling, or contrast issue.
Medium: affects usability but workaround exists.
Low: minor improvement or documentation note.
```

## Safety Boundaries

```text
No deploy.
No public endpoint exposure.
No cloud billing impact.
No real user data.
No PHI.
No e-Nabiz export.
No TCKN.
No secrets.
No .env.
No private authenticated page.
```

## Portfolio Output

This checklist prepares a portfolio-ready accessibility audit workflow using Chrome DevTools, Lighthouse, keyboard navigation checks, semantic HTML review, and evidence-based remediation notes.

## Next Step

After this checklist is reviewed and merged, the next safe step is to run a local accessibility audit on a safe static demo page and record the evidence in Module 11-C.

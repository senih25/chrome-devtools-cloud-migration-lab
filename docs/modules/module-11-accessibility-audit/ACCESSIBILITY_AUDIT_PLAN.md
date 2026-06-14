# Module 11-A - Accessibility Audit Plan

## Purpose

This document defines a local-first accessibility audit plan for Module 11 using Chrome DevTools and Lighthouse.

## Scope

This is a docs-only accessibility audit planning step.

No deploy is performed.
No cloud resource is changed.
No API is enabled.
No IAM change is made.
No secrets or .env files are created.
No real user data or PHI is used.

## Why Accessibility Matters

Accessibility work improves usability, keyboard reachability, screen reader compatibility, color readability, and overall interface quality.

It also produces evidence-based engineering output that can be reviewed, prioritized, and converted into concrete remediation work.

## Chrome DevTools Panels To Use

The primary Chrome DevTools surfaces for this module are:

```text
Lighthouse
Elements
Accessibility tree
Console
Rendering / contrast-related inspection where applicable
```

## Lighthouse Accessibility Checks

Lighthouse should be used as the first pass to identify broad accessibility issues and provide a baseline score.

Focus areas:

```text
accessibility score
failed accessibility audits
contrast failures
form label issues
button and link naming issues
heading structure issues
landmark and semantic issues
```

## Elements Panel Checks

The Elements panel should be used to inspect failing nodes directly and verify DOM structure.

Check for:

```text
heading order
button text clarity
link text clarity
form control labels
image alt attributes
focusable element behavior
semantic container usage
```

## Keyboard Navigation Checks

A manual keyboard pass should validate:

```text
tab order
focus visibility
reachability of interactive elements
escape behavior where applicable
unreachable controls
keyboard traps
```

## Color Contrast Checks

Color contrast should be inspected wherever text, icons, or focus indicators may become difficult to perceive.

Check for:

```text
foreground / background contrast
focus ring visibility
disabled state visibility
text over gradients or images
contrast regressions in buttons, links, and form states
```

## ARIA / Semantic HTML Checks

Review the page for correct semantic HTML and appropriate ARIA usage.

Focus on:

```text
native semantic elements before ARIA
clear form labeling
meaningful button and link names
heading hierarchy
landmark regions
aria-label / aria-labelledby correctness
avoiding unnecessary or incorrect ARIA roles
```

## Evidence To Capture

Capture the following evidence in later local audit work:

```text
Lighthouse Accessibility score
List of failed audits
Affected elements
Keyboard navigation notes
Focus order notes
Color contrast findings
ARIA / semantic HTML findings
Before / after recommendation summary
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
```

## Local-First Workflow

Recommended local-first workflow:

```text
1. Select a local or static demo page.
2. Run Lighthouse Accessibility audit.
3. Inspect failing elements in Elements panel.
4. Check keyboard navigation.
5. Check focus visibility.
6. Check color contrast.
7. Check labels, headings, buttons, links, and form controls.
8. Record findings in a markdown evidence note.
9. Convert findings into portfolio-ready summary.
```

## Portfolio Output

This module will produce a portfolio-ready accessibility audit workflow using Chrome DevTools, Lighthouse, Elements inspection, keyboard navigation checks, and evidence-based remediation notes.

Expected portfolio value:

```text
clear audit method
repeatable local workflow
evidence-driven findings
remediation-ready notes
public-safe accessibility documentation
```

## Next Step

After this planning document is reviewed and merged, the next safe step is to create a local accessibility evidence checklist or run a local Lighthouse accessibility audit on a safe demo page.

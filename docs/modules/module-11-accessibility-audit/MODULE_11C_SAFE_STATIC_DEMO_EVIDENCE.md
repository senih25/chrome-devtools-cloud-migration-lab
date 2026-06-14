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

- Accessibility score: `93`
- Failed audits:
  - `button-name` -> icon-only button has no accessible name
  - `heading-order` -> heading sequence is not descending correctly
- Passed audit summary: `24 / 26` binary accessibility audits passed
- Selectors observed in Lighthouse output:
  - `div.hero-grid > div > div.actions > button.icon-only-button`
  - `section#overview > div.hero-grid > div > h3`
- Notes for remediation:
  - add a meaningful accessible name to the icon-only button
  - restore logical heading order

## Elements / Accessibility Tree Evidence

- Image accessible text: placeholder is exposed as `role="img"` with `aria-label="image"`; technically named, but the accessible name is too weak to be useful
- Button accessible names: icon-only `+` button has no `aria-label` and no title
- Form labels: `#email` input has no explicit label association; `name`, `topic`, and `notes` fields are labeled
- Heading structure: page order is `h1 -> h3 -> h2`, which creates a deliberate hierarchy break
- Landmarks: semantic structure exists with `header`, `nav`, `main`, `section`, `form`, and `footer`
- Link clarity: `Click here` link text is present and is not descriptive
- Tabindex usage: custom chip uses `tabindex="0"`
- Role usage: custom chip uses `role="button"`

## Keyboard Navigation Evidence

- Tab order: logical in the tested sequence of nav links -> hero buttons -> `Click here` link -> custom chip -> form controls
- Keyboard activation: native buttons and links are keyboard-focusable; custom chip is focusable but its activation behavior is not implemented beyond role/tabindex
- Keyboard trap check: none observed
- Reachable interactive elements: native links, buttons, custom chip, and form controls were all reachable during the test

## Focus Visibility Evidence

- Default focus visibility: visible on native links, buttons, and inputs
- Custom control focus visibility: not visible on the custom chip
- Focus consistency across controls: generally consistent except for the custom chip

## Color Contrast Evidence

- Lighthouse did not flag `color-contrast`
- Manual review still suggests keeping helper text and low-emphasis copy under review
- Focus indicator contrast appears acceptable on native elements
- Custom chip remains a visibility issue due to missing visible focus style rather than a Lighthouse contrast failure

## Forms / Labels Evidence

- Explicit labels: present for `name`, `topic`, and `notes`
- Missing labels: `email` input has no explicit label
- Placeholder misuse: email placeholder acts as the only visible naming hint for that field
- Submit button meaning: `Send synthetic request` is clear
- Textarea labeling: present for `notes`

## Console Evidence

- Errors: `None`
- Warnings: `None`
- Sensitive data logs: `None`

## Findings Table

| Area | Tool / Panel | Status | Finding | Severity | Recommendation |
|---|---|---:|---|---|---|
| Lighthouse score | Lighthouse | Completed | Accessibility score: 93; 24/26 binary audits passed | Medium | Use score as baseline and fix confirmed failed audits |
| Image alt text | Elements / Accessibility tree | Completed | Placeholder exposed as `role="img"` with weak `aria-label="image"` | Low | Use meaningful accessible name or mark decorative if appropriate |
| Button name | Lighthouse / Accessibility tree | Failed | Icon-only `+` button has no accessible name | High | Add `aria-label` or visible text |
| Form labels | Elements / Accessibility tree | Manual finding | `#email` input has no explicit label association | Medium | Add explicit `<label for="email">` |
| Heading order | Lighthouse | Failed | Heading order breaks as `h1 -> h3 -> h2` | High | Use logical heading sequence |
| Link text | Manual inspection | Manual finding | `Click here` link text is vague | Medium | Replace with descriptive link text |
| Color contrast | Lighthouse / Elements | Passed by Lighthouse; manual review noted | No Lighthouse failure, but review remains recommended | Low | Keep contrast review in remediation checklist |
| Keyboard navigation | Keyboard + DevTools | Completed | Tab order logical; no trap observed | Low | Preserve logical order during remediation |
| Focus visibility | Keyboard + Elements | Manual finding | Custom chip has no visible focus outline | High | Add visible focus style |
| Console errors | Console | Completed | No errors, warnings, or sensitive logs | Low | Keep console clean |

## Module 11-D Manual Evidence

### Local URL

```text
http://localhost:8088
```

### Lighthouse

- Accessibility score: `93`
- Failed audits:
  - `button-name` - icon-only button has no accessible name.
  - `heading-order` - heading sequence is not descending correctly.
- Notable warnings: `None`
- Passed audits summary: `24 / 26` binary accessibility audits passed.

### Elements / Accessibility Tree

- Image alt: decorative image placeholder is exposed as `role="img"` with `aria-label="image"`; technically named, but the name is too weak to be useful.
- Button accessible name: icon-only `+` button has no `aria-label`, no title, and Lighthouse flags it.
- Form labels: `#email` input has no explicit label association; `name`, `topic`, and `notes` fields are labeled.
- Heading order: page goes `h1 -> h3 -> h2`, so there is a deliberate hierarchy break.
- Link text: `Click here` is present and is not descriptive.
- ARIA / semantic HTML:
  - good semantic structure exists: `header`, `nav`, `main`, `section`, `form`, `footer`
  - custom chip uses `role="button"` and `tabindex="0"`
  - custom chip has no visible focus outline (`outline: none`)

### Keyboard

- Tab order: logical in the tested sequence: nav links -> hero buttons -> `Click here` link -> custom chip -> form controls.
- Focus visibility: visible on native links/buttons/inputs; not visible on the custom chip.
- Keyboard activation: native buttons and links are keyboard-focusable; custom chip is focusable but its activation behavior is not implemented beyond role/tabindex.
- Keyboard trap: none observed.

### Console

- Errors: `None`
- Warnings: `None`
- Sensitive data logs: `None`

### Notes

- Real Lighthouse evidence was collected locally with a temporary local run.
- No deploy or cloud action was used.
- Lighthouse did not flag `color-contrast`, `label`, or `link-name`, but manual inspection still shows weak UX/accessibility patterns:
  - non-descriptive image name
  - unlabeled email field
  - vague `Click here` link text
  - missing visible focus style on custom chip
- Most critical confirmed issues:
  - unnamed icon-only button
  - broken heading order

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

After this work is reviewed and merged, the next safe step is to prepare Module 11-E remediation plan for the confirmed accessibility issues.

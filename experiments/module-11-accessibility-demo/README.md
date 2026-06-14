# Module 11 Accessibility Demo

## Purpose

This folder contains a synthetic static demo page for safe local accessibility inspection.

## Safety

The demo is intentionally local-only and synthetic.

- No deploy
- No cloud resource
- No API request
- No real user data
- No PHI
- No e-Nabiz data
- No TCKN
- No secrets

## How To Open Locally

Option 1:

```powershell
Start-Process .\experiments\module-11-accessibility-demo\index.html
```

Option 2:

```powershell
python -m http.server 8088 --directory experiments\module-11-accessibility-demo
```

Then open:

```text
http://localhost:8088
```

This local server is not a deploy and does not expose a public cloud endpoint.

## What To Inspect

- Lighthouse Accessibility audit
- Elements panel and Accessibility tree
- Keyboard navigation
- Focus visibility
- Color contrast
- Form labeling
- Accessible names for buttons and links

## Expected Accessibility Issues

- image without useful accessible text
- button without accessible name
- input without label
- low contrast helper text
- unclear link text
- heading order issue
- missing visible focus style on one custom control

## DevTools Panels

- Lighthouse
- Elements
- Accessibility tree
- Console
- Rendering / contrast-related inspection where applicable

## No Cloud Boundary

This demo does not use cloud resources, APIs, authentication, deploy infrastructure, public endpoints, or secrets.

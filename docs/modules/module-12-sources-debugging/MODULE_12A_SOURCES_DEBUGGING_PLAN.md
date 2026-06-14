# Module 12-A - DevTools Sources Debugging Plan

## Purpose

Module 12 introduces JavaScript debugging with Chrome DevTools Sources panel. The goal is to learn how to pause execution, inspect variables, follow call stack, step through code, and document a reproducible debugging workflow.

## Scope

This module will stay local-first and synthetic. It will use a small static JavaScript debugging demo in a later step. No cloud resource, deploy, external API, real user data, or secret will be used.

## Learning Goals

- Open and navigate the Sources panel.
- Set and remove breakpoints.
- Use step over, step into, and step out.
- Inspect local and global variables.
- Read the call stack.
- Use watch expressions.
- Pause on exceptions.
- Debug a deliberate JavaScript logic bug.
- Capture before/after debugging evidence.

## DevTools Panels

- Sources: breakpoints, call stack, scope, watch expressions, stepping.
- Console: error messages and quick variable checks.
- Elements: optional DOM state verification.
- Network: optional static file loading check.

## Debugging Concepts

- Breakpoint
- Conditional breakpoint
- Call stack
- Scope
- Watch expression
- Step over
- Step into
- Step out
- Pause on exception
- Source file mapping
- Runtime state inspection

## Planned Demo Scenario

A local static demo will be created in a later PR. The demo should include a simple JavaScript bug such as an incorrect total calculation, a wrong condition, or a broken form interaction. The bug must be synthetic and safe.

## Evidence To Collect

- Screenshot or written evidence of breakpoint location.
- Initial bug behavior.
- Variable values before the fix.
- Call stack observation.
- Root cause explanation.
- Fix summary.
- Console status after fix.
- Local-only validation result.

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
No external API.
```

## Out of Scope

- No production debugging.
- No remote debugging.
- No cloud logs.
- No real API credentials.
- No browser extension debugging yet.
- No React debugging yet.

## Portfolio Output

This module will produce a portfolio-ready JavaScript debugging case study showing how to use Chrome DevTools Sources panel to identify a bug, inspect runtime state, explain root cause, implement a fix, and validate the result.

## Next Step

Next step: Module 12-B should create a safe local JavaScript debugging demo with a deliberate logic bug.

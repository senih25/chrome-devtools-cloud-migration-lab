# Module 10-A — Security Panel and Web Security Checks Plan

## Purpose
Module 10 introduces browser-side web security analysis with Chrome DevTools Security and Network panels. The goal is to learn how to inspect secure contexts, HTTPS state, mixed content signals, certificate information, response headers, cookies, and basic Content Security Policy indicators in a safe local workflow.

## Scope
This module will stay local-first and synthetic. It will use a safe local demo in a later step. No production site testing, public endpoint exposure, cloud resource, external API, real user data, credential, or secret will be used.

## Learning Goals
- Open and interpret the Chrome DevTools Security panel.
- Understand secure context versus non-secure context signals.
- Identify mixed content concepts.
- Inspect request and response details in the Network panel.
- Review security-related response headers.
- Understand basic Content Security Policy purpose.
- Understand cookie security attributes at a high level.
- Document security findings safely without testing real systems.
- Convert browser-side security checks into portfolio evidence.

## DevTools Panels
- Security: page security state, secure origin signals, certificate overview.
- Network: headers, status codes, resource loading, response metadata.
- Application: cookies and storage inspection if needed.
- Console: security-related warnings and runtime messages.

## Security Concepts
- HTTPS
- Secure context
- Mixed content
- Certificate
- Same-origin basics
- Response headers
- Content Security Policy
- Cookie attributes
- HttpOnly
- Secure
- SameSite
- Local-only security testing boundary

## Planned Demo Scenario
A safe local demo will be created in a later PR. The demo should allow browser-side inspection of security-related concepts without using real credentials, real user data, external APIs, production endpoints, or cloud resources.

## Evidence To Collect
- Security panel page state.
- Local URL used for testing.
- Network document request status.
- Response headers observed.
- Console security warnings if any.
- Cookie/storage state if used.
- Notes about what can and cannot be verified in a local HTTP-only demo.
- Safety boundary confirmation.

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
No production security testing.
No scanning third-party sites.
No vulnerability probing.

## Out of Scope
- No penetration testing.
- No production security testing.
- No real user account testing.
- No credential handling.
- No cloud security configuration changes.
- No IAM changes.
- No external API testing.
- No automated vulnerability scanning.

## Portfolio Output
This module will produce a portfolio-ready browser-side security inspection case study showing how to use Chrome DevTools Security and Network panels to document safe, local web security observations and remediation thinking.

## Next Step
Next step: Module 10-B should create a safe local security inspection demo that can be analyzed with Chrome DevTools Security, Network, Console, and Application panels.

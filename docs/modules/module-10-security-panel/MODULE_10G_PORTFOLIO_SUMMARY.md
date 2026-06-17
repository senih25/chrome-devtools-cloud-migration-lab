# Module 10-G — Web Security and Chrome DevTools Case Study

## Project Overview

This case study demonstrates the process of auditing, planning, and remediating web security exposures for a local application using **Chrome DevTools**. By utilizing a sandboxed local-first workflow, we implemented and verified defense-in-depth security headers and Content Security Policy (CSP) alignment without incurring cloud costs or introducing data exposure risks.

---

## 1. Context & Objectives

Modern web applications must enforce security controls to mitigate common attack vectors such as Cross-Site Scripting (XSS), clickjacking, and MIME-type sniffing.

The goal of this module was to:
1. **Audit** a local static web application served via standard Python `http.server` using Chrome DevTools.
2. **Identify** missing security headers and browser-side security vulnerabilities.
3. **Remediate** the identified weaknesses by writing a custom Python server (`server.py`) and refactoring application assets.
4. **Validate** the security controls using Chrome DevTools Security, Network, Console, and Application panels.

---

## 2. The Auditing Phase (DevTools Inspection)

We launched the unmitigated application on `http://127.0.0.1:8090/` and conducted a multi-panel audit:

### Security Panel
* **Finding**: The Security Panel identified the context as an HTTP cleartext transport.
* **Analysis**: While localhost loopback addresses are treated as secure enough for development, production deployments must enforce HTTPS. This formed the basis for planning HSTS enforcement.

### Network Panel
* **Finding**: The response headers for HTML and JS payloads lacked security protections.
* **Analysis**:
  - No `Content-Security-Policy` (CSP) was declared, exposing the app to script injection.
  - No `X-Frame-Options` or `frame-ancestors` directive was active, leaving the application vulnerable to clickjacking.
  - No `X-Content-Type-Options` was set, allowing browsers to guess (sniff) the MIME type.

### Application Panel
* **Finding**: Verified that client-side storage (`localStorage` and `sessionStorage`) was used.
* **Analysis**: Ensured that the values written are strictly synthetic and do not store any sensitive session identifiers or credentials.

---

## 3. Remediation & Implementation

To address these vulnerabilities, we developed a custom multi-threaded Python server (`server.py`) that subclassed `SimpleHTTPRequestHandler` to dynamically inject modern security response headers.

### Security Header Architecture
We configured the server to supply the following HTTP header payload:
```python
SECURITY_HEADERS = {
    "Content-Security-Policy": (
        "default-src 'self'; "
        "base-uri 'self'; "
        "connect-src 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "script-src 'self'; "
        "style-src 'self'"
    ),
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer-when-downgrade",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}
```

### Refactoring for CSP Compliance
Our audit identified inline CSS styling that would violate a strict CSP (`style-src 'self'`). To resolve this:
1. We stripped inline styles out of `index.html`.
2. Created a dedicated external stylesheet `styles.css`.
3. Moved all styles to `styles.css` and linked it via a standard `<link>` tag.
4. This allowed us to enforce a clean Content Security Policy without needing to declare `'unsafe-inline'` or hash values.

---

## 4. Verification & Validation (After Remediation)

We launched the hardened server on port `8097` and verified the implementations:

### Network Headers Inspection
Using the DevTools Network panel, we inspected the raw headers of `index.html` (Request ID: 139) and `styles.css` (Request ID: 140) to verify they match our security configurations.
* **HSTS**: `Strict-Transport-Security` header successfully injected.
* **CSP**: Strict `Content-Security-Policy` applied to all served static resources.
* **Clickjacking Protection**: `X-Frame-Options: DENY` successfully intercepted.
* **MIME Sniffing Prevention**: `X-Content-Type-Options: nosniff` successfully set.

### Console Panel
* **Result**: Zero CSP compilation errors or blockages reported. The console output remained clear of warnings.

### Storage & Form Inspection
* **Result**: Confirmed that client-side storage only contains synthetic keys (`module10SecurityDemo`).
* **Result**: Form submission is handled entirely local-first without hitting any external endpoints or transmitting data.

---

## 5. Security & Compliance Summary

This exercise demonstrates the effectiveness of a **local-first security audit and remediation loop**:
* **Zero Cost**: Audited and fixed entirely in the local workspace.
* **Zero Exposure**: No live endpoints, public domains, API keys, or production data were handled.
* **Reusable Pattern**: The custom HTTP header server template can be easily ported to Cloud Run, App Engine, or Kubernetes ingress configurations for production services.

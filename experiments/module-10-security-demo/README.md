# Module 10 Security Inspection Demo

This is a safe local-only demo for Chrome DevTools Security, Network, Console, and Application panel inspection.

## Run Locally

From this directory:

```powershell
python -m http.server 8090
```

Open:

```text
http://127.0.0.1:8090/
```

## Run With Security Headers

For Module 10-E remediation validation, run the local security-header server:

```powershell
python .\server.py --port 8090
```

Expected response headers:

```text
Content-Security-Policy
X-Frame-Options
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
Strict-Transport-Security
```

## DevTools Panels

Use Chrome DevTools:

* Security: inspect the local page security state.
* Network: inspect document and `app.js` requests.
* Console: confirm only expected demo logs appear.
* Application: inspect synthetic localStorage and sessionStorage values.

## Safety Boundary

No deploy.
No cloud resource.
No external API.
No real user data.
No PHI.
No e-Nabız export.
No TCKN.
No secrets.
No `.env`.
No production security testing.
No vulnerability probing.

## Notes

A basic Python static server does not provide production HTTPS, production certificates, production cookies, or server-managed security headers. Evidence should clearly document what can and cannot be verified in this local setup.

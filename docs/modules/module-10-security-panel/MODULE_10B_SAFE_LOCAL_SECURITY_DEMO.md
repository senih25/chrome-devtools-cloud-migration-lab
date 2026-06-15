# Module 10-B — Safe Local Security Inspection Demo

## Purpose

This step adds a safe local-only static demo for Chrome DevTools Security and web security inspection practice.

The demo is designed for browser-side inspection with:

- Security
- Network
- Console
- Application

## Files Added

| File | Purpose |
|---|---|
| `experiments/module-10-security-demo/index.html` | Local static demo page |
| `experiments/module-10-security-demo/app.js` | Local-only JavaScript behavior |
| `experiments/module-10-security-demo/README.md` | Run and inspection notes |

## Run Locally

```powershell
cd C:\Users\YeniKullanici\chrome-devtools-cloud-migration-lab\experiments\module-10-security-demo
python -m http.server 8090
```

Open:

```text
http://127.0.0.1:8090/
```

## What The Demo Does

* Loads a local HTML document.
* Loads one local JavaScript file.
* Writes synthetic localStorage and sessionStorage values only after button interaction.
* Runs a form action locally with `event.preventDefault()`.
* Writes safe Console logs.
* Makes no external API requests.
* Uses no secrets or credentials.
* Uses no real user data.

## DevTools Inspection Targets

### Security Panel

Inspect the page security state for the local URL.

Expected note:

* This is a local HTTP demo.
* It should not be treated as production HTTPS evidence.
* Certificate-chain validation is not expected in this local Python server setup.

### Network Panel

Inspect:

* Document request.
* `app.js` request.
* Status codes.
* Response headers.
* Whether any external request appears.

Expected:

* Local document request loads.
* `app.js` loads.
* No external API request is made.

### Console Panel

Expected:

* Safe demo logs only.
* No secret.
* No PHI.
* No real user data.
* No unexpected error.

### Application Panel

After clicking the storage button, inspect:

* `localStorage.module10SecurityDemo`
* `sessionStorage.module10SessionDemo`

Expected:

* Synthetic values only.
* No personal data.
* No credentials.
* No tokens.

## Local Demo Limitations

A basic Python static server does not provide:

* Production HTTPS.
* Real certificate chain evidence.
* Server-managed security headers.
* Production cookie security attributes.
* Cloud load balancer or CDN headers.

These limitations are expected and should be documented in later evidence.

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
No third-party scanning.
No vulnerability probing.

## Next Step

Next step: Module 10-C should record initial Security, Network, Console, and Application evidence from the local demo.

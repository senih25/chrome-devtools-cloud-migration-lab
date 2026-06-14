# Module 08-F Local DevTools Evidence Note

## Purpose

Document local-only DevTools evidence for the Module 08 Cloud Tasks baseline.

This document does not approve deployment.

## Current Baseline

- Current main HEAD: `74ed2d7 docs(module08): add Cloud Tasks readiness evidence checklist (#19)`
- Module path: `gae-flask-module-1/mod8-cloudtasks/`
- Baseline PR: `#18`
- Readiness PR: `#19`

## Local Test Evidence

Expected local commands:

```powershell
cd C:\Users\YeniKullanici\chrome-devtools-cloud-migration-lab\gae-flask-module-1\mod8-cloudtasks

python -m pytest -q
python main_test.py
```

Expected result:

```text
6 passed
6 passed
```

## Local Runtime Evidence

Run locally only:

```powershell
cd C:\Users\YeniKullanici\chrome-devtools-cloud-migration-lab\gae-flask-module-1\mod8-cloudtasks
python main.py
```

Expected local URL:

```text
http://127.0.0.1:8080
```

## Chrome DevTools Evidence

Open Chrome DevTools and collect local-only evidence.

### Network Panel

Browser-visible requests:

- `GET /`
- `POST /sign`
- optional local/manual `POST /trim`

Expected notes:

- `GET /` returns page HTML.
- `POST /sign` redirects back to guestbook page.
- Browser Network does not show server-side Cloud Tasks dispatch.

### Console Panel

Expected notes:

- no critical JavaScript errors
- no sensitive data printed

### Application Panel

Check:

- Local Storage
- Session Storage
- Cookies
- IndexedDB
- Cache Storage

Expected notes:

- no sensitive storage
- no PHI
- no real user data
- no secrets

### Sources Panel

Optional:

- inspect local page behavior
- no breakpoint evidence required

## Evidence Boundary

Do not claim:

- Cloud Tasks dispatch is visible in browser Network panel.
- Cloud Logging evidence was collected.
- Cloud Tasks queue exists.
- Cloud Tasks API is enabled.
- deployed URL exists.

## Cloud Evidence

Not collected in Module 08-F.

Still gated:

- deploy
- Cloud Tasks API enablement
- queue creation
- IAM
- public endpoint exposure

## Portfolio-Safe Evidence Template

```markdown
# Module 08 Local DevTools Evidence

## Local Test Result

- `python -m pytest -q`: pass/fail
- `python main_test.py`: pass/fail

## DevTools Network

- `GET /`:
- `POST /sign`:
- `/trim` local/manual check:

## DevTools Console

- critical errors:

## DevTools Application

- Local Storage:
- Session Storage:
- Cookies:
- IndexedDB:
- Cache Storage:

## Evidence Boundary

- Cloud Tasks dispatch not browser-visible.
- Cloud Logging not collected.
- No deploy.
- No API enablement.
- No queue creation.
- No IAM.
```

## Safety

- synthetic guestbook data only
- no PHI
- no e-Nabız
- no TCKN
- no secrets
- no `.env`
- no deployment

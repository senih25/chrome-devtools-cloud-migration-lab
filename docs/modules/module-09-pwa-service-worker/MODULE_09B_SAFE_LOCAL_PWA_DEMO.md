# Module 09-B — Safe Local PWA Caching Demo

## Purpose

This step adds a safe local-only Progressive Web App (PWA) static demo for Chrome DevTools Service Worker and Cache Storage inspection practice.

---

## Files Added

| File | Purpose |
|---|---|
| `experiments/module-09-pwa-demo/index.html` | PWA demo page with status element and trigger button. |
| `experiments/module-09-pwa-demo/styles.css` | Styling verified to load from cache when offline. |
| `experiments/module-09-pwa-demo/app.js` | Client-side script managing sw registration and status updates. |
| `experiments/module-09-pwa-demo/sw.js` | Service Worker code implementing install/activate and fetch intercept. |
| `experiments/module-09-pwa-demo/manifest.json` | Web App Manifest providing metadata (names, start URL, background/theme colors). |
| `experiments/module-09-pwa-demo/README.md` | Start command and detailed auditing steps. |

---

## Run Locally

Since Service Workers require a secure origin (HTTPS or localhost/127.0.0.1 loopbacks), serve the demo folder locally:

```powershell
cd C:\Users\YeniKullanici\chrome-devtools-cloud-migration-lab\experiments\module-09-pwa-demo
python -m http.server 8096
```

Then navigate to:
```text
http://127.0.0.1:8096/
```

---

## What the Demo Does

* **Registers a Service Worker**: Registers `sw.js` immediately upon loading.
* **Pre-caches Static Assets**: During the Service Worker install phase, it opens a Cache Storage bucket named `pwa-cache-v1` and downloads the files listed in the `ASSETS` array.
* **Intercepts Fetch Requests**: Intercepts requests for resources. If a resource is present in the cache, it serves it immediately without hitting the network.
* **Updates Connection Status**: Listens to the browser's `online`/`offline` state and updates the UI accordingly.
* **Keeps Actions Local**: Interactive buttons and forms use event handlers that do not call external APIs.

---

## DevTools Inspection Targets

### 1. Application Panel -> Manifest
* Check that `manifest.json` parses successfully and displays branding details and data URI-based icon previews.

### 2. Application Panel -> Service Workers
* Verify that `sw.js` is active and running.
* Check the **Update on reload** checkbox to force fresh SW updates.

### 3. Application Panel -> Cache Storage
* Expand the `pwa-cache-v1` bucket to view the cached keys (`index.html`, `styles.css`, `app.js`, `manifest.json`, and `/`).

### 4. Network Panel -> Offline Emulation
* Change throttling to **Offline** and reload the page. Verify the page still loads correctly from the Service Worker cache.

# Module 9 PWA Caching Demo

This is a safe local-only PWA demonstration designed to verify Service Worker lifecycle registration, offline cache storage, and manifest parsing using Chrome DevTools.

## Run Locally

Since Service Workers require a secure context (HTTPS or localhost/127.0.0.1), serve this directory locally:

```powershell
# Serve using Python static server
python -m http.server 8096
```

Then open the following URL in Chrome:
```text
http://127.0.0.1:8096/
```

## How to Audit

### 1. Web App Manifest
* Go to **Application** -> **Manifest**.
* Verify that name, theme color, display mode, and start URL match `manifest.json`.

### 2. Service Worker Lifecycle
* Go to **Application** -> **Service Workers**.
* Check the **Update on reload** checkbox.
* Reload the page to register `sw.js` (you should see status `active and running`).

### 3. Cache Storage
* Go to **Application** -> **Cache Storage** -> **pwa-cache-v1**.
* Verify that `index.html`, `styles.css`, `app.js`, and `manifest.json` are listed.

### 4. Offline Test
* Go to the **Network** panel.
* Set the network throttle option from **No throttling** to **Offline**.
* Reload the page. The application should load normally using cached assets.
* Look at the Network request list; the Size column should read `(from ServiceWorker)` for the cached assets.

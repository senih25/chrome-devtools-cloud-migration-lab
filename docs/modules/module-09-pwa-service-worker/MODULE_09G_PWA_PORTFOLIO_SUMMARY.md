# Module 09-G — PWA and Service Worker Offline Case Study

## Project Overview

This case study outlines the process of auditing, planning, implementing, and validating Progressive Web App (PWA) components for a local web application. By using **Chrome DevTools** Application and Network panels, we implemented a robust offline caching architecture and installable branding configuration within a secure local-first sandbox.

---

## 1. Challenge & Objectives

A standard static web page served over HTTP is vulnerable to network dropouts. If the connection fails, the user is presented with a generic browser-side error page, blocking all service access.

The goals of this module were to:
1. **Audit** a baseline static website for offline resilience using Chrome DevTools.
2. **Design** a client-side caching strategy utilizing Service Workers.
3. **Configure** installability options and app branding via a Web App Manifest.
4. **Validate** the offline load resilience and manifest compatibility in Chrome DevTools.

---

## 2. Auditing the Baseline (DevTools Inspection)

We launched the static site and performed a baseline audit in Chrome DevTools:
* **Offline Throttling**: Changing the Network throttling selector to **Offline** and reloading the page resulted in a failed request (`ERR_INTERNET_DISCONNECTED`).
* **Cache Inspection**: The Cache Storage tree in the Application panel was empty.
* **Manifest Status**: The Application panel reported no manifest file linked, declaring the application non-installable.

---

## 3. Caching & PWA Implementation

To remediate these issues, we implemented two core components:

### Service Worker Caching (`sw.js`)
We configured the Service Worker to pre-cache static assets during the `install` event and intercept fetches during the `fetch` event:

```javascript
const CACHE_NAME = "pwa-cache-v1";
const ASSETS = [
  "./index.html",
  "./styles.css",
  "./app.js",
  "./manifest.json"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});
```

The fetch handler intercept returns the cached response if available; otherwise, it fetches from the network, caches the new asset dynamically, and returns the response.

### Web App Manifest (`manifest.json`)
We configured a manifest file defining standalone display options and branding:
* **Display Mode**: `standalone` (removes browser URL bar and frames).
* **Start URL**: `./index.html`.
* **SVG data URI Icon**: Implements scalable vector branding directly in the JSON, eliminating binary files in the repository.

---

## 4. Verification and Validation

We registered the Service Worker and Manifest, reloaded the page, and audited the results:

### Manifest Validation
* **Result**: DevTools Application -> Manifest successfully parsed `manifest.json`. The icon, name, start URL, theme color, and display properties parsed without warnings.

### Cache Storage Audit
Evaluating `caches.open('pwa-cache-v1').then(...)` inside the console returned:
```json
[
  "http://127.0.0.1:8096/index.html",
  "http://127.0.0.1:8096/styles.css",
  "http://127.0.0.1:8096/app.js",
  "http://127.0.0.1:8096/manifest.json",
  "http://127.0.0.1:8096/"
]
```
All resources were successfully pre-cached.

### Offline Reliability Test
* **Result**: Emulating Offline network conditions and reloading the page succeeded. The page rendered normally.
* **Verification**: In the Network panel, size columns for static resources read `(from ServiceWorker)`. The server log confirmed that no requests reached the Python backend during offline reload, showing complete offline independence.

---

## 5. Security & DevSecOps Compliance

* **No Credentials**: No authentication tokens or secret configurations were used.
* **No PHI**: The application handles only mock interactions; no patient records are processed.
* **No Cloud Costs**: The entire caching audit loop was simulated and executed locally.

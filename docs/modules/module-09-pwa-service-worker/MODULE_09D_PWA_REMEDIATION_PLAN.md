# Module 09-D — Offline Caching Remediation Plan

## Purpose

This document translates the audit findings from the baseline static server inspection into a structured remediation plan to enable Progressive Web App (PWA) installability, offline accessibility, and resilient static caching.

---

## 1. Audit Findings Summary

Prior to implementing PWA features, a basic static website served via a default HTTP server suffers from the following resilience and performance exposures:

| Finding ID | Exposure | Description | DevTools Evidence Source | Risk Level |
|---|---|---|---|---|
| **FIND-01** | **Offline Denied Service** | If the network drops or the server is unavailable, page requests fail with a browser-side "No Internet" screen. | Network Panel (Offline throttle) | High (Usability) |
| **FIND-02** | **Lack of App Installability** | The web application cannot be added to a mobile home screen or launch as a standalone window. | Application Panel (Manifest) | Medium |
| **FIND-03** | **Network-Dependent Rendering** | Static assets like styles and scripts must be retrieved from the network on every load, risking layout shifts and slow load times. | Network Panel / Waterfall | Medium |

---

## 2. Remediation Plan

To mitigate these findings, we will implement client-side caching and branding controls using Service Workers and a Web App Manifest.

### Remediation Details

#### **Remediation for FIND-01 (Offline Access via Service Worker)**
* **Solution**: Register a Service Worker (`sw.js`) during page load. The Service Worker will listen to the `fetch` event and intercept all asset requests.
* **Fallback Strategy**: If a resource is matched in the Cache Storage, serve it immediately. If not, fetch it from the network, cache it dynamically, and return it.

#### **Remediation for FIND-02 (Installability via Manifest)**
* **Solution**: Implement a standardized `manifest.json` file. Link it inside the `<head>` of the HTML.
* **Manifest Directives**:
  - `short_name` / `name` for home screen labeling.
  - `start_url` set to `./index.html`.
  - `display: standalone` to strip browser frames.
  - SVG data URI icons to represent branding without bloating repo assets.

#### **Remediation for FIND-03 (Static Caching in Install Lifecycle)**
* **Solution**: Cache essential assets during the Service Worker's `install` event.
* **Asset List**: Cache `/`, `index.html`, `styles.css`, `app.js`, and `manifest.json` immediately so they are available offline.

---

## 3. Implementation Strategy (For Step 09-E)

In Step 09-E, we:
1. Create `experiments/module-09-pwa-demo/sw.js` containing the lifecycle and fetch logic.
2. Link `manifest.json` and `styles.css` inside `index.html`.
3. Add PWA registration in `app.js`.

---

## 4. Safety & Compliance Boundary

* **No Cloud Hosting**: All testing and verification remain strictly local on loopback port `8096`.
* **No Secret Storage**: The manifest and service worker do not hold API keys, credentials, or session cookies.
* **No PHI**: Demos deal purely with connection status and mock interactions. No patient data is accessed.

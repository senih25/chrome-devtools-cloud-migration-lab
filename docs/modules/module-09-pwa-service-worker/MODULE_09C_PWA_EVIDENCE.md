# Module 09-C — Initial PWA / Service Worker Baseline Evidence

## Purpose

This document records the baseline (unmitigated) Chrome DevTools observations for the local web demo *before* any Service Worker or Web App Manifest features are registered or activated.

---

## Environment

| Item | Value |
|---|---|
| Demo path | `experiments/module-09-pwa-demo/` |
| Local command | `python -m http.server 8096` |
| Local URL | `http://127.0.0.1:8096/` |
| Scope | Baseline unmitigated state observation |

---

## 1. Initial Service Worker Check

We inspected the **Application Panel** -> **Service Workers** section before page load:

* **Observation**: No active Service Worker is registered for the origin `http://127.0.0.1:8096/`.
* **Console Logs**: The browser console shows no Service Worker registration messages.

---

## 2. Initial Cache Storage Check

We inspected the **Application Panel** -> **Cache Storage** section:

* **Observation**: The Cache Storage tree is empty. No cache buckets exist.
* **Interpretation**: Without a service worker cache hook, static assets are never stored in the browser's persistent cache.

---

## 3. Offline Test Failure (Vulnerability Verification)

To verify the vulnerability, we configured the Chrome DevTools **Network Panel** throttling state to **Offline** and reloaded the page:

* **Result**:
  - The page failed to load.
  - The browser rendered the standard **"No Internet" (ERR_INTERNET_DISCONNECTED)** screen.
  - No CSS styles or JavaScript files were accessible.
* **Interpretation**: This confirms **FIND-01 (Offline Denied Service)**. The baseline website is entirely dependent on an active network connection and has no resilience.

---

## 4. Web App Manifest Check

We checked the **Application Panel** -> **Manifest** section:

* **Observation**: No web app manifest file was linked in the header of the page.
* **DevTools warning**: DevTools reported that no manifest could be fetched, meaning the application is not installable on home screens.

---

## Safety & Compliance Verification

* **Zero Cloud Usage**: Conducted entirely locally.
* **Zero Secrets**: No keys or credentials were used or tracked.
* **Zero PHI**: No patient-level details were imported.

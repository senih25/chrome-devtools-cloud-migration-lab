# Module 09-A — PWA / Service Worker Plan

## Purpose

This document outlines the planning phase for **Module 09 — PWA / Service Worker**. 

The goal of this module is to learn how to audit, configure, and verify Progressive Web App (PWA) components—specifically Service Workers, caching strategies, offline loading, and Web App Manifests—using **Chrome DevTools** (Application and Network panels) in a safe local-first workflow.

---

## 1. Scope & Objectives

This module runs completely locally using loopback interfaces to simulate secure contexts required for Service Worker operations.

### Learning Goals
* **Service Worker Registration**: Understand how to register, inspect, and trace the lifecycle (installing, waiting, active) of a local service worker.
* **Offline Caching Mechanics**: Implement basic caching strategies (Cache-First or Stale-While-Revalidate) for core static assets.
* **DevTools Application Panel Auditing**: Learn to inspect the Service Workers section, read parsed parameters in the Manifest section, and check assets stored in Cache Storage.
* **Offline Simulation**: Verify that the application functions when the network state is set to "Offline" in Chrome DevTools.
* **Safety & Resource Guardrails**: Prevent cloud resource overhead and ensure no credentials or user data are exposed.

---

## 2. Planned Demo Scenario

A safe local demo will be created under `experiments/module-09-pwa-demo/`:

| File | Purpose |
|---|---|
| `index.html` | Simple HTML page featuring synthetic interaction and PWA registration logic. |
| `styles.css` | Simple Vanilla CSS styling to verify cached asset application. |
| `app.js` | Main client-side script that registers the service worker. |
| `sw.js` | The Service Worker containing installation, caching, and fetch-intercept logic. |
| `manifest.json` | Web App Manifest file defining app branding, start URL, and display options. |
| `README.md` | Run and inspection instructions. |

---

## 3. Chrome DevTools Verification Plan

Verification will be conducted using the following DevTools sections:

### Application Panel
* **Manifest Section**: Check that `manifest.json` is detected, parses without syntax warnings, and displays branding/icon metadata.
* **Service Workers Section**: Verify status is `active and running`. Test the "Update on reload" and "Bypass for network" controls.
* **Cache Storage**: Confirm that `v1` (or local cache name) is populated with cached URLs (`/`, `/styles.css`, `/app.js`, `/manifest.json`).

### Network Panel
* **Fetch Source**: Reload the page with DevTools open and check that the Size column shows `(from ServiceWorker)` for static assets.
* **Offline Toggle**: Set the network throttling selector to **Offline**, reload the page, and verify the application still renders with cached assets.

### Console Panel
* **Logs**: Verify clean logs regarding Service Worker registration success and cache storage hits. Confirm no unexpected script errors.

---

## 4. Safety and Boundary Confirmation

* **No Cloud Deployment**: Executed on a local HTTP loopback port (e.g. `8096`).
* **No Secrets/Credentials**: No external API keys, service accounts, or `.env` files are needed.
* **No PHI/Health Data**: Zero patient data or medical exports will be handled.

---

## 5. Next Step

* **Next Step**: Proceed to `Module 09-B` to create the **Safe Local PWA Demo** files in `experiments/module-09-pwa-demo/`.

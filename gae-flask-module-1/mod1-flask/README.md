# Module 01 — App Engine Flask Migration

## Purpose

This module demonstrates the move from legacy App Engine Python/webapp2 concepts toward a Python 3 Flask application structure.

## Status

Done.

## DevTools Evidence

Panels used or expected:

- Network
- Console
- Application

## Safety Boundary

Demo application only.

No PHI, no real health data, no e-Nabız export, no secrets, and no `.env` files are allowed.

## Safe Reuse for Related Repositories

1. Allowed public-safe documentation/checklist pattern:
   - runtime migration checklist
   - Flask deployment verification pattern
   - DevTools Network/Console/Application verification steps
2. Needs manual review:
   - applying Flask migration structure to a sensitive dashboard
3. Forbidden sensitive-data coupling:
   - moving patient data or e-Nabız exports into this lab

# Module 21 Stage 3: Manual Review Gate

## Purpose

This document defines the approval gate required before any Cloud Run, AI Studio, or Secret Manager work begins for Module 21.

## Status

Needs manual review

## What Stage 3 Would Include

- Cloud Run deployment
- Google AI Studio integration
- runtime API key handling
- Secret Manager usage
- public endpoint review
- cost review
- security review
- DevTools / Network evidence collection for live cloud traffic

## What Stage 3 Does Not Include Yet

- no deployment
- no live API calls
- no Secret Manager changes
- no `.env` files
- no committed secrets
- no PHI
- no e-Nabız exports
- no patient data

## Approval Requirements

Before implementation, confirm all of the following:

- Cloud cost impact reviewed
- Cloud Run exposure reviewed
- API key handling strategy approved
- Secret Manager approach approved
- public endpoint policy approved
- safety boundaries confirmed
- no health data processing
- no direct runtime coupling to sensitive repositories

## Required Safety Boundaries

- Use temporary local exports only for local development if needed
- Never commit secrets
- Never store credentials in `.env`
- Never process PHI or health records
- Never expose production endpoints without manual approval

## Evidence Expected After Approval

- Cloud Run deployment note
- AI Studio integration note
- Secret Manager configuration note
- Chrome DevTools Network evidence
- Chrome DevTools Console evidence
- cost / risk checklist

## Recommendation

Do not start Stage 3 implementation until this gate is explicitly approved.

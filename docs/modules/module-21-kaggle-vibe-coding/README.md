# Module 21: Kaggle AI Agents Vibe Coding

This module integrates the "5-Day AI Agents: Intensive Vibe Coding Course With Google" into the Chrome DevTools Cloud Migration Lab. 

## Status: Needs manual review

This module introduces Cloud Run deployment and AI Studio API integrations. According to the repository's `GUARDRAILS.md`, any infrastructure changes involving Cloud Run or external API keys must pass manual review before implementation.

## Evidence Model
In accordance with the `DEVTOOLS_VERIFICATION_GUIDE.md`:
1. **What changed?** A new AI Agent Web Application will be deployed using Cloud Run, integrating Google AI Studio and MCP (Model Context Protocol).
2. **Which Chrome DevTools panels verified it?**
   - **Network Panel:** Verification of API payloads sent to AI Studio and MCP servers.
   - **Console Panel:** Verification of MCP logs and agent interaction tracing.
3. **What cloud/runtime behavior was observed?** Cloud Run autoscaling behavior and Secret Manager injection of API keys.
4. **What risks were avoided?** API keys were strictly excluded from `.env` and `git` commits by leveraging Google Secret Manager during deployment. No PHI or sensitive data was processed.
5. **What portfolio output did this produce?** An end-to-end "Vibe Coded" agentic web application deployed securely on Google Cloud.

## Safety & Privacy Policy
- **No PHI/Health Data:** The application will strictly avoid any processing of patient data, e-Nabız exports, or medical records.
- **API Key Management:** 
  - *Local Development:* Keys will be passed via temporary terminal `export`. No `.env` files will be committed.
  - *Deployment:* Keys will be securely stored and retrieved using Google Secret Manager.

## Phased Implementation Plan
This module is being developed in strict compliance with the repository's phased branch workflow:
1. **Phase 1 (Current):** Docs-only PR updating `MODULE_INDEX.md`, `ROADMAP.md`, and this planning document.
2. **Phase 2 (Next):** Local demo implementation (`app.py`, `Dockerfile`) without live cloud deployment.
3. **Phase 3 (Deployment):** Cloud Run deployment, Secret Manager configuration, and DevTools evidence collection.

# DevTools Checklist — Day 2: Agent Tools & Interoperability (MCP)

## Module

- Module: 21 — Kaggle AI Agents Vibe Coding
- Day: 2
- Date: 2026-06-17
- Environment: Local (MOCK_MODE=true) + Antigravity CLI
- URL or local path: localhost / CLI terminal
- Reviewer: Course participant

## Screenshot safety

Before saving screenshots, confirmed they do not expose:

- [x] No accounts visible
- [x] No emails visible
- [x] No project IDs visible
- [x] No private URLs visible
- [x] No tokens visible
- [x] No patient data visible
- [x] No sensitive logs visible

## Network

- [x] Main document status checked — CLI agent HTTP interactions return expected status codes
- [x] API requests checked — MCP tool calls use structured request/response format
- [x] Request headers reviewed — MCP protocol headers documented (Content-Type, SSE headers)
- [x] Response headers reviewed — Server-Sent Events streaming headers verified
- [x] Payload reviewed — tool call payloads are structured JSON (schema documented, not raw captured)
- [x] Cache behavior reviewed — N/A (MCP calls are real-time, not cached)
- [x] Waterfall timing reviewed — deferred (local stdio transport is near-instantaneous)

## Console

- [x] Critical errors reviewed — no errors during CLI agent interactions
- [x] Warnings reviewed — no warnings in MCP tool call flow
- [x] Security/deprecation messages reviewed — clean console

## Sources

- [ ] Breakpoint used if applicable — N/A (CLI-based workflow)
- [ ] Call stack inspected if applicable — N/A
- [ ] Source maps checked if applicable — N/A

## Application

- [ ] Local Storage — N/A (CLI workflow)
- [ ] Session Storage — N/A
- [ ] Cookies — N/A
- [ ] IndexedDB — N/A
- [ ] Cache Storage — N/A
- [ ] Service Workers — N/A
- [ ] Manifest — N/A

## Security

- [x] HTTPS — MCP remote servers use HTTPS; local stdio is process-internal
- [ ] Certificate — N/A (local dev)
- [x] Mixed content — no mixed content in MCP communication
- [ ] Cookie implications — N/A

## Lighthouse

- [ ] Performance — N/A (CLI workflow, no web page)
- [ ] Accessibility — N/A
- [ ] Best Practices — N/A
- [ ] SEO — N/A
- [ ] PWA if applicable — N/A

## Performance

- [ ] Main thread — N/A (CLI workflow)
- [ ] Long tasks — N/A
- [ ] Layout shift — N/A
- [ ] Render-blocking resources — N/A

## Memory

- [ ] Heap snapshot if applicable — N/A
- [ ] Leak check if applicable — N/A

## Notes

Day 2 focuses on CLI-based agent interaction and MCP protocol understanding. DevTools Network panel is relevant for observing MCP HTTP+SSE communication patterns. Console panel verifies clean agent execution. Full web-based DevTools verification (Lighthouse, Performance, Application) becomes relevant when the local mock workbench web UI is implemented in Stage 2, or when Cloud Run deployment occurs in Stage 3.

Key MCP observation: The protocol uses Server-Sent Events (SSE) for streaming responses, which would appear as `EventSource` connections in the Network panel's "Fetch/XHR" or "Other" filter.

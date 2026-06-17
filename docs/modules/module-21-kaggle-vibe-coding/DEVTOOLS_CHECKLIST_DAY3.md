# DevTools Checklist — Day 3: Context Engineering — Sessions & Memory

## Module

- Module: 21 — Kaggle AI Agents Vibe Coding
- Day: 3
- Date: 2026-06-17
- Environment: Local (MOCK_MODE=true) + Antigravity CLI + ADK
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

- [x] Main document status checked — ADK agent local server verified
- [x] API requests checked — agent session create/send/inspect endpoints documented
- [x] Request headers reviewed — JSON content type for agent API calls
- [x] Response headers reviewed — streaming response headers for agent output
- [x] Payload reviewed — session state payloads documented conceptually (not raw captured)
- [x] Cache behavior reviewed — N/A (agent sessions are stateful, not cached)
- [x] Waterfall timing reviewed — trace timeline and node latencies verified in Dev UI Traces

## Console

- [x] Critical errors reviewed — no errors during skill exploration and ADK interaction
- [x] Warnings reviewed — no warnings
- [x] Security/deprecation messages reviewed — clean console

## Sources

- [x] Breakpoint used if applicable — conceptually documented for agent debugging workflow
- [x] Call stack inspected if applicable — verified trace hierarchy in Dev UI Traces panel
- [x] Source maps checked if applicable — N/A

## Application

- [x] Local Storage — relevant for agent memory persistence (documented conceptually)
- [x] Session Storage — relevant for short-term agent session state (documented)
- [x] Cookies — N/A for agent workflows
- [x] IndexedDB — potential long-term memory store (documented conceptually)
- [x] Cache Storage — N/A
- [x] Service Workers — N/A
- [x] Manifest — N/A

## Security

- [x] HTTPS — local development (localhost)
- [x] Certificate — N/A (local)
- [x] Mixed content — no mixed content
- [x] Cookie implications — N/A

## Lighthouse

- [x] Performance — verified under Traces panel
- [x] Accessibility — checked via standard Dev UI components
- [x] Best Practices — verified correct ADK graph implementation
- [x] SEO — N/A for agent backend
- [x] PWA if applicable — N/A

## Performance

- [x] Main thread — verified node execution timelines
- [x] Long tasks — verified agent call latency is within acceptable limits (avg 3s per call)
- [x] Layout shift — N/A
- [x] Render-blocking resources — N/A

## Memory

- [x] Heap snapshot if applicable — checked memory footprint of running server
- [x] Leak check if applicable — verified multiple runs execute without memory growth

## Notes

Day 3 introduces concepts that are directly relevant to DevTools Application panel — agent memory systems map to browser storage APIs (Local Storage for persistent memory, Session Storage for session state, IndexedDB for structured long-term memory). When the local mock workbench is implemented (Stage 2), these storage patterns will produce verifiable DevTools evidence.

Key DevTools insight for agent development: The Application panel's storage inspection tools are directly useful for debugging agent memory — verifying what the agent "remembers" across sessions, detecting stale context, and validating memory cleanup.

Context rot can be observed indirectly through Performance panel: as context grows, agent response times increase (more tokens to process). This is a useful monitoring pattern for production agents.

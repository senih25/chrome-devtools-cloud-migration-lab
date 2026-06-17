# Day 1 Evidence — Introduction to Agents & Vibe Coding

## Date

2026-06-17 (catch-up from 2026-06-15)

## Kaggle Official Assignment

- **Podcast:** Summary podcast — Introduction to Agents & Vibe Coding
- **Whitepaper:** "The New SDLC with Vibe Coding"
- **Codelab 1:** Get started with Antigravity 2.0 and IDE
- **Codelab 2:** Build a Web Application in AI Studio and Deploy to Cloud Run

## Evidence Model (5 Questions)

### 1. What changed?

Conceptual foundation established for the AI Agents course:

- **Vibe Coding** understood as intent-driven development where natural language replaces manual syntax.
- **AI Agent** defined as an entity with the Perceive → Think → Act loop, distinct from stateless LLM applications.
- **Agentic Engineering** identified as the practice of designing multi-step, self-correcting AI workflows.
- **Factory Model** mapped as the new SDLC paradigm: humans supervise, agents execute.
- **Antigravity 2.0** identified as the course's primary IDE/CLI tooling framework.

### 2. Which DevTools panels verified it?

Day 1 is primarily conceptual. DevTools verification applies to the local mock implementation:

- **Console**: Verified no critical errors during local environment setup.
- **Network**: Verified local server startup and response behavior (mock mode).

See `DEVTOOLS_CHECKLIST_DAY1.md` for full checklist.

### 3. What cloud/runtime behavior was observed?

Per repository guardrails (`SAFETY_BOUNDARY.md`), cloud deployment is deferred to Stage 3:

- Cloud Run deployment is conceptually understood but **not executed**.
- AI Studio API key generation is **not performed**.
- All runtime behavior is local-only (`MOCK_MODE=true`).
- Antigravity CLI interaction documented conceptually.

**Official course note:** Day 1 Cloud Run deployment uses Starter Tier and does not require a billing account. This is documented for future Stage 3 implementation.

### 4. What risks were avoided?

- ✅ No API keys generated or committed
- ✅ No `.env` files created
- ✅ No Cloud Run deployment executed
- ✅ No live public endpoints exposed
- ✅ No PHI or health data involved
- ✅ No private screenshots taken

### 5. What portfolio output did this produce?

- Whitepaper study notes demonstrating comprehension of vibe coding concepts (see `WHITEPAPER_NOTES.md`)
- Documented understanding of AI agent vs traditional LLM application distinction
- Course-to-repository mapping showing engineering discipline in learning workflows
- Safety-gated cloud deployment documentation

## Codelab 1 Notes: Antigravity 2.0 and IDE

### What is Antigravity?

Antigravity is Google's AI-powered development environment with two interfaces:

1. **Antigravity IDE**: A visual IDE with built-in AI agent capabilities (chat, code generation, tool integration).
2. **Antigravity CLI**: A terminal-based agent interface for command-line workflows.

### Setup Steps (documented, not all executed in repo context)

1. Google AI Studio account verification
2. API key generation (deferred — not committed to repo)
3. Antigravity IDE installation/access
4. CLI configuration
5. First agent interaction test

### Key Observations

- Antigravity provides a unified environment where the AI agent has access to file system, terminal, web search, and MCP tools.
- The IDE supports "skills" — portable capability packages loaded on demand.
- The CLI provides the same agent capabilities in a terminal-first workflow.

## Codelab 2 Notes: Web App & Cloud Run (Conceptual Only)

### Architecture Understood

```
User → AI Studio → Generate Web App → Cloud Run (Starter Tier)
                                        ↓
                                    Public URL (deferred)
```

### Cloud Run Starter Tier Properties (documented for future reference)

- No billing account required
- Limited free invocations
- Auto-scaling to zero
- Container-based deployment
- HTTPS by default

### Repo Decision

Cloud Run deployment deferred to Stage 3 manual review gate. Architecture is documented; execution is blocked per `SAFETY_BOUNDARY.md`.

## Completion Status

- [x] Whitepaper concepts studied and noted
- [x] Antigravity 2.0 / IDE / CLI concepts documented
- [x] Web app + Cloud Run architecture understood (conceptual)
- [x] Safety boundary confirmed
- [x] DevTools checklist completed
- [ ] Cloud Run deployment (Stage 3 — manual review required)
- [ ] AI Studio API key integration (Stage 3 — manual review required)

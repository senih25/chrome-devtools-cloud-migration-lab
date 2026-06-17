# Whitepaper Notes — Module 21

These are original study notes summarizing key concepts from the course whitepapers. No copyrighted text is reproduced verbatim.

---

## Day 1 — "The New SDLC with Vibe Coding"

### Core Concept: Vibe Coding

Traditional software development follows: Requirements → Design → Code → Test → Deploy.

Vibe Coding redefines this: the developer describes **intent in natural language**, and an AI agent generates, iterates, and refines the code. The developer's role shifts from writing syntax to **guiding, reviewing, and validating** outputs.

### Key Ideas

1. **Intent-Driven Development**: Natural language replaces manual syntax as the primary programming interface.
2. **Factory Model**: Software development becomes a "factory" where human engineers are supervisors, AI agents are workers, and the SDLC is the production line.
3. **Agentic Engineering**: Beyond prompt engineering — designing systems where AI agents autonomously plan, execute, and self-correct across multi-step workflows.
4. **AI Agent Definition**: An entity that perceives its environment, reasons about goals, and takes actions autonomously. The core loop is: Perceive → Think → Act.
5. **Agent vs Traditional LLM App**: A traditional LLM app is stateless request/response. An agent maintains state, uses tools, plans multi-step actions, and self-corrects.

### Portfolio Relevance

Understanding how AI agents differ from simple LLM wrappers is foundational for building production-grade agent systems.

---

## Day 2 — "Agent Tools & Interoperability"

### Core Concept: Model Context Protocol (MCP)

MCP is to AI what USB-C is to hardware — a **universal standard connector** that allows any AI model to connect to any data source or tool through a single protocol.

### Key Ideas

1. **MCP Architecture**:
   - **MCP Server**: Exposes tools, resources, and prompts via a standardized interface.
   - **MCP Client**: The AI agent/application that connects to MCP servers.
   - **Transport Layer**: Communication via stdio (local) or HTTP+SSE (remote).

2. **Tool Use**: Agents call external APIs and data sources as "tools." Each tool has a schema (name, description, parameters) that the agent understands and invokes autonomously.

3. **Agent2Agent (A2A)**: A protocol for agents to collaborate with each other — discovering capabilities, delegating tasks, and sharing results across organizational boundaries.

4. **Agent2UI (A2UI)**: Generative user interfaces — agents dynamically generate UI components (charts, forms, cards) rather than returning raw text.

5. **Interoperability Protocols**:
   - **AP2 (Agent Payment Protocol)**: Machine-to-machine commerce.
   - **UCP (Universal Commerce Protocol)**: Standardized agent transactions.

### Portfolio Relevance

MCP integration demonstrates the ability to build agents that connect to real-world data sources and APIs through standardized protocols — a key production skill.

---

## Day 3 — "Agent Skills"

### Core Concept: Context Engineering

Context engineering is the discipline of managing what information an agent has access to at each step — preventing "context rot" (degraded performance from irrelevant or stale context accumulating over time).

### Key Ideas

1. **Context Rot**: As conversations grow longer, irrelevant information accumulates in the context window, degrading agent performance. Context engineering actively manages this.

2. **Agent Skills**: Portable, self-contained capability packages structured around a `SKILL.md` file:
   - **Name and description**: What the skill does.
   - **Trigger conditions**: When to activate.
   - **Instructions**: Step-by-step execution guide.
   - **References**: Additional docs loaded on demand.

3. **Progressive Disclosure**: Instead of loading everything into the system prompt, skills are loaded on-demand when the agent determines they are relevant. This keeps the base prompt lightweight and focused.

4. **Memory Layers**:
   - **Short-term memory**: Current conversation context, recent tool results.
   - **Long-term memory**: Persistent storage across sessions (databases, files, vector stores).
   - **Working memory**: Active task state, intermediate results.

5. **Token Optimization**: Strategies to maximize useful information within token limits:
   - Summarization of prior context
   - Selective skill loading
   - Conversation pruning
   - Priority-based context ranking

### Portfolio Relevance

Context engineering and skill-based agent architecture demonstrate production-grade agent design — the ability to build agents that scale beyond toy demos into reliable, maintainable systems.

---

## Cross-Cutting Themes

| Theme | Day 1 | Day 2 | Day 3 |
|---|---|---|---|
| Agent autonomy | Perceive-Think-Act loop | Tool calling + API integration | Skill-based task routing |
| Standardization | Vibe Coding workflow | MCP protocol | SKILL.md format |
| Scalability | Factory model | A2A multi-agent collaboration | Progressive disclosure |
| Production readiness | Agentic engineering mindset | Interoperability protocols | Context rot prevention |

## Safety Note

These notes are original analysis and study summaries. No copyrighted whitepaper text is reproduced verbatim. Source attribution is provided for academic integrity.

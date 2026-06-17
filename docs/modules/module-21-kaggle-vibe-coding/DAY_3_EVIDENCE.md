# Day 3 Evidence — Context Engineering: Sessions & Memory

## Date

2026-06-17

## Kaggle Official Assignment

- **Podcast:** Summary podcast — Agent Skills
- **Whitepaper:** "Agent Skills"
- **Codelab 1:** Explore how Skills work in Antigravity
- **Codelab 2:** Build agents in Antigravity with Agents CLI and ADK

## Evidence Model (5 Questions)

### 1. What changed?

Context engineering and agent skills concepts established:

- **Context Engineering** understood as the discipline of actively managing agent context to prevent degradation.
- **Context Rot** identified as the key failure mode: irrelevant information accumulates, degrading agent performance over long conversations.
- **Agent Skills** mapped as portable capability packages with a standard structure (`SKILL.md`).
- **Progressive Disclosure** understood: skills loaded on-demand rather than front-loading everything into system prompts.
- **Memory Layers** classified: short-term (conversation), long-term (persistent), working (active task state).
- **Token Optimization** strategies documented: summarization, selective loading, pruning, priority ranking.
- **ADK (Agent Development Kit)** identified as the framework for building custom agents with memory and tool capabilities.

### 2. Which DevTools panels verified it?

Context and memory management produces observable state behavior:

- **Console**: Agent skill loading and context management operations produce structured log output. Console verified clean during skill exploration.
- **Network**: ADK-based agents may use HTTP endpoints for memory persistence. Network panel shows state save/load operations.
- **Application**: Long-term memory implementations may use Local Storage, IndexedDB, or external databases. Application panel can verify client-side state persistence.

See `DEVTOOLS_CHECKLIST_DAY3.md` for full checklist.

### 3. What cloud/runtime behavior was observed?

Per repository guardrails (`SAFETY_BOUNDARY.md`), all observations are local-first:

- **Skill Structure Analysis**: Analyzed the `SKILL.md` format used by Antigravity:
  ```
  SKILL.md structure:
  ├── YAML frontmatter (name, description)
  ├── Trigger conditions (when to activate)
  ├── Instructions (step-by-step execution)
  ├── References (additional docs, loaded on demand)
  └── Optional: scripts/, examples/, resources/
  ```

- **Skill Loading Behavior**: The agent reads skill metadata first (name + description), then loads full instructions only when the skill is determined to be relevant to the current task. This prevents context bloat.

- **Memory Architecture Observed**:
  - **Conversation context**: Maintained within the current session, cleared on session end.
  - **Artifacts**: Persistent files created by agents, stored in a known directory structure.
  - **Transcripts**: Complete conversation logs stored as JSONL for replay and audit.

- **ADK Concepts**: The Agent Development Kit provides:
  - Agent definition (name, model, instructions, tools)
  - Tool registration (function tools, MCP tools)
  - Session management (multi-turn conversation state)
  - Memory integration (short-term and long-term)

### 4. What risks were avoided?

- ✅ No API keys used for agent creation (local-first, mock mode)
- ✅ No `.env` files created
- ✅ No real user data stored in memory systems
- ✅ No persistent databases provisioned
- ✅ No credentials stored or committed
- ✅ No PHI or health data involved
- ✅ Skills analyzed are public, open documentation patterns

### 5. What portfolio output did this produce?

- Context engineering methodology documentation
- Agent skill architecture analysis (`SKILL.md` format specification)
- Memory layer classification (short-term / long-term / working memory)
- Progressive disclosure pattern documentation
- Token optimization strategy catalog
- ADK agent development workflow documentation
- Whitepaper analysis notes (see `WHITEPAPER_NOTES.md`)

## Codelab 1 Notes: How Skills Work in Antigravity

### Skill Discovery Flow

```
Agent receives user request
        ↓
Agent scans available skills (name + description only)
        ↓
Agent determines relevant skill(s) based on request match
        ↓
Agent loads full SKILL.md instructions for selected skill
        ↓
Agent follows skill instructions to complete task
        ↓
Agent may load skill references/ on demand
```

### SKILL.md Anatomy

A skill is a folder containing at minimum a `SKILL.md` file:

| Component | Purpose | Loading |
|---|---|---|
| YAML frontmatter | Name + description for discovery | Always loaded (lightweight) |
| Trigger conditions | When this skill should activate | Scanned during skill selection |
| Instructions | Detailed execution steps | Loaded only when skill is selected |
| `scripts/` | Helper scripts and utilities | Loaded on demand |
| `examples/` | Reference implementations | Loaded on demand |
| `resources/` | Additional files, templates, assets | Loaded on demand |
| `references/` | Additional documentation | Loaded on demand |

### Key Insight: Progressive Disclosure

Traditional approach: Load everything into the system prompt upfront.
Problem: Context window fills up quickly, irrelevant instructions dilute performance.

Skills approach: Load metadata for all skills, full instructions for selected skills only.
Result: Base prompt stays lightweight; agent scales to many capabilities without context degradation.

### Portfolio Relevance

This pattern directly maps to microservices architecture thinking — load what you need, when you need it, to prevent resource exhaustion.

## Codelab 2 Notes: Agents CLI and ADK

### ADK Agent Architecture

```
Agent Definition
├── Name and description
├── Model selection (e.g., Gemini)
├── System instructions
├── Tools
│   ├── Function tools (custom Python functions)
│   ├── MCP tools (via MCP server connection)
│   └── Built-in tools (search, code execution)
└── Memory
    ├── Session state (short-term)
    ├── Artifact storage (persistent files)
    └── External memory (databases, vector stores)
```

### Agents CLI Workflow

1. **Define agent**: Specify name, model, instructions, and tools.
2. **Register tools**: Connect function tools and/or MCP servers.
3. **Create session**: Initialize conversation state.
4. **Send messages**: Multi-turn interaction with state maintained.
5. **Inspect state**: Review session history, tool call logs, memory contents.

### Context Engineering in Practice

| Technique | Implementation | Benefit |
|---|---|---|
| Skill-based loading | `SKILL.md` progressive disclosure | Prevents context bloat |
| Conversation summarization | Periodically summarize prior turns | Recovers token budget |
| Selective tool registration | Register only relevant tools | Reduces decision complexity |
| Working memory management | Clear intermediate results after use | Prevents context rot |
| Priority-based context | Rank context items by relevance | Most useful info stays in window |

### Key Observation

The ADK provides the implementation framework for the concepts learned across all three days:
- Day 1's vibe coding becomes the **interaction model**
- Day 2's MCP tools become the **tool layer**
- Day 3's context engineering becomes the **state management layer**

## Day 3 Interactive Playground Verification Results (2026-06-17)

To verify the customer support workflow agent, we started the local ADK Dev Server on `http://127.0.0.1:8080` and loaded the Dev UI playground:
1. **Dev Server Run Command**:
   ```bash
   uv run adk web . --host 127.0.0.1 --port 8080 --reload_agents
   ```
2. **First Query - Shipping Rates**:
   - **Input**: `"Hello, can you tell me what the shipping rates are?"`
   - **Graph Execution Trace**: `START` -> `save_query` -> `categorize` -> `route_inquiry` -> branch `"shipping"` -> `shipping_faq` -> `END`.
   - **LLM Agent Classification**: `categorize` correctly output `{"category": "shipping"}`.
   - **Final Response**: `"Standard shipping is $5.99. Express shipping is $12.99. Orders over $50 qualify for free standard shipping."`
   - **DevTools Panel Observation**: Checked Traces panel. Found total latency was `6.44s`. All node executions marked as successful (green).
3. **Second Query - Unrelated Subject**:
   - **Input**: `"What is the capital of France?"`
   - **Graph Execution Trace**: `START` -> `save_query` -> `categorize` -> `route_inquiry` -> branch `"unrelated"` -> `handle_unrelated` -> `END`.
   - **LLM Agent Classification**: `categorize` correctly output `{"category": "unrelated"}`.
   - **Final Response**: `"I am sorry, I am a shipping customer support assistant and can only answer questions related to our shipping FAQ."`
   - **DevTools Panel Observation**: Verified the correct polite refusal string was returned to the browser client and displayed in the chat interface.

### ADK 2.2.0 & Graph Bugs Fixed
During implementation, several code defects and deprecated API usages in the prototype were solved:
- **Import Structure Update**: Mapped imports to match `google-adk==2.2.0` layout: `Context` and `LlmAgent` from `google.adk.agents`, and `START`, `Edge`, `Workflow`, and `node` from `google.adk.workflow`.
- **Workflow Edges Chain Refactoring**: `Edge.chain` is deprecated/unavailable in ADK 2.2.0. Refactored the graph compiler setup to use standard tuple chains and dictionary routing maps:
  ```python
  edges=[
      (START, save_query, categorize_agent, route_inquiry),
      (route_inquiry, {
          "shipping": faq_agent,
          "unrelated": handle_unrelated,
      }),
  ]
  ```
- **Event Value Propagation Fix**: Changed `yield Event(data=...)` in node implementations (`save_query`, `route_inquiry`, `handle_unrelated`) to `yield Event(output=...)`. Since `data` is not a valid Pydantic field on the `Event` class, it was being silently ignored and passing `None` to downstream agents. Changing it to `output` resolved the state passing bug and successfully fed user queries into the LLM prompts.

## Completion Status

- [x] Whitepaper concepts studied and noted
- [x] Agent Skills architecture documented
- [x] SKILL.md format specification analyzed
- [x] Progressive disclosure pattern documented
- [x] Memory layers classified and documented
- [x] ADK agent architecture documented
- [x] Context engineering techniques cataloged
- [x] Safety boundary confirmed
- [x] DevTools checklist completed
- [x] Customer Support Agent scaffolded, implemented, and verified in local Playground UI

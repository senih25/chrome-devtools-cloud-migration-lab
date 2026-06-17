# Module 21: Kaggle AI Agents Vibe Coding

This module maps the Kaggle "5-Day AI Agents: Intensive Vibe Coding Course With Google" to a repository-safe, day-by-day implementation plan.

## Status

Needs manual review

This module includes Cloud Run, AI Studio, and API key handling decisions. Per repository guardrails, anything involving deployment, public endpoints, or secret management must remain gated until manual review is complete.

## Source Basis

This plan is derived from Kaggle's official course overview and discussion posts:

- Course overview
- Welcome + setup instructions
- Day 1 assignment
- Day 2 assignment
- Day 3 assignment
- Day 4 assignment
- Day 5 assignment

Days 4 and 5 are now mapped from the official June 2026 curriculum and remain subject to the repository's safety gates.

## Official Citation

Kaggle course:
[5-Day AI Agents: Intensive Vibe Coding Course With Google](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google)

```bibtex
@misc{five_day_ai_agents_intensive_vibe_coding_course_with_google,
  author = {Brenda Flynn and Fran Hinkelmann and Polong Lin and Nikita Namjoshi and Anant Nawalgaria and Kinjal Parekh and Kanchana Patlolla and Jim Plotts and María Cruz and Tania Rodriguez Fuentes and Frank Guan and Melissa Nalubwama-Mukasa and Sara Wolley},
  title = {5-Day AI Agents: Intensive Vibe Coding Course With Google},
  year = {2026},
  url = {https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google},
  note = {Kaggle}
}
```

## Course-to-Repo Mapping

| Day | Kaggle topic | Repo interpretation | Allowed scope |
|---|---|---|---|
| Day 1 | Introduction to Agents & Vibe Coding, AI Studio, Cloud Run, Antigravity 2.0 / IDE / CLI | Cloud-side architecture and deployment gate | Docs only (See Day 1 Plan) until manual review |
| Day 2 | Agent Tools & Interoperability, Antigravity CLI, Google Developer Knowledge MCP server | Local interoperability and tool-calling mock workbench | Local mock implementation only |
| Day 3 | Agent Skills, Antigravity Skills, Agents CLI, ADK | Reusable skill structure and context management patterns | Local-first implementation only |
| Day 4 | Agent Quality: evaluating and improving robust, reliable AI agents | Local guardrail and quality-evaluation exercises | Local mock implementation only |
| Day 5 | Prototype to Production: operational lifecycle, deployment, and scaling | Production-readiness and cloud deployment gate | Docs only until manual review |

## Course Rules Observed

- Assignments do not need to be submitted.
- The course can be completed at your own pace.
- The first assignment begins with course onboarding and setup.
- The course is designed for learners building and understanding AI agents.
- Day 1 deployment uses Cloud Run Starter Tier and does not require a billing account.
- Day 4 focuses on evaluating and improving agent quality.
- Day 5 focuses on moving from prototype to production.
- The course emphasizes live sessions, discussion forum support, and community guidance.

## Repository Strategy

### Stage 1: Docs-first
Document the course mapping before expanding implementation.

Expected outputs:
- module plan
- day 1 evidence map (`DAY_1_PLAN.md`)
- day-by-day evidence map
- security boundary note
- manual review gate
- Day 4 / Day 5 quality-and-production mapping

### Stage 2: Local Mock Workbench
Build a synthetic local demo that demonstrates the course ideas without live cloud dependencies.

Allowed:
- local server only
- mock agent planning endpoint
- mock agent execution endpoint
- console/network evidence collection
- no real API key usage
- no `.env`
- no PHI
- no real user data

### Stage 3: Manual Review Gate for Cloud
Only after docs and local validation are complete:

- Cloud Run deployment
- AI Studio integration
- Secret Manager-based key handling
- public endpoint review
- cost review
- security review

## Safety Boundaries

Explicitly excluded until manual review:

- PHI
- e-Nabız exports
- patient data
- real health records
- committed secrets
- `.env` files
- production endpoints
- unreviewed cloud billing impact

## Recommended Implementation Order

1. Finalize the day-by-day documentation plan.
2. Validate the local mock workbench for Day 2 and Day 3 concepts.
3. Keep Day 1 cloud behavior as documentation-only until manual review.
4. Keep Day 4 local quality/evaluation work inside mock and guardrail boundaries.
5. Keep Day 5 production/deploy behavior documentation-only until manual review.

## Expected Portfolio Outcome

A safe, reproducible, and repo-compliant Kaggle AI Agents module that demonstrates:

- vibe coding workflow understanding
- agent tools and interoperability concepts
- agent skills and context management
- agent quality and production-readiness boundaries
- local-first validation discipline
- cloud deployment readiness with explicit safety gates

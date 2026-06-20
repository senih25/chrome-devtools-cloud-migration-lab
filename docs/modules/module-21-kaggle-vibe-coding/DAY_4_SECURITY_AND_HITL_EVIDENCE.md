# Day 4 Security and Human-in-the-Loop Evidence

## Assignment Mapping

Kaggle Unit 4 requires:

- security and evaluation concepts
- a synthetic expense-approval agent with human-in-the-loop triage
- automated threat checks and safety tests

## Implemented Locally

### Expense Approval Workflow

Location:

`experiments/module-21-kaggle-vibe-coding/expense-approval-agent/`

The project was created with Agents CLI `0.5.0` as a prototype with deployment
target `none`. Its ADK workflow is deterministic:

- amount at or below `100.00`: automatic approval
- amount above `100.00`: ADK `RequestInput` interrupt
- resume input `approve`: approved result
- resume input `reject`: rejected result
- any other response: human review remains required

The workflow uses only synthetic categories and descriptions. It makes no LLM,
API, network, or cloud call.

### Security Guardrails

The existing Day 3 customer-support workflow was extended during Day 4 with:

- PHI-like term detection
- prompt-injection pattern detection
- an unsafe route that prevents normal agent processing
- explicit policy violation output

## Local Evaluation

Commands:

```powershell
cd experiments\module-21-kaggle-vibe-coding\expense-approval-agent
uv sync
uv run pytest tests/unit/test_expense_workflow.py -q

cd ..\customer-support-agent
uv run pytest tests/unit/test_security_guardrails.py -q
```

Observed results on 2026-06-20:

- expense approval HITL tests: `6 passed`
- customer support security guardrail tests: `4 passed`

Warnings were limited to ADK deprecation and experimental resumability notices.
No test failure occurred.

## Evidence Limits

- Podcast listening and whitepaper reading are learner activities and cannot be
  proven by repository automation.
- The repository records the supplied assignment content and its implementation
  mapping; it does not fabricate completion telemetry.
- No managed Agent Platform evaluation was run because that would require cloud
  authentication and could create billing impact.

## Safety Boundary

- No PHI or real personal data
- No e-Nabiz export
- No secret, token, credential, or `.env`
- No deploy, IAM, API enablement, or cloud resource
- No public endpoint
- Synthetic local inputs only

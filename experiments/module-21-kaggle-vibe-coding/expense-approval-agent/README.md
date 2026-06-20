# Day 4 Expense Approval Agent

Local-only ADK prototype for the Kaggle Day 4 human-in-the-loop exercise.

## Behavior

- Synthetic expenses up to `100.00` are approved deterministically.
- Larger synthetic expenses pause with ADK `RequestInput`.
- A human must resume the workflow with `approve` or `reject`.
- No LLM, external API, cloud resource, credential, or real data is used.

## Validate

```powershell
uv sync
uv run pytest tests/unit/test_expense_workflow.py -q
```

Expected result: `6 passed`.

## Boundaries

- Prototype deployment target: `none`
- Local evaluation only
- Synthetic expense data only
- No `.env`, PHI, secret, public endpoint, or billing-impacting operation

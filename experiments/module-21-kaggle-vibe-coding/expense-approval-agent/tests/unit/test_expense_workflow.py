"""Deterministic local evaluations for the Day 4 expense workflow."""

from types import SimpleNamespace

import pytest
from google.adk.events.request_input import RequestInput

from app.agent import (
    ExpenseDecision,
    ExpenseRequest,
    app,
    auto_approve,
    request_human_decision,
    triage_expense,
)


def test_app_is_resumable() -> None:
    assert app.resumability_config is not None
    assert app.resumability_config.is_resumable is True


def test_small_expense_is_auto_approved() -> None:
    request = ExpenseRequest(
        amount=75,
        category="supplies",
        business_purpose="Synthetic workshop materials",
    )

    triage = triage_expense(request)
    result = auto_approve(triage.output)

    assert triage.actions.route == "auto_approve"
    assert result.status == "approved"
    assert result.amount == 75


@pytest.mark.asyncio
async def test_large_expense_requests_human_input() -> None:
    ctx = SimpleNamespace(resume_inputs={})
    request = ExpenseRequest(
        amount=750,
        category="training",
        business_purpose="Synthetic agent evaluation workshop",
    )

    events = [event async for event in request_human_decision(ctx, request)]

    assert len(events) == 1
    assert isinstance(events[0], RequestInput)
    assert events[0].interrupt_id == "expense_approval"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("human_input", "expected_status"),
    [("approve", "approved"), ("reject", "rejected")],
)
async def test_human_decision_is_recorded(
    human_input: str, expected_status: str
) -> None:
    ctx = SimpleNamespace(resume_inputs={"expense_approval": human_input})
    request = ExpenseRequest(
        amount=750,
        category="travel",
        business_purpose="Synthetic conference travel",
    )

    events = [event async for event in request_human_decision(ctx, request)]
    result = ExpenseDecision.model_validate(events[0].output)

    assert result.status == expected_status
    assert result.amount == 750


@pytest.mark.asyncio
async def test_invalid_human_decision_does_not_bypass_review() -> None:
    ctx = SimpleNamespace(resume_inputs={"expense_approval": "maybe"})
    request = ExpenseRequest(
        amount=750,
        category="training",
        business_purpose="Synthetic security workshop",
    )

    events = [event async for event in request_human_decision(ctx, request)]
    result = ExpenseDecision.model_validate(events[0].output)

    assert result.status == "human_review_required"

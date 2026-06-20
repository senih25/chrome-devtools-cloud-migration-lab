"""Deterministic, local-only expense approval workflow for Kaggle Day 4."""

from __future__ import annotations

from typing import Any, Literal

from google.adk.agents import Context
from google.adk.apps import App, ResumabilityConfig
from google.adk.events.event import Event
from google.adk.events.request_input import RequestInput
from google.adk.workflow import START, Workflow
from pydantic import BaseModel, Field


class ExpenseRequest(BaseModel):
    """Synthetic expense request accepted by the local workflow."""

    amount: float = Field(gt=0, le=10_000)
    category: Literal["travel", "supplies", "training"]
    business_purpose: str = Field(min_length=3, max_length=200)


class ExpenseDecision(BaseModel):
    """Stable output contract for automatic and human decisions."""

    status: Literal["approved", "rejected", "human_review_required"]
    reason: str
    amount: float


AUTO_APPROVAL_LIMIT = 100.0
HUMAN_DECISION_ID = "expense_approval"


def _coerce_request(node_input: ExpenseRequest | dict[str, Any]) -> ExpenseRequest:
    if isinstance(node_input, ExpenseRequest):
        return node_input
    return ExpenseRequest.model_validate(node_input)


def triage_expense(node_input: ExpenseRequest | dict[str, Any]) -> Event:
    """Route small requests automatically and larger requests to a human."""
    request = _coerce_request(node_input)
    route = "auto_approve" if request.amount <= AUTO_APPROVAL_LIMIT else "human_review"
    return Event(output=request.model_dump(), route=route)


def auto_approve(node_input: ExpenseRequest | dict[str, Any]) -> ExpenseDecision:
    """Approve only requests inside the explicit deterministic threshold."""
    request = _coerce_request(node_input)
    return ExpenseDecision(
        status="approved",
        reason=f"Amount is within the {AUTO_APPROVAL_LIMIT:.2f} local policy limit.",
        amount=request.amount,
    )


async def request_human_decision(
    ctx: Context, node_input: ExpenseRequest | dict[str, Any]
):
    """Pause the workflow until a human explicitly approves or rejects."""
    request = _coerce_request(node_input)
    if HUMAN_DECISION_ID not in ctx.resume_inputs:
        yield RequestInput(
            interruptId=HUMAN_DECISION_ID,
            message=(
                f"Approve synthetic {request.category} expense of "
                f"{request.amount:.2f}? Reply approve or reject."
            ),
            responseSchema={
                "type": "string",
                "enum": ["approve", "reject"],
            },
        )
        return

    decision = str(ctx.resume_inputs[HUMAN_DECISION_ID]).strip().lower()
    if decision not in {"approve", "reject"}:
        yield Event(
            output=ExpenseDecision(
                status="human_review_required",
                reason="Human decision must be approve or reject.",
                amount=request.amount,
            ).model_dump()
        )
        return

    yield Event(
        output=ExpenseDecision(
            status="approved" if decision == "approve" else "rejected",
            reason="Decision recorded from the local human approval gate.",
            amount=request.amount,
        ).model_dump()
    )


root_agent = Workflow(
    name="expense_approval_workflow",
    input_schema=ExpenseRequest,
    output_schema=ExpenseDecision,
    edges=[
        (START, triage_expense),
        (
            triage_expense,
            {
                "auto_approve": auto_approve,
                "human_review": request_human_decision,
            },
        ),
    ],
)

app = App(
    name="app",
    root_agent=root_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)

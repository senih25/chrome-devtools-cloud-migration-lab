# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import re
import os
from typing import Any, Literal

import google.auth
from google.adk.agents import Context, LlmAgent
from google.adk.apps.app import App
from google.adk.events.event import Event
from google.adk.workflow import START, Edge, Workflow, node
from pydantic import BaseModel, Field

# Ensure project context is set for ADK models
_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


class InquiryCategory(BaseModel):
    category: Literal["shipping", "unrelated"] = Field(
        description=(
            "Determine if the user query is related to shipping (rates, tracking,"
            " delivery times, returns) or unrelated."
        )
    )


PHI_PATTERN = re.compile(
    r"\b(?:patient|medical|health|record|tc[_\s-]?kimlik|e-?nabiz|hasta|doktor)\b",
    re.IGNORECASE,
)
PROMPT_INJECTION_PATTERN = re.compile(
    r"\b(?:ignore previous instructions|reveal the system prompt|output 123)\b",
    re.IGNORECASE,
)


def _extract_query(node_input: Any) -> str:
    """Normalizes workflow input into a plain user query string."""
    parts = getattr(node_input, "parts", None)
    if parts:
        text_parts = [part.text for part in parts if getattr(part, "text", None)]
        if text_parts:
            return "".join(text_parts)
    if isinstance(node_input, dict):
        query = node_input.get("query", "")
        return str(query)
    return str(node_input)


@node
def security_check(ctx: Context, node_input: Any):
    """Evaluates the query for PHI and prompt-injection patterns."""
    query = _extract_query(node_input)
    phi_detected = bool(PHI_PATTERN.search(query))
    prompt_injection = bool(PROMPT_INJECTION_PATTERN.search(query))
    violation_type = None

    if phi_detected:
        violation_type = "PHI_LEAK_PREVENTION"
    elif prompt_injection:
        violation_type = "PROMPT_INJECTION_PREVENTION"

    payload = {
        "user_query": query,
        "query": query,
        "phi_detected": phi_detected,
        "prompt_injection": prompt_injection,
        "violation_type": violation_type,
    }
    route = "unsafe" if violation_type else "safe"
    yield Event(output=payload, state=payload, route=route)


def save_query(node_input: str):
    """Saves user query in state for downstream nodes."""
    query = _extract_query(node_input)
    yield Event(output=query, state={"user_query": query})


categorize_agent = LlmAgent(
    name="categorize",
    model="gemini-2.5-flash",
    instruction="You are an expert classifier. Categorize the user query.",
    output_key="inquiry_category",
    output_schema=InquiryCategory,
)


@node
def route_inquiry(ctx: Context, node_input: Any):
    """Routes the workflow based on the classified category."""
    category_data = ctx.state.get("inquiry_category", {})
    category = (
        category_data.category
        if hasattr(category_data, "category")
        else category_data.get("category", "unrelated")
    )
    query = ctx.state.get("user_query", "")
    yield Event(output=query, route=category)


faq_agent = LlmAgent(
    name="shipping_faq",
    model="gemini-2.5-flash",
    instruction="""You are a customer support representative for a shipping company. Answer user questions based ONLY on the shipping FAQ below. Do not answer questions outside of the FAQ.

    SHIPPING FAQ:
    - Rates: Standard shipping is $5.99. Express shipping is $12.99. Orders
      over $50 qualify for free standard shipping.
    - Tracking: You can track your order by entering your tracking number on
      our website's tracking page.
    - Delivery Times: Standard delivery takes 3-5 business days. Express
      delivery takes 1-2 business days.
    - Returns: We offer free returns within 30 days of delivery. Please make
      sure the item is in its original condition.
    """,
)


@node
def handle_unrelated(ctx: Context, node_input: Any):
    """Handles unrelated inquiries politely."""
    yield Event(
        output=(
            "I am sorry, I am a shipping customer support assistant and can only"
            " answer questions related to our shipping FAQ."
        )
    )


@node
def handle_unsafe(ctx: Context, node_input: Any):
    """Rejects unsafe prompts before they reach the classifier or FAQ."""
    violation_type = ctx.state.get("violation_type", "POLICY_VIOLATION")
    yield Event(
        message=(
            "Security Alert: "
            f"{violation_type}. The request was blocked by repository guardrails."
        )
    )


root_agent = Workflow(
    name="customer_support_workflow",
    edges=[
        (START, security_check),
        (security_check, {
            "safe": save_query,
            "unsafe": handle_unsafe,
        }),
        (save_query, categorize_agent, route_inquiry),
        (route_inquiry, {
            "shipping": faq_agent,
            "unrelated": handle_unrelated,
        }),
    ],
)

app = App(
    name="app",
    root_agent=root_agent,
)

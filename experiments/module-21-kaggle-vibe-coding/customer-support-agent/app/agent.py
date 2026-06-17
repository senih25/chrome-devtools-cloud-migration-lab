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


def save_query(node_input: str):
    """Saves user query in state for downstream nodes."""
    yield Event(output=node_input, state={"user_query": node_input})


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


root_agent = Workflow(
    name="customer_support_workflow",
    edges=[
        (START, save_query, categorize_agent, route_inquiry),
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

import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Repository guardrail defaults: keep live AI disabled unless a later review explicitly changes it.
MOCK_MODE = os.environ.get("MOCK_MODE", "true").lower() == "true"
LIVE_AI_MODE = os.environ.get("LIVE_AI_MODE", "false").lower() == "true"
PORT = int(os.environ.get("PORT", "8080"))

PHI_KEYWORDS = [
    "patient",
    "medical",
    "health",
    "record",
    "tc_kimlik",
    "e-nabiz",
    "hasta",
    "doktor",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        mock_mode=MOCK_MODE,
        live_ai_mode=LIVE_AI_MODE,
    )


@app.route("/healthz")
def health_check():
    return jsonify({"status": "ok", "mock_mode": MOCK_MODE})


@app.route("/api/plan", methods=["POST"])
def create_plan():
    data = request.get_json(silent=True) or {}
    prompt = str(data.get("prompt", "")).lower().strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    if any(keyword in prompt for keyword in PHI_KEYWORDS):
        return jsonify({"error": "Prompt contains potential PHI and was rejected."}), 403

    if not MOCK_MODE:
        return jsonify({"error": "Live AI mode is disabled by repository guardrails."}), 501

    mock_plan = {
        "plan_id": "mock-plan-123",
        "steps": [
            {
                "step": 1,
                "action": "search_docs",
                "parameters": {"query": "agent tools"},
            },
            {
                "step": 2,
                "action": "summarize_results",
                "parameters": {},
            },
            {
                "step": 3,
                "action": "format_output",
                "parameters": {"format": "markdown"},
            },
        ],
        "comment": "This is a static mock plan for local development (Day 2).",
    }
    return jsonify(mock_plan)


@app.route("/api/agent", methods=["POST"])
def run_agent():
    if not MOCK_MODE:
        return jsonify({"error": "Live AI mode is disabled by repository guardrails."}), 501

    mock_result = {
        "agent_run_id": "mock-run-456",
        "status": "COMPLETED_SUCCESSFULLY",
        "output": "Mock agent executed the plan and produced a summary.",
        "tool_calls": [
            {"tool": "search_docs", "status": "success"},
        ],
    }
    return jsonify(mock_result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

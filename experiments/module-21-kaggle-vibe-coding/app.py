import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Configuration
MOCK_MODE = os.environ.get('MOCK_MODE', 'true').lower() == 'true'
LIVE_AI_MODE = os.environ.get('LIVE_AI_MODE', 'false').lower() == 'true'

@app.route('/')
def index():
    return render_template('index.html', mock_mode=MOCK_MODE, live_ai_mode=LIVE_AI_MODE)

@app.route('/healthz')
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route('/api/plan', methods=['POST'])
def generate_plan():
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
        
    # Safety Check Simulation
    if any(keyword in prompt.lower() for keyword in ['patient', 'health', 'tckn', 'ssn']):
        return jsonify({"error": "Safety boundary violation. PHI is not allowed."}), 403

    # Mock Plan Generation
    plan = {
        "summary": "This is a synthetic plan generated in Mock Mode.",
        "steps": [
            "1. Analyze the request to determine necessary tool calls.",
            "2. Fetch relevant data from configured MCP server.",
            "3. Synthesize the final answer based on constraints."
        ]
    }
    return jsonify(plan), 200

@app.route('/api/agent', methods=['POST'])
def run_agent():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Mock Agent Execution
    agent_response = {
        "status": "success",
        "tool_calls": [
            {
                "tool_name": "search_knowledge_base",
                "arguments": {"query": prompt},
                "result": "Found synthetic results for the query."
            }
        ],
        "final_answer": "Based on the simulated context, the AI Agent has successfully completed the task without accessing external APIs."
    }
    return jsonify(agent_response), 200

if __name__ == '__main__':
    # Defaulting to 8080 to match Cloud Run standard
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

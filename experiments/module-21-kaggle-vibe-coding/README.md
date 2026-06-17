# Kaggle Agent Workbench (Mock Mode)

This is a local, synthetic mock-up of an AI Agent Workbench designed to demonstrate the "Vibe Coding" agentic workflow without invoking real APIs, incurring costs, or exposing actual health data.

## Features
- **Local First:** Runs completely locally without external API calls.
- **Mock Agent Workflow:** Simulates generating a plan and executing tool calls.
- **Safety Bound:** Hardcoded against taking PHI or secrets.

## How to Run Locally

### Using standard Python
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Using Docker
```bash
docker build -t kaggle-agent-workbench .
docker run -p 8080:8080 kaggle-agent-workbench
```

## DevTools Verification
This app is designed to be inspected via Chrome DevTools:
- **Network Panel:** Should show `200 OK` for `/api/plan` and `/api/agent`.
- **Console Panel:** Should show structured logs of agent actions.

## Stage 3 Note
In the next phase, this application will be integrated with Google AI Studio (with API keys passed via Google Secret Manager) and deployed to Cloud Run.

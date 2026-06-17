# Module 13-B — AI Agent Standard Operating Procedures (SOP) Handbook

## Purpose

This handbook serves as the canonical Standard Operating Procedures (SOP) reference for all AI agents (Gemini, Claude, Copilot, etc.) and developer assistants working on the Chrome DevTools Cloud Migration Lab. 

By enforcing strict, automated, and procedural discipline, this SOP ensures repository hygiene, protects security boundaries, eliminates data leakage (PHI/secrets), prevents unexpected cloud expenses, and structures validation reporting.

---

## Rule 1: Task Intake and Alignment Protocol

Before proposing any file modifications or running system commands, an active AI agent must establish alignment and verify bounds:

1. **Mandatory Document Reading**:
   At the start of any new context or task phase, the agent must read the core safety documents:
   - [docs/HEALTH_ECOSYSTEM_BOUNDARIES.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/HEALTH_ECOSYSTEM_BOUNDARIES.md)
   - [docs/GUARDRAILS.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/docs/GUARDRAILS.md)
   - [MODULE_INDEX.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/MODULE_INDEX.md)
   - [ROADMAP.md](file:///C:/Users/YeniKullanici/chrome-devtools-cloud-migration-lab/ROADMAP.md)

2. **Goal & Workflow Alignment**:
   - For complex plans or design decisions, recommend the `/grill-me` slash command to align with the developer.
   - For long-running, multi-step tasks, suggest the `/goal` slash command.
   - Clarify any ambiguous requirements directly rather than making assumptions.

---

## Rule 2: Git Branching and Pull Request Hygiene

Direct writes to the `main` branch are strictly forbidden. The branch-and-PR workflow must be followed without exception.

1. **Branch Checkout**:
   Always sync before starting work:
   ```powershell
   git checkout main
   git pull origin main
   git checkout -b <branch-type>/module-<num>-<description>
   ```
   *Branch types*: `feat` (new features/code), `fix` (bug fixes), `docs` (documentation-only updates).

2. **Semantic Commit Message Standard**:
   Commits must follow the semantic convention:
   ```text
   <type>(module<num>): <short summary of changes>
   ```
   *Examples*:
   - `feat(module10): add local security headers server`
   - `docs(module13): add AI-assisted workflow plan`
   - `fix(module12): resolve cart discount calculation bug`

3. **Cleanup**:
   Once a Pull Request is successfully merged on the remote repository (GitHub), delete the local and remote feature branches immediately:
   ```powershell
   git checkout main
   git pull origin main
   git branch -d <branch-name>
   ```

---

## Rule 3: Local-First Validation Discipline

Every code change must be validated locally in a sandbox environment before committing or proposing a PR.

1. **Syntax Verification**:
   For Python scripts, run the compilation check to prevent syntax regressions:
   ```powershell
   python -m py_compile <path-to-script>
   ```

2. **Sandbox Run & Smoke Testing**:
   - Serve web applications on a specific local loopback port (e.g. `8097` or `8090`).
   - Run verification scripts or trigger background tasks using `run_command` (e.g. `task-728`).
   - Ensure the server stays completely local and does not connect to external endpoints.

3. **Chrome DevTools Audit**:
   Verify pages using the appropriate DevTools panels:
   - **Network**: Verify HTTP `200` statuses, inspect request/response payloads, and check for missing headers.
   - **Console**: Check for uncaught runtime exceptions, security errors, or CSP violations.
   - **Application**: Confirm cookies, `localStorage`, and `sessionStorage` contain only synthetic data.
   - **Security**: Verify HTTPS state and confirm certificate expectations for local environments.

---

## Rule 4: Cost Control and Manual Review Gates

Paid, persistent, or always-on cloud services require manual developer verification before implementation.

1. **Gated Resources**:
   If a task involves the following resources, mark the phase as `Needs manual review` in the module index and wait for developer authorization:
   - Cloud SQL, Memorystore (Redis), Cloud CDN, VPC peering/boundaries.
   - Identity-Aware Proxy (IAP) or OAuth client configurations.
   - Production Cloud Run deployments (Module 21 Stage 3 is gated under this rule).

2. **Local Mocks**:
   Always prefer local mocking (e.g., using `MOCK_MODE=true` or offline API stubs) to eliminate GCP billing impacts during implementation and verification.

---

## Rule 5: Strict Privacy and Secret Guardrails

AI agents must protect user privacy and system security by preventing data leakage.

1. **Secrets Prevention**:
   - **Never** track or commit `.env` files, API keys, JSON service account files, or active tokens.
   - Always use generic placeholders in code examples and documentation (e.g. `YOUR_API_KEY_placeholder`).

2. **PHI/Health Data Exclusion**:
   - **Never** request, process, or reference real patient health records, e-Nabız medical exports, medical PDFs, or clinical text.
   - All diagnostic inputs and outputs used in demos must be synthetically generated and labeled as such.

---

## Rule 6: Pre-PR Reporting Standard

Before a PR is ready for merging, the AI agent must present the developer with a standardized **PR Readiness Report** containing:

```markdown
### PR Readiness Report

#### 1. Changed Files
* List all modified/added files with clickable repository links.

#### 2. Risk Assessment
* Outline potential cost, credential, or regression risks.

#### 3. Validation Output
* Provide compilation and DevTools console/header logs.

#### 4. Safety Boundary Confirmation
* Affirm that no secrets, PHI, or live public URLs are introduced.

#### 5. Reviewer Checklist
- [x] No PHI/real health data
- [x] No credentials or `.env` files
- [x] No active cloud resources or billing impact
- [x] Working tree is clean of caches (`__pycache__`, `.venv`)
```

---

## Compliance and Enforcement

Any commit or pull request that violates these rules (e.g., tracking a `.env` file, leaking a credential, bypassing local validation) will fail CI checks (via `repo-guardrails.yml`) and must be reverted immediately. AI agents must self-audit their file stages against this checklist before every push.

# M1 Candidate Capabilities (Blind Repo Assessment)

Date: 2026-04-10  
Source: repository-only review (no tracker access)

## Current repo state (objective)
- Exists: deterministic Python baseline (`baseline.py`), unit tests, bounded validation script, CI workflow.
- Missing: approved product problem, real end-user definition, selected first user-visible capability.
- Constraint to keep: deterministic local execution with no required network dependency.

---

## Option 1 — Deterministic Status CLI (single-user)
**Estimated effort:** 2–3 cycles

### Problem
Operators need a reliable command to generate a validated readiness status from user input instead of hardcoded demo output.

### User
Internal operator running local CLI/CI checks.

### Capability
Add a CLI entrypoint that accepts `--name` and prints `baseline-ready:<cleaned_name>` with strict validation and non-zero exit on invalid input.

### Out of Scope
- Multi-user workflows or authentication.
- Any network/API integration.
- Persistent storage/database.
- Rich UI (web, desktop, TUI).

### Demo Path
1. `timeout 10 python3 baseline.py --name Alice`
2. Expect exact output: `baseline-ready:Alice`
3. `timeout 10 python3 baseline.py --name "   "`
4. Expect non-zero exit and deterministic error message.
5. `timeout 40 ./scripts/validate.sh`

### Key risks
- Very small scope may be viewed as too incremental.
- Output contract must be frozen to avoid test churn.

---

## Option 2 — Local JSON Task Capture + List
**Estimated effort:** 3–4 cycles

### Problem
A user needs a minimal, local way to capture and review tasks without external services.

### User
Individual contributor managing a personal task list from terminal.

### Capability
Implement `tasks.py` CLI with:
- `add --title <text>` (creates task with deterministic ID)
- `list` (prints tasks in stable order)
- file-backed storage in repo-local JSON (`data/tasks.json`)

### Out of Scope
- Multi-user sync/collaboration.
- Deadlines, reminders, or notifications.
- Remote backends/cloud sync.
- Full CRUD beyond `add` and `list` for M1.

### Demo Path
1. `timeout 10 python3 tasks.py add --title "Write report"`
2. `timeout 10 python3 tasks.py add --title "Review PR"`
3. `timeout 10 python3 tasks.py list`
4. Expect two tasks, deterministic ordering, stable ID format.
5. `timeout 40 ./scripts/validate.sh`

### Key risks
- Deterministic ID strategy must be clearly defined.
- JSON file path/format contract needs agreement early.
- Potential scope creep into edit/delete/completion features.

---

## Option 3 — Batch Input Validation Report
**Estimated effort:** 2–4 cycles

### Problem
Teams need to validate many input names at once and quickly identify invalid rows.

### User
Operator preparing batch data for downstream automation.

### Capability
Add script that reads newline-delimited names from a file and outputs:
- valid statuses (`baseline-ready:<name>`)
- invalid row report with row numbers
- final summary counts (valid/invalid)

### Out of Scope
- CSV dialect variations and advanced parsing.
- Auto-correction/suggestion of invalid values.
- Parallel processing/performance optimization.
- External data sources (S3, APIs, DBs).

### Demo Path
1. Create fixture file with valid + blank-name lines.
2. `timeout 10 python3 batch_status.py --input fixtures/names.txt`
3. Expect deterministic per-row output and summary totals.
4. Verify non-zero exit when any invalid rows exist.
5. `timeout 40 ./scripts/validate.sh`

### Key risks
- Exact output format must be fixed for objective verification.
- Error handling rules (skip vs fail-fast) need explicit choice.

---

## Human clarification blockers (applies to all options)
1. Which target user/problem should be treated as the product baseline?
2. Preferred interface for first slice: CLI-only vs API-first?
3. Should local file persistence be allowed in M1, or remain stateless?
4. Priority order among options so implementation can begin immediately.

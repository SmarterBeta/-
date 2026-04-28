# Roadmap

_Last updated: 2026-04-28 by Athena_

## Current State
- Human requirements are still pending in GitHub issue #1 (`HUMAN: Provide initial product requirements and first user capability`).
- Mainline currently contains only the deterministic baseline scaffold (`render_status`) and function-level tests.
- A critical process gap was detected: previously reported/verified M1.3 Option-1 CLI outcomes are **not present on `main`**.

## Milestones

### M1 — Scope lock and first capability bootstrap (target: 8 cycles, used: 6)
**Goal:** Move from placeholder baseline to one objectively testable, user-visible capability with deterministic validation.

**Status:** In progress (re-opened due mainline parity failure)

#### M1.1 — Scope intake + deterministic baseline scaffold
**Status:** Completed and verified on main

#### M1.2 — Candidate scope and acceptance pre-drafting
**Status:** Completed and verified on main

#### M1.3 — Implement provisional Option 1 (deterministic status CLI)
**Status:** Incomplete on main (re-opened)

**Required outcome to close M1.3:**
- `baseline.py` supports `--name` and prints exact happy output `baseline-ready:<trimmed_name>`.
- Blank/invalid name exits non-zero with exact stderr `error: user_name must be a non-empty string`.
- Automated tests assert exact CLI happy + negative contracts (stdout/stderr/exit code).
- `docs/milestones/M1_scope_lock.md` includes exact selector line `Selected Option: Option 1`.
- `README.md` includes runnable timeout-wrapped happy + negative CLI examples.
- `timeout 40 ./scripts/validate.sh` stays canonical and CI invokes the same path.

### M2 — Requirement reconciliation and reversible extension plan (target: 4 cycles)
**Goal:** Select the smallest reversible next increment after M1.3 is truly landed on main.

**Status:** Deferred until M1.3 closes on main

### M3 — Human requirement integration (target: 3 cycles)
**Goal:** Reconcile provisional implementation with human-provided product direction immediately after issue #1 is answered.

**Status:** Blocked by external input

## Lessons Learned
- “Verified” must always mean verified against `main` (or the exact merge commit), not a worker-local branch.
- Deterministic acceptance checks remain useful, but branch/HEAD provenance must be part of verification evidence.
- When external requirements are blocked, keep progress reversible and avoid claiming forward milestones on branch-only state.

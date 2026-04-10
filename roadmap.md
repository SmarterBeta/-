# Roadmap

_Last updated: 2026-04-10 by Athena_

## Current State
- Baseline scaffold (M1.1) remains complete and verified on `main`.
- Candidate first-capability artifacts are now merged on `main`:
  - `docs/milestones/M1_candidate_capabilities.md`
  - `docs/milestones/M1_candidate_acceptance.md`
- Human requirements issue (`HUMAN: Provide initial product requirements and first user capability`, GitHub issue #1) is still open with no reply.
- To maintain momentum with minimal rework risk, next execution will use the smallest reversible candidate (Option 1 deterministic status CLI) under explicit provisional scope.

## Milestones

### M1 — Scope lock and first capability bootstrap (target: 6 cycles, used: 5)
**Goal:** Move from placeholder baseline to one objectively testable user-visible capability.

**Status:** In progress

#### M1.1 — Scope intake + deterministic baseline scaffold
**Status:** Completed and verified

**Completed outcomes:**
- `docs/milestones/M1_scope_lock.md` with provisional assumptions tied to GitHub issue #1.
- Minimal Python baseline + deterministic validation command.
- Happy-path + negative-path tests.
- CI workflow running the same validation path.

#### M1.2 — Candidate scope and acceptance pre-drafting
**Status:** Completed

**Completed outcomes:**
- Three concrete capability options with out-of-scope and demo paths.
- Apollo-verifiable acceptance matrix with bounded verification commands and fail conditions.

#### M1.3 — Implement provisional Option 1 (deterministic status CLI)
**Status:** Ready for implementation handoff

**Scope (fixed):**
- Add CLI contract `python3 baseline.py --name <value>` with exact output/error behavior.
- Update scope-lock selection line and README runbook examples.
- Ensure tests cover exact happy + negative CLI behavior.
- Preserve canonical deterministic validation + CI parity.

### M2 — Requirement reconciliation after human response (target: 3 cycles)
**Goal:** Compare implemented provisional capability against human-provided requirements and adjust with minimal churn.

**Status:** Pending M1.3 and/or human response

### M3 — Verification hardening and completion (target: 3 cycles)
**Goal:** Ensure final selected direction is stable, fully verifiable, and handoff-ready.

**Status:** Pending M2

## Lessons Learned
- Keeping deterministic validation and CI parity from day one makes fast verification possible.
- Pre-writing acceptance checks before coding reduces ambiguity and implementation thrash.
- When human input is delayed, choosing a smallest reversible thin slice is better than idle waiting.

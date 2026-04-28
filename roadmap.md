# Roadmap

_Last updated: 2026-04-28 by Athena_

## Current State
- M1 provisional capability (Option 1 deterministic status CLI) is implemented on `main` and passed Apollo verification.
- Canonical deterministic validation path is stable and CI-parity is preserved (`timeout 40 ./scripts/validate.sh` and `.github/workflows/validate.yml`).
- Human requirements issue is still unanswered: GitHub issue #1 `HUMAN: Provide initial product requirements and first user capability`.

## Milestones

### M1 — Scope lock and first capability bootstrap (target: 6 cycles, used: 6)
**Goal:** Move from placeholder baseline to one objectively testable user-visible capability.

**Status:** Completed and verified

#### M1.1 — Scope intake + deterministic baseline scaffold
**Status:** Completed and verified

#### M1.2 — Candidate scope and acceptance pre-drafting
**Status:** Completed

#### M1.3 — Implement provisional Option 1 (deterministic status CLI)
**Status:** Completed and verified

**Verified outcomes:**
- `docs/milestones/M1_scope_lock.md` contains `Selected Option: Option 1`.
- `baseline.py` supports `--name` with exact happy output and exact negative error contract.
- Tests cover exact CLI happy and negative behavior.
- README includes runnable happy/negative examples.
- CI executes the same canonical validation path as local docs.

### M2 — Requirement reconciliation and reversible extension plan (target: 4 cycles)
**Goal:** Advance the project safely while waiting for human requirements by choosing the smallest reversible next increment with strict verification criteria.

**Status:** Planning

#### M2.1 — Post-M1.3 option analysis + acceptance hardening
**Status:** In progress (Athena planning cycle)

**Planned outcomes:**
- Independent blind repo assessment of 2–3 low-regret next-step options.
- Apollo-verifiable acceptance criteria for selected option, including bounded timeout checks and explicit fail conditions.
- Recommendation that minimizes churn once GitHub issue #1 is answered.

### M3 — Human requirement integration (target: 3 cycles)
**Goal:** Reconcile provisional implementation with human-provided product direction immediately after issue #1 is answered.

**Status:** Blocked by external input

## Lessons Learned
- Objective acceptance criteria before coding continue to reduce ambiguity and rework.
- Maintaining deterministic validation/CI parity allows rapid verification loops.
- When external requirements are blocked, focus on reversible, low-coupling increments rather than speculative feature expansion.

# Roadmap

_Last updated: 2026-04-28 by Athena_

## Current State
- Human requirements are still pending in GitHub issue #1 (`HUMAN: Provide initial product requirements and first user capability`).
- Mainline now contains the full M1.3 Option 1 deterministic CLI contract (`baseline.py --name`) with exact happy/negative behavior, tests, docs, and CI parity.
- Canonical validation is stable and deterministic via `timeout 40 ./scripts/validate.sh`.

## Milestones

### M1 — Scope lock and first capability bootstrap (target: 8 cycles, used: 8)
**Goal:** Move from placeholder baseline to one objectively testable, user-visible capability with deterministic validation.

**Status:** Completed and verified on main

#### M1.1 — Scope intake + deterministic baseline scaffold
**Status:** Completed and verified on main

#### M1.2 — Candidate scope and acceptance pre-drafting
**Status:** Completed and verified on main

#### M1.3 — Implement provisional Option 1 (deterministic status CLI)
**Status:** Completed and verified on main

### M2 — Reversible extension while requirements are pending (target: 4 cycles)
**Goal:** Add one additional small, deterministic CLI capability that is easy to revise once the human product direction is provided.

**Status:** Handoff queued in tbc-db issue #25

#### M2.1 — Deterministic local task capture (`tasks.py` add/list)
**Status:** Planned

**Planned acceptance direction:**
- Implement `tasks.py add --title <text>` and `tasks.py list` with deterministic sequential IDs (`T0001`, `T0002`, ...).
- Persist to local JSON file with stable schema.
- Enforce exact negative-path error for blank title.
- Add exact-output tests (happy + negative + schema).
- Keep canonical validation and CI parity unchanged (`./scripts/validate.sh`).

### M3 — Human requirement integration (target: 3 cycles)
**Goal:** Reconcile provisional implementations with human-provided target user/problem/capability as soon as GitHub issue #1 is answered.

**Status:** Blocked by external input

## Lessons Learned
- “Verified” must mean verified against `main` (or exact merge commit), never branch-local state.
- Acceptance criteria with exact output/error contracts prevent ambiguity and reduce verification disputes.
- While waiting for external requirements, prioritize reversible, deterministic slices and avoid irreversible architecture commitments.

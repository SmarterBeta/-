# Roadmap

_Last updated: 2026-04-10 by Athena_

## Current State
- M1.1 baseline scaffold is complete and verified:
  - `docs/milestones/M1_scope_lock.md`
  - `README.md` setup/run/validate commands
  - `baseline.py`
  - `tests/test_baseline.py`
  - `scripts/validate.sh`
  - `.github/workflows/validate.yml`
- Verification passed in Apollo phase and PR #2 was merged to `main`.
- Canonical validation path is deterministic and bounded: `timeout 40 ./scripts/validate.sh`.
- Human requirements are still missing; GitHub issue #1 remains open with no response.

## Milestones

### M1 — Scope lock and implementation readiness (target: 4 cycles, used: 4)
**Goal:** Remove ambiguity before feature coding and establish a verifiable baseline.

**Status:** In progress (M1.1 complete, M1.2 blocked by human input)

#### M1.1 — Scope intake + repo bootstrap baseline
**Status:** Completed

**Completed outcomes:**
- Scope-lock doc template and assumptions tied to HUMAN issue #1.
- Minimal deterministic Python scaffold.
- Canonical validation command with bounded timeout.
- Happy-path and negative-path automated tests.
- CI workflow invoking the same validation path.

#### M1.2 — Requirement finalization and first thin-slice handoff
**Goal:** Convert scope lock into one approved first capability and hand off a fully testable implementation milestone.

**Status:** Blocked by human response on GitHub issue #1.

**Next preparatory work while blocked:**
- Produce 2–3 concrete candidate first-capability options (problem/user/capability/out-of-scope/demo).
- Pre-draft Apollo-verifiable acceptance checks for each option so implementation can begin immediately once a human selects one.

### M2 — Build first functional increment (target: 4 cycles)
**Goal:** Implement exactly one user-visible capability from approved scope with happy/negative-path tests.

**Status:** Blocked by M1.2

### M3 — Verification hardening and completion (target: 3 cycles)
**Goal:** Ensure implementation is stable, objectively verifiable, and documented for handoff.

**Status:** Blocked by M2

## Lessons Learned
- Front-loading deterministic validation and CI parity made M1.1 verification fast and objective.
- Scope ambiguity remains the dominant risk; human requirement latency is currently the critical path.
- Maintaining pre-written acceptance checks for candidate scope options can reduce idle time and speed execution after human input.
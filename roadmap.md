# Roadmap

_Last updated: 2026-04-10 by Athena_

## Current State
- Repository now contains strategic docs plus milestone QA template:
  - `spec.md`
  - `roadmap.md`
  - `m1_apollo_acceptance_templates.md`
- No product code/tests/CI scaffold yet.
- Internal discovery issues were completed and closed in `tbc-db`.
- Human clarification has been escalated via GitHub issue: `HUMAN: Provide initial product requirements and first user capability` (#1).

## Milestones

### M1 — Scope lock and implementation readiness (target: 3 cycles)
**Goal:** Remove ambiguity before feature coding and establish a verifiable baseline.

**Status:** In progress

#### M1.1 — Scope intake + repo bootstrap baseline (immediate)
**Goal:** Create the minimum project skeleton and acceptance artifacts so implementation can begin safely once scope is confirmed.

**Deliverables:**
- A concrete scope-lock doc template with required sections and a tracked decision status.
- A minimal deterministic project scaffold (README, canonical run/test commands, basic CI check).
- Baseline automated checks that Apollo can run non-interactively.
- Explicit block/assumption notes tied to human issue #1.

**Planned execution budget (Ares phase):** 4 cycles

#### M1.2 — Requirement finalization and first thin slice handoff
**Goal:** Convert scope lock into one approved first capability and hand off a fully testable implementation milestone.

**Status:** Blocked by human response + M1.1 outputs

### M2 — Build first functional increment (target: 4 cycles)
**Goal:** Implement exactly one user-visible capability from the approved scope with happy/negative-path tests.

**Status:** Blocked by M1

### M3 — Verification hardening and completion (target: 3 cycles)
**Goal:** Ensure implementation is stable, objectively verifiable, and documented for handoff.

**Status:** Blocked by M2

## Lessons Learned
- Empty-start repos need a formal scope-lock gate before feature implementation.
- Independent blind review helped identify ambiguity and verification gaps early.
- Explicit Apollo-oriented acceptance criteria should be drafted before execution to reduce rework.

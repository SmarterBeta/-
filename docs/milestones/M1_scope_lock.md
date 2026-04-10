# M1 Scope Lock

**Decision Status:** Provisional and blocked pending human clarification from GitHub HUMAN issue #1.

**Assumptions tied to GitHub HUMAN issue #1:**
- Until issue #1 is answered, the first capability is limited to a deterministic local scaffold and validation path only.
- No external services, APIs, or network calls are required for M1.1 required validation.
- The first user-facing behavior remains a placeholder baseline signal (`baseline-ready:<name>`) until issue #1 confirms the real capability.

## Problem
The repository needs a minimum executable baseline that can be validated non-interactively while product requirements are still pending in GitHub HUMAN issue #1.

## User
Primary user for this milestone is the internal automation runner (Apollo/CI) that must execute deterministic checks without human input.

## Capability
Provide a tiny local Python scaffold with a canonical validation command, one happy-path smoke test, one negative-path test, and CI that invokes the same validation command.

## Out of Scope
- Final product behavior and user flows (blocked by GitHub HUMAN issue #1).
- Any network-dependent checks in required validation.
- Any broader architecture beyond the minimal M1.1 baseline.

## Demo Path
1. Run `timeout 10 python3 baseline.py`.
2. Run canonical validation: `timeout 40 ./scripts/validate.sh`.
3. Confirm CI workflow `.github/workflows/validate.yml` invokes `./scripts/validate.sh`.

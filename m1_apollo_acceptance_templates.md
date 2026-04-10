# Blind Milestone Quality Review — First Implementation Milestone

Date: 2026-04-10  
Mode: Blind (repo-only review)

## 1) Readiness verdict for implementation

**Current verdict: NOT implementation-ready yet.**

From `spec.md` + `roadmap.md`, functional scope is still undefined. If implementation starts now, Apollo cannot produce reliable pass/fail beyond "files exist" checks.

### Minimum gate before coding starts
Require a short scope-lock artifact (one page) with:
1. Target user + problem statement (single sentence each)
2. First user-visible capability (exactly one)
3. Out-of-scope list (at least 3 bullets)
4. Demo path Apollo can execute (command + expected output)

Without this gate, milestone checks will be subjective and likely to thrash.

---

## 2) Apollo-verifiable acceptance criteria template (for Milestone 1 implementation)

Use this template per criterion.

```md
### AC-[ID]: [Short title]
- Type: code | test | doc | prompt-based
- Requirement (atomic): [single behavior]
- Evidence path(s): [exact file paths]
- Verification command: `[exact deterministic command]`
- Pass condition (objective): [exact string, exit code, count, or schema]
- Fail condition: [what must fail this criterion]
- Anti-flake guard: [fixed seed / no network / timeout]
```

### Recommended baseline AC set (fill placeholders)

#### AC-01 Scope lock present
- Type: doc
- Requirement (atomic): `docs/milestones/M1_scope_lock.md` exists and contains required sections.
- Evidence path(s): `docs/milestones/M1_scope_lock.md`
- Verification command:
  - `test -f docs/milestones/M1_scope_lock.md`
  - `grep -E "^## (Problem|User|Capability|Out of Scope|Demo Path)$" docs/milestones/M1_scope_lock.md`
- Pass condition (objective): file exists and all 5 section headers are present.
- Fail condition: missing file or any section missing.
- Anti-flake guard: text-only check, no external dependency.

#### AC-02 Build/Run entrypoint works
- Type: code
- Requirement (atomic): project exposes one canonical local run command.
- Evidence path(s): `README.md`, build/run config files
- Verification command: `[FILL: e.g., timeout 120 make run-smoke]`
- Pass condition (objective): command exits 0 and prints `[FILL_EXPECTED_MARKER]` exactly once.
- Fail condition: non-zero exit code, timeout, or marker missing/duplicated.
- Anti-flake guard: no network calls; fixed local test data.

#### AC-03 Happy-path behavior test exists and passes
- Type: test
- Requirement (atomic): one automated test validates the first user-visible capability end-to-end (happy path).
- Evidence path(s): `[FILL_TEST_FILE_PATH]`
- Verification command: `[FILL_SINGLE_TEST_COMMAND]`
- Pass condition (objective): exit code 0 and test output contains `[TEST_NAME] ... PASS`.
- Fail condition: test missing, skipped, flaky, or failing.
- Anti-flake guard: fixed seed/time input, deterministic fixtures.

#### AC-04 Negative-path behavior test exists and passes
- Type: test
- Requirement (atomic): invalid input or failure mode returns specified error/response.
- Evidence path(s): `[FILL_TEST_FILE_PATH]`
- Verification command: `[FILL_SINGLE_TEST_COMMAND]`
- Pass condition (objective): exit code 0 and assertion matches exact error code/message pattern.
- Fail condition: broad/ambiguous error assertions (e.g., "contains error" only).
- Anti-flake guard: assert exact status/code + stable message regex.

#### AC-05 Regression guard for existing checks
- Type: test
- Requirement (atomic): all pre-existing required checks continue to pass.
- Evidence path(s): CI workflow + test config
- Verification command: `[FILL_MINIMAL_REQUIRED_CHECK_COMMAND]`
- Pass condition (objective): command exits 0 with no skipped required suites.
- Fail condition: any previously required check fails or becomes optional without rationale PR note.
- Anti-flake guard: pin tool versions in lockfile/config.

#### AC-06 Operator documentation for milestone feature
- Type: doc
- Requirement (atomic): README includes setup, run, and validation steps for the new capability.
- Evidence path(s): `README.md`
- Verification command:
  - `grep -E "^## (Setup|Run|Validate)$" README.md`
- Pass condition (objective): all 3 sections present; each section includes at least one command block.
- Fail condition: missing sections or prose-only instructions with no executable commands.
- Anti-flake guard: commands must be copy/paste runnable.

#### AC-07 Prompt-based oracle (only if LLM output is part of product)
- Type: prompt-based
- Requirement (atomic): given fixed prompt input, output conforms to required schema.
- Evidence path(s): `tests/prompts/m1_prompt_cases.json`, schema file
- Verification command: `[FILL_PROMPT_TEST_RUNNER_COMMAND]`
- Pass condition (objective): 100% of cases validate against schema and required keys.
- Fail condition: free-form grading, subjective wording, or manual-only review.
- Anti-flake guard: temperature=0, fixed model/version, schema validation only.

---

## 3) Top ambiguity/regression risks and how to make checks objective

| Risk | Why it causes thrash | Objective countermeasure |
|---|---|---|
| Undefined "first capability" | Team builds different things; Apollo cannot judge correctness | Require single-sentence capability in scope lock; reject milestone if more than one capability is listed |
| Vague words ("basic", "working", "user-friendly") | Non-testable criteria lead to endless review loops | Replace adjectives with measurable outcomes (exit code, output marker, latency bound, count) |
| No canonical command | Apollo/manual reviewers run different flows | Define one required command per criterion; fail if command absent in README/Makefile/scripts |
| Only happy-path coverage | Breaks appear immediately in real inputs | Require one explicit negative-path test with exact expected status/error |
| Flaky tests/non-determinism | False failures and rework | Fixed seeds, deterministic fixtures, no network, bounded timeouts |
| Hidden scope creep during implementation | Milestone balloons and blocks completion | Out-of-scope section required; any addition must add/change AC IDs in same PR |
| Prompt-quality judged by humans | Inconsistent pass/fail and model drift | Evaluate schema/constraints only; pin model version; disable randomness |

---

## 4) Apollo pass/fail objectivity checklist (quick use)

A criterion is Apollo-ready only if all are true:
- [ ] Single atomic behavior
- [ ] Exact evidence file path(s)
- [ ] One deterministic command with timeout
- [ ] Binary pass/fail rule (no subjective wording)
- [ ] Explicit failure examples
- [ ] No hidden human judgment required

If any box is unchecked, criterion should be considered **not ready**.

---

## 5) Recommended milestone quality bar

Before implementation milestone is marked complete:
1. All AC items are machine-checkable.
2. At least 1 happy-path + 1 negative-path test pass.
3. README runbook reproduces the demo path.
4. No criterion depends on subjective manual interpretation.

This is the minimum to make Apollo verification credible for an empty-start project.

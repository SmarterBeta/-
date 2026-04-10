# M1 Candidate Acceptance Checks (Apollo-Verifiable)

Date: 2026-04-10  
Mode: Blind repo-only drafting

Purpose: define objective pass/fail acceptance checks for each candidate first-capability option in `docs/milestones/M1_candidate_capabilities.md`, so Apollo can verify completion without subjective judgment.

---

## Global gates (must pass for **any** selected option)

### G-01 Exactly one option is selected for implementation
- **Type:** doc
- **Evidence:** `docs/milestones/M1_scope_lock.md`
- **Verification command:**
  - `timeout 10 grep -E "^Selected Option: Option [123]$" docs/milestones/M1_scope_lock.md`
- **Pass condition:** exactly one line matches `Selected Option: Option 1|2|3`.
- **Fail condition:** no selection, multiple selections, or free-form wording.
- **Ambiguity guard:** reject milestone if scope lock references behaviors from more than one option.

### G-02 Canonical validation command remains deterministic
- **Type:** test
- **Evidence:** `scripts/validate.sh`, `.github/workflows/validate.yml`
- **Verification command:**
  - `timeout 40 ./scripts/validate.sh`
  - `timeout 10 grep -F "./scripts/validate.sh" .github/workflows/validate.yml`
- **Pass condition:** validation exits `0` and workflow invokes same command.
- **Fail condition:** timeout, non-zero exit, or CI uses a different required command.
- **Ambiguity guard:** required checks must run with bounded timeout and no network dependency.

### G-03 Required acceptance tests exist (happy + negative)
- **Type:** test
- **Evidence:** option-specific test file(s)
- **Verification command:**
  - `timeout 10 python3 -m unittest discover -s tests -p "test_*.py" -q`
- **Pass condition:** at least one happy-path and one negative-path test for selected option pass.
- **Fail condition:** missing negative-path coverage, skipped tests, or only manual verification.
- **Ambiguity guard:** assertions must check exact status/output contracts, not vague substrings.

---

## Option 1 — Deterministic Status CLI (`baseline.py --name`)

### O1-AC-01 CLI happy path contract
- **Type:** code
- **Evidence:** `baseline.py`
- **Verification command:**
  - `timeout 10 python3 baseline.py --name "  Alice  "`
- **Pass condition:** exit `0`; stdout is exactly `baseline-ready:Alice` (single line).
- **Fail condition:** different prefix, extra prose/log lines, or whitespace not normalized.
- **Ambiguity guard:** output contract is exact string match, case-sensitive.

### O1-AC-02 CLI negative path contract
- **Type:** code
- **Evidence:** `baseline.py`
- **Verification command:**
  - `timeout 10 bash -lc 'python3 baseline.py --name "   " >/tmp/o1.out 2>/tmp/o1.err; code=$?; echo $code; test $code -ne 0; grep -Fx "error: user_name must be a non-empty string" /tmp/o1.err'`
- **Pass condition:** non-zero exit and exact stderr line `error: user_name must be a non-empty string`.
- **Fail condition:** zero exit, traceback-only failure, or non-deterministic error text.
- **Ambiguity guard:** disallow generic messages like `invalid input`.

### O1-AC-03 Automated tests pin contract
- **Type:** test
- **Evidence:** `tests/test_baseline.py` (or `tests/test_baseline_cli.py`)
- **Verification command:**
  - `timeout 10 python3 -m unittest tests.test_baseline -q`
- **Pass condition:** test suite includes and passes one exact-output happy-path assertion and one exact-error negative-path assertion.
- **Fail condition:** tests only assert exception type without message/exit behavior.
- **Ambiguity guard:** if CLI is added, tests must validate CLI behavior (not only function-level behavior).

### O1-AC-04 Operator runbook updated
- **Type:** doc
- **Evidence:** `README.md`
- **Verification command:**
  - `timeout 10 grep -F "python3 baseline.py --name \"Alice\"" README.md`
  - `timeout 10 grep -F "python3 baseline.py --name \"   \"" README.md`
- **Pass condition:** README shows executable happy + negative command examples.
- **Fail condition:** prose-only docs or missing negative example.
- **Ambiguity guard:** command examples must be copy/paste runnable with `timeout`.

---

## Option 2 — Local JSON task capture + list (`tasks.py`)

### O2-AC-01 Add command creates deterministic IDs
- **Type:** code
- **Evidence:** `tasks.py`, `data/tasks.json`
- **Verification command:**
  - `timeout 10 bash -lc 'tmp=$(mktemp); python3 tasks.py add --title "Write report" --data-file "$tmp"; python3 tasks.py add --title "Review PR" --data-file "$tmp"; cat "$tmp"'`
- **Pass condition:** stored IDs are exactly `T0001`, `T0002` in insertion order.
- **Fail condition:** UUID/time-based/random IDs, gaps, or non-stable ordering.
- **Ambiguity guard:** ID format fixed to regex `^T[0-9]{4}$` for M1.

### O2-AC-02 List command output schema is exact
- **Type:** code
- **Evidence:** `tasks.py`
- **Verification command:**
  - `timeout 10 bash -lc 'tmp=$(mktemp); python3 tasks.py add --title "Write report" --data-file "$tmp" >/dev/null; python3 tasks.py add --title "Review PR" --data-file "$tmp" >/dev/null; python3 tasks.py list --data-file "$tmp"'`
- **Pass condition:** stdout exactly:
  - `T0001 | Write report`
  - `T0002 | Review PR`
- **Fail condition:** unstable sort order, extra fields, or decorative formatting that breaks parsing.
- **Ambiguity guard:** output is line-oriented and machine-parseable (one task per line).

### O2-AC-03 Negative path rejects blank title
- **Type:** code/test
- **Evidence:** `tasks.py`, `tests/test_tasks.py` (or equivalent)
- **Verification command:**
  - `timeout 10 bash -lc 'tmp=$(mktemp); python3 tasks.py add --title "   " --data-file "$tmp" >/tmp/o2.out 2>/tmp/o2.err; code=$?; echo $code; test $code -ne 0; grep -Fx "error: title must be a non-empty string" /tmp/o2.err'`
- **Pass condition:** non-zero exit, exact error, and JSON file remains empty/non-created.
- **Fail condition:** blank title accepted or partial/corrupt writes occur.
- **Ambiguity guard:** write must be atomic (no partial file on validation failure).

### O2-AC-04 File schema remains stable
- **Type:** test
- **Evidence:** `tests/test_tasks_schema.py` (or equivalent)
- **Verification command:**
  - `timeout 10 python3 -m unittest tests.test_tasks_schema -q`
- **Pass condition:** schema assertions enforce keys `{id,title}` and JSON array top-level.
- **Fail condition:** undocumented schema drift (extra required fields or changed key names).
- **Ambiguity guard:** any schema change requires same-PR update to acceptance doc and tests.

---

## Option 3 — Batch input validation report (`batch_status.py`)

### O3-AC-01 Mixed-input report format is exact
- **Type:** code
- **Evidence:** `batch_status.py`, `tests/fixtures/names_mixed.txt`
- **Verification command:**
  - `timeout 10 bash -lc 'python3 batch_status.py --input tests/fixtures/names_mixed.txt >/tmp/o3.out 2>/tmp/o3.err; code=$?; echo $code; test $code -eq 1; cat /tmp/o3.out'`
- **Pass condition:** stdout exact lines:
  - `1\tbaseline-ready:Alice`
  - `2\tERROR\tblank-name`
  - `3\tbaseline-ready:Bob`
  - `SUMMARY\tvalid=2\tinvalid=1`
- **Fail condition:** fail-fast behavior, altered delimiters, or summary mismatch.
- **Ambiguity guard:** processing mode is explicitly **continue-on-error** with row numbers.

### O3-AC-02 All-valid batch exits cleanly
- **Type:** code
- **Evidence:** `batch_status.py`, `tests/fixtures/names_valid.txt`
- **Verification command:**
  - `timeout 10 bash -lc 'python3 batch_status.py --input tests/fixtures/names_valid.txt >/tmp/o3v.out; code=$?; echo $code; test $code -eq 0; grep -Fx "SUMMARY\tvalid=3\tinvalid=0" /tmp/o3v.out'`
- **Pass condition:** exit `0` and exact valid-only summary.
- **Fail condition:** non-zero exit on all-valid input or missing summary.
- **Ambiguity guard:** summary line required in all modes.

### O3-AC-03 Missing file is handled deterministically
- **Type:** negative test
- **Evidence:** `batch_status.py`, `tests/test_batch_status.py`
- **Verification command:**
  - `timeout 10 bash -lc 'python3 batch_status.py --input tests/fixtures/does_not_exist.txt >/tmp/o3m.out 2>/tmp/o3m.err; code=$?; echo $code; test $code -ne 0; grep -Fx "error: input file not found" /tmp/o3m.err'`
- **Pass condition:** non-zero exit and exact missing-file error text.
- **Fail condition:** traceback dump, silent success, or vague message.
- **Ambiguity guard:** filesystem errors are normalized to stable user-facing error strings.

### O3-AC-04 Automated regression tests cover row accounting
- **Type:** test
- **Evidence:** `tests/test_batch_status.py`
- **Verification command:**
  - `timeout 10 python3 -m unittest tests.test_batch_status -q`
- **Pass condition:** tests assert row numbers, valid/invalid counts, and exit code policy.
- **Fail condition:** tests check only partial output or ignore exit codes.
- **Ambiguity guard:** every fixture-driven test must assert final summary line exactly.

---

## Anti-thrash ambiguity checklist (apply before implementation starts)

1. **Freeze exact output contract** for the selected option (line format, delimiters, casing).
2. **Freeze error policy** (exact message + exit code mapping per failure mode).
3. **Define deterministic data rules** (ID sequence, ordering, normalization rules).
4. **Require one canonical command per acceptance check**, each with `timeout`.
5. **Reject subjective wording** (`simple`, `usable`, `clean`) in acceptance criteria.
6. **Fail on hidden scope creep**: if new behavior appears outside selected option and out-of-scope list, milestone is not complete.

If any checklist item is unresolved, M1.2 is not Apollo-ready.

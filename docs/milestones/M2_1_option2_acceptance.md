# M2.1 Option 2 — Deterministic local task capture (provisional)

Status: Drafted by Athena for Ares implementation handoff

## Goal
Add a second reversible, deterministic CLI capability while human requirements are pending.

## Scope
Implement `tasks.py` with two commands:
- `python tasks.py add --title "<text>"`
- `python tasks.py list`

Persistence:
- Use a local JSON data file at `data/tasks.json` (create if missing).
- Store stable schema:
  - top-level object with key `tasks`
  - `tasks` is an array of objects with keys: `id`, `title`

ID policy:
- Deterministic sequential IDs in insertion order: `T0001`, `T0002`, ...

## Exact behavioral contract
### Happy path
1. `timeout 10 python tasks.py add --title "alpha"`
   - stdout exactly: `added:T0001:alpha`
   - exit code: 0
2. `timeout 10 python tasks.py add --title "beta"`
   - stdout exactly: `added:T0002:beta`
   - exit code: 0
3. `timeout 10 python tasks.py list`
   - stdout exactly:
     - line 1: `T0001 alpha`
     - line 2: `T0002 beta`
   - exit code: 0

### Negative path
`timeout 10 python tasks.py add --title "   "`
- stderr exactly: `error: title must be a non-empty string`
- exit code: non-zero

## Required verification additions
- Add tests covering:
  - exact stdout/stderr and exit behavior for happy/negative paths
  - deterministic ID sequence
  - persisted JSON schema and values
- Add README section with timeout-wrapped runnable examples for happy + negative paths.
- Keep canonical validation path unchanged (`timeout 40 ./scripts/validate.sh`).
- Ensure CI still invokes `./scripts/validate.sh`.

## Out of scope
- Multi-user/auth
- Network/API integration
- Task editing/deleting/searching/filtering
- Timestamps/metadata beyond `id` and `title`
- Concurrency guarantees across simultaneous writers

## Apollo verification checklist
- [ ] `tasks.py` exists and implements exact commands/outputs/errors above.
- [ ] `data/tasks.json` initialization and schema are deterministic.
- [ ] Tests prove exact contract and pass under bounded timeout.
- [ ] README examples match implemented behavior.
- [ ] `./scripts/validate.sh` remains canonical and is used by CI.

# Deterministic CLI Baselines

This repository contains deterministic milestone scaffolds with exact CLI contracts.

## Setup

```bash
timeout 10 python3 --version
```

## M1.3 baseline CLI (existing)

Happy path:

```bash
timeout 10 python3 baseline.py --name "  Alice  "
```

Negative path (exact stderr + non-zero exit):

```bash
timeout 10 bash -lc 'python3 baseline.py --name "   " >/tmp/o1.out 2>/tmp/o1.err; code=$?; test $code -ne 0; test ! -s /tmp/o1.out; grep -Fx "error: user_name must be a non-empty string" /tmp/o1.err'
```

## M2.1 option 2 tasks CLI

Happy path:

```bash
timeout 10 python3 tasks.py add --title "alpha"
timeout 10 python3 tasks.py add --title "beta"
timeout 10 python3 tasks.py list
```

Negative path (exact stderr + non-zero exit):

```bash
timeout 10 bash -lc 'python3 tasks.py add --title "   " >/tmp/tasks.out 2>/tmp/tasks.err; code=$?; test $code -ne 0; test ! -s /tmp/tasks.out; grep -Fx "error: title must be a non-empty string" /tmp/tasks.err'
```

## Validate

Canonical validation command:

```bash
timeout 40 ./scripts/validate.sh
```

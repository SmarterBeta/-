# M1.2 Option 1 Baseline CLI

This repository contains a minimal deterministic scaffold for milestone M1.2 Option 1.

## Setup

```bash
timeout 10 python3 --version
```

## Run

Happy path:

```bash
timeout 10 python3 baseline.py --name "Alice"
# baseline-ready:Alice
```

Negative path (blank name):

```bash
timeout 10 bash -lc 'python3 baseline.py --name "   " >/tmp/baseline.out 2>/tmp/baseline.err; code=$?; echo "$code"; cat /tmp/baseline.err'
# 1
# error: user_name must be a non-empty string
```

## Validate

Canonical validation command (bounded timeout is enforced in-script):

```bash
timeout 40 ./scripts/validate.sh
```

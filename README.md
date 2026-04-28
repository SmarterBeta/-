# M1.3 Option 1 Baseline CLI Contract

This repository contains a minimal deterministic scaffold for milestone M1.3 Option 1.

## Setup

```bash
timeout 10 python3 --version
```

## Run

Happy path:

```bash
timeout 10 python3 baseline.py --name "  Alice  "
```

Negative path (exact stderr + non-zero exit):

```bash
timeout 10 bash -lc 'python3 baseline.py --name "   " >/tmp/o1.out 2>/tmp/o1.err; code=$?; test $code -ne 0; test ! -s /tmp/o1.out; grep -Fx "error: user_name must be a non-empty string" /tmp/o1.err'
```

## Validate

Canonical validation command:

```bash
timeout 40 ./scripts/validate.sh
```

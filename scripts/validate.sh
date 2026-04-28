#!/usr/bin/env bash
set -euo pipefail

echo "Running canonical validation (timeout: 40s)..."
timeout 40 python3 -m unittest discover -s tests -p "test_*.py" -q

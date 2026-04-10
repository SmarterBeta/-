#!/usr/bin/env bash
set -euo pipefail

echo "Running canonical validation (timeout: 30s)..."
timeout 30 python3 -m unittest discover -s tests -p "test_*.py" -q

#\!/bin/bash
# Quick test runner
set -e
python -m pytest tests/ -v --tb=short
echo 'All tests passed\!'

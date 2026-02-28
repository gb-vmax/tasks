#!/bin/bash
set -e
out=/home/user/tree.txt
[ -f "$out" ] || { echo 0 > /logs/verifier/reward.txt; exit; }
grep -q 'README.md' "$out" && grep -q 'src' "$out" && grep -q 'main.py' "$out" && grep -q 'tests' "$out" && grep -q 'unit' "$out" && grep -q 'test_utils.py' "$out" && grep -q 'test_main.py' "$out"
if [ $? -eq 0 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

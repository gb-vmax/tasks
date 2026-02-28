#!/bin/bash
set -e
out="$(free -h)"
if echo "$out" | grep -qEi '^\s*Mem:' && echo "$out" | grep -qEi '\bGi\b|\bMi\b|\bKi\b'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

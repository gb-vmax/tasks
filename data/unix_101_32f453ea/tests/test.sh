#!/bin/bash
set -e
out="$(free -b -t)"
if echo "$out" | grep -qE '^\s*Total:' && echo "$out" | grep -qE '\s+[0-9]{7,}\s+'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if declare -p COLORS 2>/dev/null | grep -q 'declare -a COLORS=\(\[0\]="red" \[1\]="green" \[2\]="blue"\)'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

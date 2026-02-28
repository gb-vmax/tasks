#!/bin/bash
# Check that 'w' output contains the expected header fields
OUT=$(w)
if echo "$OUT" | grep -qE '^USER +TTY +FROM +LOGIN@ +IDLE +JCPU +PCPU +WHAT'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

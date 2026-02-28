#!/bin/bash
# Check that 'w -s -h' output does NOT contain the header and is in short format
OUT=$(w -s -h)
if ! echo "$OUT" | grep -q '^USER'; then
  # Make sure output lines are shorter than usual (short format omits JCPU/PCPU)
  if [ "$(echo "$OUT" | awk 'NR==1{print NF}')" -le 6 ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

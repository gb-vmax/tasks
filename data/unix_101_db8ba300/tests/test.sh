#!/bin/bash
EXPECTED=$'10\n40\n50'
if diff -u <(echo "$EXPECTED") /home/user/unique1.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

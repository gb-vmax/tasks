#!/bin/bash
output=$(users --version 2>&1 | head -1)
if echo "$output" | grep -qi '^users (GNU coreutils)'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

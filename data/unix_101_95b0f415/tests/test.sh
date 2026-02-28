#!/bin/bash
set -e
output=$(users --version 2>/dev/null | head -n 1)
if [[ "$output" == users* && "$output" == *GNU* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

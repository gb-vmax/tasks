#!/bin/bash
set -e
output=$(expr 42 + 58)
if [ "$output" = "100" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

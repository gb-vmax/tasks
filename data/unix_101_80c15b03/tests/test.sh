#!/bin/bash
set -e
output="$(who)"
if [ -n "$output" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

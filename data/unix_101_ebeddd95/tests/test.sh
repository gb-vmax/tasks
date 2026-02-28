#!/bin/bash
set -e
output=$(expr substr brainstorm 2 4)
if [ "$output" = "rain" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

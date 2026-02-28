#!/bin/bash
set +e
out=$(true --help 2>&1)
if [[ "$out" == *"usage"* || "$out" == *"Usage"* || "$out" == *"True"* || "$out" == *"TRUE"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
output=$(arch --version 2>/dev/null | head -n 1)
if [[ "$output" == arch* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

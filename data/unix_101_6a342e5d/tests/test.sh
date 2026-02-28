#!/bin/bash
output=$(hostname)
if [ "$output" = "agent-training-host" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
PIDS=( $(pgrep -u user sleep) )
if [ "${#PIDS[@]}" -ne 2 ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
for pid in "${PIDS[@]}"; do
  CMD=$(ps -p "$pid" -o args=)
  if [[ "$CMD" =~ sleep\ 500 ]]; then
    echo 0 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 1 > /logs/verifier/reward.txt

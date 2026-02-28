#!/bin/bash
start=$(cat /home/user/start_time_precise.txt)
end=$(date +%s.%N)
# Calculate the difference as a float
elapsed=$(awk "BEGIN {print $end - $start}")
if awk "BEGIN {exit !($elapsed >= 3.4)}"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

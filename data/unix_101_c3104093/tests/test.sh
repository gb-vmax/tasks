#!/bin/bash
output=$(bzcat /home/user/logs/log1.txt.bz2 /home/user/logs/log2.txt.bz2 2>/dev/null)
if [[ "$output" == $'First log entry\nSecond log entry' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

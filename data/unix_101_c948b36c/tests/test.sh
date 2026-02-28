#!/bin/bash
if [ ! -f /home/user/proc_count.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
val=$(cat /home/user/proc_count.txt)
if [[ "$val" =~ ^[1-9][0-9]*$ ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

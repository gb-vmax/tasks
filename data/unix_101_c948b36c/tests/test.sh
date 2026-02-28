#!/bin/bash
EXPECTED=$(nproc)
ACTUAL=$(cat /home/user/cpu_count.txt)
if [ "$EXPECTED" = "$ACTUAL" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

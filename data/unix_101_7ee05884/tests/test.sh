#!/bin/bash
if [ ! -f /home/user/output/timing.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi

grep -q '^real' /home/user/output/timing.txt && grep -q '^user' /home/user/output/timing.txt && grep -q '^sys' /home/user/output/timing.txt
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

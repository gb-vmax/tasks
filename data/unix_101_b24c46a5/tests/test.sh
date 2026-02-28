#!/bin/bash
sleep 3
if [ -f /home/user/kill_check.txt ]; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi

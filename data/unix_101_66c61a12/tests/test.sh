#!/bin/bash
PID=$(cat /home/user/pid.txt)
if ps -p $PID > /dev/null; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi

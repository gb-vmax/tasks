#!/bin/bash
if [ -f /home/user/failure.log ] && grep -qx 'FAILED' /home/user/failure.log; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

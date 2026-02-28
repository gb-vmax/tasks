#!/bin/bash
if [ -f /home/user/error.log ] && grep -q 'No such file or directory' /home/user/error.log; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

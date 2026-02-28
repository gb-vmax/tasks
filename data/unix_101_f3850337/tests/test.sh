#!/bin/bash
if grep -q -i 'No such file or directory' /home/user/errno2.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

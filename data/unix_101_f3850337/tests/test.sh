#!/bin/bash
if grep -q "ENOENT" /home/user/errno2.txt && grep -qi "No such file or directory" /home/user/errno2.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

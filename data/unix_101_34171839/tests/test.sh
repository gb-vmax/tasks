#!/bin/bash
if [ -f /home/user/output.txt ] && grep -q '^John Doe$' /home/user/output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

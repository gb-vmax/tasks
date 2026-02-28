#!/bin/bash
if [ -f /home/user/empty.txt ] && grep -q '^empty$' /home/user/empty.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

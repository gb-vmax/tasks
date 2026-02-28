#!/bin/bash
if [ -f /home/user/factors.txt ] && grep -q '^84: 2 2 3 7$' /home/user/factors.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

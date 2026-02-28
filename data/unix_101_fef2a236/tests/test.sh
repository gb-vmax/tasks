#!/bin/bash
if [ -f /home/user/sum.txt ] && grep -qx '12' /home/user/sum.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

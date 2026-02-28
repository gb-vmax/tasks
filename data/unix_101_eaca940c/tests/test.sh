#!/bin/bash
if grep -Fxq "locked append" /home/user/output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

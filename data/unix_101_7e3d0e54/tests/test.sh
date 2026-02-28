#!/bin/bash
expected_output="45: 3 3 5
60: 2 2 3 5
97: 97
100: 2 2 5 5"
if [ -f /home/user/multi_factors.txt ] && diff -u <(printf "$expected_output\n") /home/user/multi_factors.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

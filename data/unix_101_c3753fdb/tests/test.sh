#!/bin/bash
if [ ! -f /home/user/second_line.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected='line2\n'
actual=$(cat /home/user/second_line.txt)
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

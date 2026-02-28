#!/bin/bash
if [ ! -f /home/user/result.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected="first line
second line
third line"
actual=$(cat /home/user/result.txt)
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

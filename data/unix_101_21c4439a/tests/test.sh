#!/bin/bash
EXPECTED=$'Alice,30\nBob,27\nJohn,24\nEve,22'
if [ -f /home/user/data_sorted.csv ] && diff -u <(echo "$EXPECTED") /home/user/data_sorted.csv >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

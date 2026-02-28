#!/bin/bash
output=$(find /home/user/documents -type f -name '*.txt' | sort)
expected='/home/user/documents/notes.txt
/home/user/documents/reports/q1.txt
/home/user/documents/reports/q2.txt'
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

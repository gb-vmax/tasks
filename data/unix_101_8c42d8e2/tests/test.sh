#!/bin/bash
set -e
expected=$'AB\nCDEFG\nXY'
output=$(cat /home/user/short_strings.txt | tr -d '\r')
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

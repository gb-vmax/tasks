#!/bin/bash
if [ ! -f /home/user/animals_unique.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected='cat
dog
bird
cat'
output=$(cat /home/user/animals_unique.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

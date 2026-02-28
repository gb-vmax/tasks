#!/bin/bash
set -e
expected=$'And so are you\nSugar is sweet\nViolets are blue\nRoses are red'
output=$(cat /home/user/data/poem_reversed.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if [ ! -f /home/user/colors_count.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected='      3 Red
      2 blue
      3 green'
output=$(cat /home/user/colors_count.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

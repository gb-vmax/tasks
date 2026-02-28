#!/bin/bash
expected='carrot | cabbage'
out=$(cat /home/user/diff_output.txt | grep -v '^$')
if [ "$out" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

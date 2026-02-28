#!/bin/bash
if [[ -f /home/user/factors_out.txt ]]; then
  expected=$'15: 3 5\n100: 2 2 5 5\n77: 7 11'
  actual=$(cat /home/user/factors_out.txt | tr -d '\r')
  if [[ "$actual" == "$expected" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
exit 0

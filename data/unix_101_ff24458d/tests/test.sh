#!/bin/bash
if [[ -f /home/user/factors.txt ]]; then
  expected='42: 2 3 7'
  actual=$(cat /home/user/factors.txt | tr -d '\r\n')
  if [[ "$actual" == "$expected" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
exit 0

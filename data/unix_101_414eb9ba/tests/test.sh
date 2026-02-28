#!/bin/bash
if [[ -f /home/user/parallel_output.txt ]]; then
  expected=$'apple\nbanana\ncherry'
  actual=$(sort /home/user/parallel_output.txt | tr -d '\r')
  if [[ "$actual" == "$expected" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

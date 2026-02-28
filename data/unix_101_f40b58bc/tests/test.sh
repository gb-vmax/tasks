#!/bin/bash
output="$(wc -l /home/user/input.txt)"
if [[ "$output" =~ ^3[[:space:]]+/home/user/input.txt$ ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
# Check that the file exists and contains only a number (possibly negative)
if [[ -f /home/user/current_nice.txt ]]; then
  val=$(cat /home/user/current_nice.txt | tr -d '\n')
  if [[ "$val" =~ ^-?[0-9]+$ ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

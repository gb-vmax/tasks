#!/bin/bash
if [ ! -f /home/user/max_name_len.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
val=$(cat /home/user/max_name_len.txt)
if [[ "$val" =~ ^[0-9]+$ ]] && [ "$val" -ge 14 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

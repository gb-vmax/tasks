#!/bin/bash
if [[ -f "/home/user/boot_time.txt" ]]; then
  CONTENT=$(cat /home/user/boot_time.txt)
  if [[ "$CONTENT" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}$ ]]; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi

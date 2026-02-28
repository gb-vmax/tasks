#!/bin/bash
if [ ! -f /home/user/page_size.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
value=$(cat /home/user/page_size.txt)
if [[ "$value" =~ ^[0-9]+$ ]] && [ "$value" -gt 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

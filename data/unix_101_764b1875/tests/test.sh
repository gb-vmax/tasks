#!/bin/bash
if [[ ! -f /home/user/logs/app_timestamped.log ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
lines=$(wc -l < /home/user/logs/app_timestamped.log)
if [[ "$lines" -ne 3 ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
headline=$(head -n1 /home/user/logs/app_timestamped.log)
if [[ "$headline" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}\s+Started\ application$ ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

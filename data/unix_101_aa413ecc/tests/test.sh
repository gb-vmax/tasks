#!/bin/bash
if [[ ! -f /home/user/settings/config_timestamped.txt ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
lines=$(wc -l < /home/user/settings/config_timestamped.txt)
if [[ "$lines" -ne 3 ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
firstline=$(head -n1 /home/user/settings/config_timestamped.txt)
if [[ "$firstline" =~ ^[0-9]{2}:[0-9]{2}:[0-9]{2}\ set\ debug=true$ ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

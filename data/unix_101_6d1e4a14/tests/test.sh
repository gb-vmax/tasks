#!/bin/bash
val=$(cat /home/user/max_name_length.txt)
if [[ "$val" =~ ^[0-9]+$ ]] && [[ $val -ge 255 ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
output=$(last -f /home/user/logs/alice_wtmp -F -n 2 alice)
if [[ $(echo "$output" | grep -c "alice") -eq 2 ]] && echo "$output" | grep -q "Sun Jan  1 10:00:00 2023" && echo "$output" | grep -q "Mon Jan  2 09:30:00 2023"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

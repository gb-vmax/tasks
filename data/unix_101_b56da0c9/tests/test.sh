#!/bin/bash
output=$(stat -c %s /home/user/data.txt)
if [ "$output" = "18" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

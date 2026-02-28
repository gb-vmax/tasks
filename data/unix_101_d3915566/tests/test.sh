#!/bin/bash
expected="/home/user/dirB/realfile.txt"
output=$(readlink -f /home/user/dirA/chainlink)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

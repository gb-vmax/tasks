#!/bin/bash
set -e
output=$(users /home/user/testutmp)
if [[ "$output" == *user1* && "$output" == *user2* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

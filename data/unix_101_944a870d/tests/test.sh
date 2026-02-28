#!/bin/bash
set -e
expected_uid=$(id -u user)
output=$(id -u)
if [ "$output" = "$expected_uid" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

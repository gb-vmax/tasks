#!/bin/bash
set -e
output=$(zdiff /home/user/data/alpha.txt.gz /home/user/data/beta.txt.gz || true)
if echo "$output" | grep -q '3c3'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

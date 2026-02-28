#!/bin/bash
set -e
output=$(zdiff -u /home/user/reports/summary.txt /home/user/reports/summary.txt.gz || true)
if echo "$output" | grep -q '\-report 2' && echo "$output" | grep -q '+report two'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

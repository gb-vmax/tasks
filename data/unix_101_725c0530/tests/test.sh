#!/bin/bash
set -e
# Accept both 'lo' and 'eth0' as commonly present interfaces
output=$(ifconfig -a)
if echo "$output" | grep -qE '^(lo|eth0)'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

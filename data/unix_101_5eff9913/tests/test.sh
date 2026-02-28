#!/bin/bash
if [ ! -f /home/user/uptime_pretty.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that output starts with 'up'
if grep -q '^up ' /home/user/uptime_pretty.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
# Check: output file exists and contains only MX short format lines (priority and hostname)
if [ ! -s /home/user/network/dig_mx_short.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -qE '^[0-9]+\s+.*\.$' /home/user/network/dig_mx_short.txt && ! grep -qE '^;' /home/user/network/dig_mx_short.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if [ ! -f /home/user/boot_time.log ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that the line matches a typical ISO 8601 date/time format: YYYY-MM-DD HH:MM:SS
if grep -Eq '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$' /home/user/boot_time.log; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

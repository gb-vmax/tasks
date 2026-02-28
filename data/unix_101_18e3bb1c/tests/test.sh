#!/bin/bash
if [ ! -f /home/user/report_modtime.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# The mod time was set to 2022-12-25 12:30:00
expected="Sun Dec 25 12:30:00"
if grep -q "$expected" /home/user/report_modtime.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

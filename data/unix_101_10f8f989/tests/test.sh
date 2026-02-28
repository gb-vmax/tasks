#!/bin/bash
# Ensure the file exists and is non-empty
if [ ! -s /home/user/my_pids.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Each line should contain only digits (PIDs)
if grep -qEv '^[0-9]+$' /home/user/my_pids.txt; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# At least one PID should match our own
if ! grep -q "^$$$" /home/user/my_pids.txt; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
echo 1 > /logs/verifier/reward.txt

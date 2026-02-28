#!/bin/bash
if [ ! -f /home/user/processes.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q "COMMAND" /home/user/processes.txt && grep -q "USER" /home/user/processes.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

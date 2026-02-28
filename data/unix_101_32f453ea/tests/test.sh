#!/bin/bash
if [ ! -f /home/user/totalmem.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -i '^Total:' /home/user/totalmem.txt | grep -q '[0-9]'; then
  if grep -i '^Mem:' /home/user/totalmem.txt && grep -i '^Swap:' /home/user/totalmem.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

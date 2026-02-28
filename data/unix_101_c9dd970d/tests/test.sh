#!/bin/bash
if [[ -f /home/user/data.txt && ! -f /home/user/data.txt.gz ]]; then
  if grep -qx 'This is a test file.' /home/user/data.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

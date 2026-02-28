#!/bin/bash
if [[ -f /home/user/archive.log && -f /home/user/archive.log.gz ]]; then
  if grep -qx 'Error: something failed.' /home/user/archive.log; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

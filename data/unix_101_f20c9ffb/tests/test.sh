#!/bin/bash
if [ -f /home/user/data.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [ -f /home/user/data.txt.gz ]; then
  if gzip -t /home/user/data.txt.gz; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

#!/bin/bash
if [ ! -f /home/user/report.log ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [ -f /home/user/report.log.gz ]; then
  if gzip -t /home/user/report.log.gz; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

#!/bin/bash
EXPECTED="Wed May 10 15:30:00 2023"
OUTPUT=$(date -r /home/user/docs/report.txt)
if [[ "$OUTPUT" =~ "May 10 15:30:00 2023" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

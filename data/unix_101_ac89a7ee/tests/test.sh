#!/bin/bash
output=$(basename /home/user/documents/report.txt)
if [ "$output" = "report.txt" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

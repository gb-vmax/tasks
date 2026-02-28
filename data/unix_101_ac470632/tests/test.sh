#!/bin/bash
output=$(dirname /home/user/docs/report.txt)
if [ "$output" = "/home/user/docs" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

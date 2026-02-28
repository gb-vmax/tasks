#!/bin/bash
if [ "$(stat -c %G /home/user/report.txt)" = "staff" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

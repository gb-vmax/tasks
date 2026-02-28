#!/bin/bash
set -e
expected="/home/user/data/report.txt"
if [ -f /home/user/abs_path.txt ] && [ "$(cat /home/user/abs_path.txt)" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

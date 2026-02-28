#!/bin/bash
expected="report2024.pdf"
if [ -f /home/user/output.txt ] && [ "$(cat /home/user/output.txt)" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

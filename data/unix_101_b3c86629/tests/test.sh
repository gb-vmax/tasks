#!/bin/bash
if [ ! -f /home/user/lines_count.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
EXPECTED="5 /home/user/data.txt"
RESULT=$(cat /home/user/lines_count.txt | tr -d '\r\n')
if [ "$RESULT" = "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

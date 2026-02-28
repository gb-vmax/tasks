#!/bin/bash
EXPECTED="/home/user/documents/reports"
if [ -f /home/user/parent.txt ] && [ "$(cat /home/user/parent.txt)" = "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

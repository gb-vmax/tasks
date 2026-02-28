#!/bin/bash
EXPECTED='     1:ERROR: Failed to load config
     2:ERROR: Connection lost'
ACTUAL=$(grep 'ERROR' /home/user/errors_numbered.txt)
FULL_RESULT=$(cat /home/user/errors_numbered.txt)
if [ "$FULL_RESULT" == "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
mode=$(stat -c '%a' /home/user/myscript.sh)
if [ "$mode" = "744" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

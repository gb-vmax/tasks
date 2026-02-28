#!/bin/bash
if [ "$(stat -c %a /home/user/myscript.sh)" = "744" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

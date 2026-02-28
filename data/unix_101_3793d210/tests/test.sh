#!/bin/bash
if [ $(stat -c%s /home/user/data.txt) -eq 6 ] && [ "$(cat /home/user/data.txt)" = "abcdef" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if [ -f /home/user/greeting.txt ] && [ "$(cat /home/user/greeting.txt)" = "Hello, World!" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

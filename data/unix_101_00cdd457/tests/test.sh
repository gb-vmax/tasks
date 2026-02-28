#!/bin/bash
if [ -f /home/user/error.log ] && [ "$(cat /home/user/error.log | tr -d '\r')" = $'line1\nline2\nline3' ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

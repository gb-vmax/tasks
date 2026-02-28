#!/bin/bash
if [ "$(cat /home/user/email.txt 2>/dev/null)" = "alice@example.com" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

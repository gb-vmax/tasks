#!/bin/bash
set -e
if [ ! -f /home/user/hello_env.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
count=$(wc -l < /home/user/hello_env.txt)
if [ "$count" -eq 1 ] && grep -Fxq "HELLO=world" /home/user/hello_env.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

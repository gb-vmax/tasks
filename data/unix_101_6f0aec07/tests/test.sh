#!/bin/bash
if [ -f /home/user/data/greeting.txt ] && [ -f /home/user/data/answer.txt ]; then
  if grep -qxF 'Hello World' /home/user/data/greeting.txt && grep -qxF '42' /home/user/data/answer.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

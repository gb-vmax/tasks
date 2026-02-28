#!/bin/bash
if [ -f /home/user/positional.txt ] && [ "$(cat /home/user/positional.txt)" = "alpha beta" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

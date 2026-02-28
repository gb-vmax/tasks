#!/bin/bash
if [[ -f /home/user/result.txt && "$(cat -A /home/user/result.txt)" == 'foo bar' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

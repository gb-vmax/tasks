#!/bin/bash
if [ -f /home/user/arg_output.txt ] && [ "$(cat /home/user/arg_output.txt)" = "world" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if [ -f /home/user/second_param.txt ]; then
  grep -qx "banana" /home/user/second_param.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

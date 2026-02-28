#!/bin/bash
if [[ -f /home/user/output.txt && "$(cat /home/user/output.txt)" == 'Hello world' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

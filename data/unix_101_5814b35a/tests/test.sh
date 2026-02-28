#!/bin/bash
if [[ "$(cat /home/user/tasks/output.txt 2>/dev/null)" == "Hello" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

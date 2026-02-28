#!/bin/bash
expected=$(pgrep bash | wc -l)
agent=$(cat /home/user/.last_command_output 2>/dev/null | tr -d '\n')
if [ "$agent" = "$expected" ] && [ "$expected" -gt 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

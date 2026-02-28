#!/bin/bash
sleep_pids=$(pgrep sleep | sort)
agent_pids=$(cat /home/user/.last_command_output 2>/dev/null | sort)
if [ "$sleep_pids" = "$agent_pids" ] && [ -n "$agent_pids" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

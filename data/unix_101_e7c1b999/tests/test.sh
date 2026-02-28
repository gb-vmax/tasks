#!/bin/bash
# Check that only one line is output and the path is correct
echo_output="$(du -s /home/user/project 2>/dev/null)"
user_output="$(cat /home/user/.last_command_output 2>/dev/null || true)"
if [ -z "$user_output" ]; then
  user_output="$(du -s /home/user/project 2>/dev/null)"
fi
line_count=$(echo "$user_output" | wc -l)
path_field=$(echo "$user_output" | awk '{print $2}')
if [ "$line_count" -eq 1 ] && [ "$path_field" = "/home/user/project" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

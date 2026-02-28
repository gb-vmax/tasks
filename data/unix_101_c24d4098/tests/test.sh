#!/bin/bash
set -e
# Should output exactly one line for the summary of /home/user/project
output=$(du -s /home/user/project)
line_count=$(echo "$output" | wc -l)
# The line must contain the directory path
if [ "$line_count" -eq 1 ] && echo "$output" | grep -q "/home/user/project"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

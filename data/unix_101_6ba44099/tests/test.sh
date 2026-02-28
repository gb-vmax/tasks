#!/bin/bash
pid=$(pgrep -u user -f 'tail -f /home/user/docs/report.txt')
output=$(fuser /home/user/docs/report.txt 2>/dev/null)
if echo "$output" | grep -qw "$pid"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
expected=$'First log entry\nSecond log entry'
output="$(xzcat /home/user/logs/part1.log.xz /home/user/logs/part2.log.xz 2>/dev/null)"
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
fail=0
for f in /home/user/project /home/user/project/src /home/user/project/src/main.c /home/user/project/data.txt; do
  mode=$(stat -c '%a' "$f")
  if [ "$mode" != "660" ]; then
    fail=1
  fi
done
if [ $fail -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

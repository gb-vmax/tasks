#!/bin/bash
set -e
file=$(ls -tr /tmp/tmp.* 2>/dev/null | tail -n 1)
if [ -n "$file" ] && [ -f "$file" ] && [ "$(stat -c %U "$file")" = "user" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

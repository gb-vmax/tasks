#!/bin/bash
set -e
dir=$(ls -d /home/user/tmp/mydir??? 2>/dev/null | head -n 1)
if [ -n "$dir" ] && [ -d "$dir" ] && [ "$(stat -c %U "$dir")" = "user" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

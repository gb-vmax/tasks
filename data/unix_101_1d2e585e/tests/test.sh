#!/bin/bash
if [[ -f /home/user/nums.txt ]] && diff -u <(cat /home/user/nums.txt) <(printf '  1\n  2\n  3\n') >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
cd /home/user/project
out=$(sha1sum -c readme.sha1 2>&1)
if echo "$out" | grep -q '^readme.md: OK$'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

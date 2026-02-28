#!/bin/bash
if [ ! -f /home/user/mygroups.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Output should contain at least the user's primary group
grep -q "$(id -gn user)" /home/user/mygroups.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt

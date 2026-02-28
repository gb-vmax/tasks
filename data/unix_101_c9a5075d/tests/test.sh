#!/bin/bash
EXPECTED="/home/user/project\0/home/user/project/subdir\0/home/user\0"
if [ -f /home/user/multi_parents.txt ]; then
  ACTUAL=$(cat -A /home/user/multi_parents.txt | sed 's/\^@/\\0/g')
  EXPECTED_ESCAPED=$(echo -n "$EXPECTED" | cat -A | sed 's/\^@/\\0/g')
  if [ "$ACTUAL" = "$EXPECTED_ESCAPED" ]; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi

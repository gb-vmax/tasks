#!/bin/bash
if [ ! -f /home/user/story_dbl.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check for double spacing and no headers
expected='Once upon a time,\n\nthere was a penguin.\n\nIt loved Linux.\n'
actual=$(cat /home/user/story_dbl.txt)
# Remove trailing newlines for comparison
expected=$(echo -e "$expected" | sed '/^$/N;/^\n$/D')
actual=$(echo "$actual" | sed '/^$/N;/^\n$/D')
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if [ ! -f /home/user/groupcheck.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Should have two lines, one starting with 'user', one with 'nobody'
found_user=0
found_nobody=0
while IFS= read -r line; do
  case "$line" in
    user*) found_user=1 ;;
    nobody*) found_nobody=1 ;;
  esac
done < /home/user/groupcheck.txt
if [ $found_user -eq 1 ] && [ $found_nobody -eq 1 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

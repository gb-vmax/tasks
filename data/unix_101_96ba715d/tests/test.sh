#!/bin/bash
# Check that /home/user/testuser_groups.txt contains all groups for 'testuser'
expected=$(id -nG testuser)
actual=$(cat /home/user/testuser_groups.txt | tr '\n' ' ' | sed 's/ *$//')
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

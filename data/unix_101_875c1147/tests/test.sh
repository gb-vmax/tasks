#!/bin/bash
# Check that /home/user/my_groups.txt contains all groups for 'user'
expected=$(id -nG user)
actual=$(cat /home/user/my_groups.txt | tr '\n' ' ' | sed 's/ *$//')
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

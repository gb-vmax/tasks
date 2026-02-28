#!/bin/bash
set -e
# cmp should output nothing and exit code 0 if files are identical
output=$(cmp /home/user/file1.txt /home/user/file2.txt)
status=$?
if [ "$output" = "" ] && [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
set -e
cd /home/user/ls_test
output=$(ls -a)
if echo "$output" | grep -qx "." && echo "$output" | grep -qx ".." && echo "$output" | grep -qx ".hiddenfile" && echo "$output" | grep -qx "file1.txt" && echo "$output" | grep -qx "file2.txt"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

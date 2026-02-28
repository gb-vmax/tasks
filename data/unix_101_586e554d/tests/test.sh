#!/bin/bash
# Run b2sum --check and capture output
output=$(b2sum --check /home/user/filesums.txt 2>&1)
file1_status=$(echo "$output" | grep '/home/user/docs/file1.txt:' | grep -c OK)
file2_status=$(echo "$output" | grep '/home/user/docs/file2.txt:' | grep -c OK)
if [[ $file1_status -eq 1 && $file2_status -eq 1 ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

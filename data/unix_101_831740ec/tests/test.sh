#!/bin/bash
# Output should mention unportable file names
output=$(pathchk --portability /home/user/unportable/* 2>&1)
# Check that at least one known unportable file name is reported
if echo "$output" | grep -q 'verylongfilename'; then
  if echo "$output" | grep -q 'file_with:colon.txt'; then
    if echo "$output" | grep -q '-leadingdash.txt'; then
      echo 1 > /logs/verifier/reward.txt
      exit 0
    fi
  fi
fi
echo 0 > /logs/verifier/reward.txt

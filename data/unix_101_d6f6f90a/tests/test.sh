#!/bin/bash
set -e
output_file="/home/user/ls_long_output.txt"
# Ensure output file exists
if [ ! -f "$output_file" ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that all expected entries are present in the long listing
if grep -q "fileA.txt" "$output_file" && grep -q "fileB.log" "$output_file" && grep -q "subdir" "$output_file"; then
  # Check that the first character of each line is d or - (directory or file)
  if awk '{print $1}' "$output_file" | grep -Eq '^d|^-'; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

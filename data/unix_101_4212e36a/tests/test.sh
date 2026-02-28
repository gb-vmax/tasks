#!/bin/bash
set -e
output=$(namei -m /home/user/links/myfile_symlink | tr -s ' ')
# Check that at least one entry is a symlink and that at least one entry has the mode for a regular file
if echo "$output" | grep -q '^l..'; then
  if echo "$output" | grep -q '^-.r'; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi

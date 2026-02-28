#!/bin/bash
set -e
output=$(namei /home/user/projects/testdir/file1.txt | tr -s ' ')
if echo "$output" | grep -qE '^f: /home/user/projects/testdir/file1.txt$|^d [^ ]+ home$' && echo "$output" | grep -q 'f file1.txt'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
expected="/home/user/file.txt"
output=$(realpath -e /home/user/projects/test/link1)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

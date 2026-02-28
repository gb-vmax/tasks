#!/bin/bash
expected="/home/user/notes.txt"
output=$(realpath /home/user/notes.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

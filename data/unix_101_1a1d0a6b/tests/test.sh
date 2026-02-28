#!/bin/bash
expected='Third line
Second line
First line'
if [ -f /home/user/reversed_notes.txt ]; then
  actual=$(cat /home/user/reversed_notes.txt)
  if [ "$actual" = "$expected" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt

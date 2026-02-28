#!/bin/bash
set -e
out=$(ls -a /home/user/project)
if echo "$out" | grep -q "\.hidden1" && echo "$out" | grep -q "\.hidden2" && echo "$out" | grep -q "file1.txt" && echo "$out" | grep -q "file2.txt" && echo "$out" | grep -q "\." && echo "$out" | grep -q "\.\." ; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

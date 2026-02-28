#!/bin/bash
set -e
out=$(ls -p /home/user/data)
if echo "$out" | grep -q "dirA/" && echo "$out" | grep -q "dirB/" && echo "$out" | grep -q "fileA.txt" && echo "$out" | grep -q "fileB.txt" && ! echo "$out" | grep -q "fileA.txt/" && ! echo "$out" | grep -q "fileB.txt/" ; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

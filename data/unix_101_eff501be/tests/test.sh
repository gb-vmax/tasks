#!/bin/bash
set -e
OUT=$(diff -s /home/user/fileA.txt /home/user/fileB.txt)
if [[ "$OUT" == *"are identical"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

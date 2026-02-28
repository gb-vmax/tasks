#!/bin/bash
if [ ! -f /home/user/doc_columns.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check for expected two-column layout
expected=$(pr -2 /home/user/doc.txt)
actual=$(cat /home/user/doc_columns.txt)
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

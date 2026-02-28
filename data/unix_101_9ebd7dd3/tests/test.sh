#!/bin/bash
if [ ! -f /home/user/notes.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q 'This is a sensitive note.' /home/user/notes.txt; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
echo 1 > /logs/verifier/reward.txt

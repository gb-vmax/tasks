#!/bin/bash
if grep -q "This is the UPDATED file." /home/user/original.txt && ! grep -q "This is the original file." /home/user/original.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

#!/bin/bash
if cmp -s /home/user/fileA.txt /home/user/fileB.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

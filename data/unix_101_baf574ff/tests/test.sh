#!/bin/bash
if [ -f /home/user/file2.txt ] && cmp -s /home/user/file1.txt /home/user/file2.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

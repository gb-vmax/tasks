#!/bin/bash
if df -i /home/user/testdir | grep -v '^Filesystem' | grep '/home/user/testdir'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

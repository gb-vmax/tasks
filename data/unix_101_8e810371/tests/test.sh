#!/bin/bash
expected='/home/user/log.txt'
if [ ! -f "$expected" ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Should have 4 lines in total
echo 'Start log
Initial entry
Second entry
Final entry' > /tmp/expected_log
if diff -q "$expected" /tmp/expected_log > /dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

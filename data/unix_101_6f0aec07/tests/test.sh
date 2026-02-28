#!/bin/bash
if [ -f /home/user/file1.txt ] && [ -f /home/user/file2.txt ]; then
  grep -q 'Hello World' /home/user/file1.txt && grep -q 'Second file' /home/user/file2.txt && echo 1 > /logs/verifier/reward.txt && exit 0
fi
echo 0 > /logs/verifier/reward.txt

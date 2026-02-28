#!/bin/bash
if grep -q 'Patched!' /home/user/code/file.c && [ -f /home/user/code/file.c.bak ] && grep -q 'Hello!' /home/user/code/file.c.bak; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

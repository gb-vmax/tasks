#!/bin/bash
EXPECTED=$(printf '%s\n' {1..10})
if [ -f /home/user/seq_easy.txt ] && diff -u <(echo "$EXPECTED") /home/user/seq_easy.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

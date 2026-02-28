#!/bin/bash
EXPECTED=$'Alice\nBob\nCharlie\nEve'
if [ -f /home/user/sorted_names.txt ] && diff -u <(echo "$EXPECTED") /home/user/sorted_names.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

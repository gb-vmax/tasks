#!/bin/bash
set -e
expected='apple pie
apple
apple tart'
if [[ -f /home/user/found_apples.txt ]] && diff -u <(echo -e "$expected") /home/user/found_apples.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

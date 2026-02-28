#!/bin/bash
EXPECTED=$'ello\norld\nBCDE'
if [[ -f /home/user/output.txt ]] && diff -u <(echo "$EXPECTED") /home/user/output.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

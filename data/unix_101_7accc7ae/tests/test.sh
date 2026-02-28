#!/bin/bash
EXPECTED=$'abfghij\nkiogram\n1267890'
if [[ -f /home/user/stripped.txt ]] && diff -u <(echo "$EXPECTED") /home/user/stripped.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

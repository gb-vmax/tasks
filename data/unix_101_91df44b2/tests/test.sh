#!/bin/bash
EXPECTED=$'Caf\xe9\nna\xefve\n'
if [ -f /home/user/output.txt ] && cmp -s /home/user/output.txt <(echo -ne "$EXPECTED"); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

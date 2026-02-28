#!/bin/bash
EXPECTED=$'Good line\nBad  line\nEnd\n'
if [ -f /home/user/clean.txt ] && cmp -s /home/user/clean.txt <(echo -ne "$EXPECTED"); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

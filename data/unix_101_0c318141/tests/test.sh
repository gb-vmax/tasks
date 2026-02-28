#!/bin/bash
EXPECTED="05,10,15,20,25"
if [ -f /home/user/seq_custom.txt ] && [ "$(cat /home/user/seq_custom.txt)" = "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

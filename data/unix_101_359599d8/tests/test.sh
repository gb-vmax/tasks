#!/bin/bash
if [ ! -f /home/user/data_od.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# octal output always contains a left column of offsets, so check for '0000000' and some octal digits
grep -q '^0000000' /home/user/data_od.txt && grep -Eq '\b[0-7]{2,}\b' /home/user/data_od.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt

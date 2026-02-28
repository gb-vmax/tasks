#!/bin/bash
ALL=$(nproc)
IGNORED=2
EXPECTED=$((ALL-IGNORED))
[ $EXPECTED -lt 0 ] && EXPECTED=0
ACTUAL=$(cat /home/user/remaining_cpus.txt)
if [ "$EXPECTED" = "$ACTUAL" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

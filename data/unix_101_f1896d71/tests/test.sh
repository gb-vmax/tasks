#!/bin/bash
EXPECTED="$(cksum /home/user/data.txt)"
ACTUAL="$(cat /home/user/data.cksum)"
if [ "$EXPECTED" = "$ACTUAL" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

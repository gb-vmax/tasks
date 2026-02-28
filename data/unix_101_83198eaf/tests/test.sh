#!/bin/bash
EXPECTED='User has  apples and  oranges.'
if [[ "$(cat /home/user/nodigits.txt)" == "$EXPECTED" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

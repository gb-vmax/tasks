#!/bin/bash
EXPECTED=$'# apple\n\tbanana\n\tcherry\ndate\n\t\tfig\n\t\tgrape'
if diff -u <(echo "$EXPECTED") /home/user/compare.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

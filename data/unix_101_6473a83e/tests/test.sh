#!/bin/bash
EXPECTED="2021-12-25"
OUTPUT=$(date -d '2021-12-25 18:45:00' -I)
if [ "$OUTPUT" = "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

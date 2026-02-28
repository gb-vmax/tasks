#!/bin/bash
EXPECTED="0000004 0123 4567 89ab cdef\n0000014"
OUTPUT=$(cat /home/user/data/sample.hex | tr -d '\r')
if [[ "$OUTPUT" == *"0000004 0123 4567 89ab cdef"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

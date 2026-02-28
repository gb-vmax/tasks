#!/bin/bash
output=$(od -c -j4 /home/user/data/binary.bin)
expected=$'0000004\tH   e   l   l   o  \n\n0000011'
# The tab is a visual separator in od output; check for expected string
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

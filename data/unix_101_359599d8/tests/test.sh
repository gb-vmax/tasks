#!/bin/bash
output=$(od -tx1 /home/user/text/sample.txt)
expected='0000000 48 65 6c 6c 6f 2c 20 6f 64 21
0000013'
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

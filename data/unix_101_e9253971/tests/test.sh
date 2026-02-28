#!/bin/bash
expected='D
C
B
A'
if [ "$(cat /home/user/sorted.txt | tr -d '\r')" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

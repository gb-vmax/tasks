#!/bin/bash
output=$(file /home/user/doc.txt)
if echo "$output" | grep -q '/home/user/doc.txt: ASCII text'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

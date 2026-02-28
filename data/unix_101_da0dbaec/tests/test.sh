#!/bin/bash
expected='This is a
line that
should wra
p.
Short.'
if [[ "$(cat /home/user/texts/folded.txt)" == "$expected" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

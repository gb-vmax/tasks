#!/bin/bash
expected='22'
if [[ -f /home/user/col2_sum.txt ]] && [[ $(cat /home/user/col2_sum.txt) == "$expected" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

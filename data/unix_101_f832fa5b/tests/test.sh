#!/bin/bash
expected='biology
chemistry
physics
math
english'
if [ "$(cat /home/user/output/sorted_order.txt | tr -d '\r')" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

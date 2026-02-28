#!/bin/bash
if [ ! -f /home/user/continue.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
lines=$(cat /home/user/continue.txt | wc -l)
if [ "$lines" -ne 5 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='continue processing'
fail=0
while read -r line; do
  if [ "$line" != "$expected" ]; then fail=1; break; fi
done < /home/user/continue.txt
if [ $fail -eq 0 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

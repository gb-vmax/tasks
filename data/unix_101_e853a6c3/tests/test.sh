#!/bin/bash
set -e
# File must exist
[ -f /home/user/numbers.txt ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# Must have 5 lines
[ "$(wc -l < /home/user/numbers.txt)" -eq 5 ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# All lines must be unique and in 20-29
sort -n /home/user/numbers.txt | uniq -d | grep . && { echo 0 > /logs/verifier/reward.txt; exit 0; }
while read n; do
  if ! [ "$n" -ge 20 ] || ! [ "$n" -le 29 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
done < /home/user/numbers.txt
echo 1 > /logs/verifier/reward.txt

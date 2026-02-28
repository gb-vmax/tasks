#!/bin/bash
set -e
if [ ! -f /home/user/random_numbers.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(wc -l < /home/user/random_numbers.txt)
if [ "$count" -ne 3 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
while read n; do
  if ! [[ "$n" =~ ^[0-9]+$ ]]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
  if [ "$n" -lt 10 ] || [ "$n" -gt 20 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
done < /home/user/random_numbers.txt
echo 1 > /logs/verifier/reward.txt

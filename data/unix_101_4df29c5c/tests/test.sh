#!/bin/bash
sleep_pid=$(pgrep -u user sleep | head -n1)
if [ -z "$sleep_pid" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
output=$(pidof sleep)
for pid in $output; do
  if [ "$pid" = "$sleep_pid" ]; then echo 1 > /logs/verifier/reward.txt; exit 0; fi
done
echo 0 > /logs/verifier/reward.txt

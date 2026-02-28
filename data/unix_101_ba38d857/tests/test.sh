#!/bin/bash
pids=( $(pgrep -u user sleep | sort -n) )
if [ ${#pids[@]} -lt 2 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
omit=${pids[0]}
expected=""
for pid in "${pids[@]:1}"; do
  if [ -z "$expected" ]; then expected="$pid"; else expected="$expected,$pid"; fi
done
output=$(pidof -d , -o $omit sleep)
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

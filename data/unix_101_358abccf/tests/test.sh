#!/bin/bash
expected='      1 /home/user/a.txt
      2 /home/user/b.txt
      3 /home/user/c.txt
      6 total'
output=$(cat /home/user/linecounts.txt | sed 's/[[:space:]]\+/ /g' | sed 's/^ //')
expected=$(echo "$expected" | sed 's/[[:space:]]\+/ /g' | sed 's/^ //')
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/first_column.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='id
1
2
3'
output=$(cat /home/user/first_column.txt | tr -d '\r')
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

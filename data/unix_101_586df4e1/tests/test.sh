#!/bin/bash
if [ ! -f /home/user/total_sales.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected="470"
output=$(cat /home/user/total_sales.txt | tr -d '\r' | tr -d ' ')
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

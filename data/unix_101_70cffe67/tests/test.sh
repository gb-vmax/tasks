#!/bin/bash
if [ ! -f /home/user/numbered.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected="     1	Alpha
     2	Beta
     3	Gamma"
output=$(cat /home/user/numbered.txt)
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

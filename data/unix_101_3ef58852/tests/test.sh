#!/bin/bash
if [ ! -f /home/user/names_ages.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'Alice\t23\nBob\t29\nCharlie\t31'
output=$(cat /home/user/names_ages.txt | tr -d '\r')
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

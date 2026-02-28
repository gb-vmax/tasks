#!/bin/bash
if [[ ! -f /home/user/data/names_reversed.txt ]]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='ecilA
boB
eilrahC'
output=$(cat /home/user/data/names_reversed.txt)
if [[ "$output" == "$expected" ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

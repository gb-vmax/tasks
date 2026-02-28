#!/bin/bash
if [ ! -f /home/user/result.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
output=$(cat /home/user/result.txt | tr -d '\n ')
if [ "$output" = "46" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

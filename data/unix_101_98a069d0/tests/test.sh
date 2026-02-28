#!/bin/bash
if [ ! -f /home/user/float_result.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
output=$(cat /home/user/float_result.txt | tr -d '\n ')
if [ "$output" = "3.33333" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

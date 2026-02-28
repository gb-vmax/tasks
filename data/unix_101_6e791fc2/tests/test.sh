#!/bin/bash
set -e
out=/home/user/data.txt.b2sum
[ -f "$out" ] || { echo 0 > /logs/verifier/reward.txt; exit; }
expected_sum="20018..." # placeholder
# Compute expected sum using b2sum for the file
actual_sum=$(cut -d' ' -f1 < "$out")
computed_sum=$(b2sum /home/user/data.txt | cut -d' ' -f1)
if [ "$actual_sum" = "$computed_sum" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/sorted_scores.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'100\n58\n42\n7'
actual=$(cat /home/user/sorted_scores.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

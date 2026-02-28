#!/bin/bash
if [ ! -f /home/user/result.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(grep -c 'apple' /home/user/result.txt)
if [ "$count" -eq 3 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

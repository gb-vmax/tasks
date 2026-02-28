#!/bin/bash
set -e
if [ ! -f /home/user/result.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected="/home/user/target1.txt"
actual=$(cat /home/user/result.txt | tr -d '\n')
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

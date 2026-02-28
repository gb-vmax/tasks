#!/bin/bash
if [ ! -f /home/user/matches.csv ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# There are three matches: Bob,Carol,David
expected=$'2,Chicago\n3,Denver\n4,Houston'
actual=$(cat /home/user/matches.csv)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

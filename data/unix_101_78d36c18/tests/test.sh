#!/bin/bash
if [ ! -f /home/user/joined.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'2 Bob Engineer\n3 Carol Doctor\n4 David Artist'
actual=$(cat /home/user/joined.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

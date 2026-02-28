#!/bin/bash
if [ ! -f /home/user/sorted_fruits.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'Apple\nBanana\nCherry\nDate'
actual=$(cat /home/user/sorted_fruits.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

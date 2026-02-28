#!/bin/bash
if [ ! -f /home/user/names.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='Alice
Bob
Charlie
David
Eve'
actual=$(cat /home/user/names.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

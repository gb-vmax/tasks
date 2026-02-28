#!/bin/bash
if [ ! -f /home/user/combined.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'A\t1\nB\t2\nC\t3'
actual=$(cat /home/user/combined.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

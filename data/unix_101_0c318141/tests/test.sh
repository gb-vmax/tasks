#!/bin/bash
if [ ! -f /home/user/seq_comma.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Check that the output is a single line, comma-separated, with zero-padded numbers
expected="10,20,30,40,50,60"
actual=$(cat /home/user/seq_comma.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

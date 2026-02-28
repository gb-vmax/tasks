#!/bin/bash
if [ ! -f /home/user/seq_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='1
2
3
4
5'
actual=$(cat /home/user/seq_output.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='Fourth line
Third line
Second line
First line'
actual=$(cat /home/user/output.txt | tr -d '\r')
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

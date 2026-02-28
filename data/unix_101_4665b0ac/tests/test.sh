#!/bin/bash
if [ ! -f /home/user/combined.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
expected='111 First line
222 Second line
333 Third line
444 Fourth line'
actual=$(cat /home/user/combined.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

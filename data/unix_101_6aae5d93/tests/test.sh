#!/bin/bash
expected='Profit up 20%'
out=$(tail -c 15 /home/user/data/report.txt)
if [ "$out" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

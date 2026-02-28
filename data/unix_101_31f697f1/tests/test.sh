#!/bin/bash
expected=$'Line 6\nLine 7\nLine 8\nLine 9\nLine 10'
out=$(tail -n 5 /home/user/logs/app.log)
if [ "$out" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

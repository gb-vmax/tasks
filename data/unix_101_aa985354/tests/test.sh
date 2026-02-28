#!/bin/bash
if [ ! -f /home/user/matches.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# All lines containing apple, banana, or cherry (case sensitive)
expected_lines=2
lines=$(wc -l < /home/user/matches.txt)
[ "$lines" -eq "$expected_lines" ] && grep -q 'apple' /home/user/matches.txt && grep -q 'banana' /home/user/matches.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt

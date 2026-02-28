#!/bin/bash
if [ ! -f /home/user/xx00 ] || [ ! -f /home/user/xx01 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected1=$'alpha\nbeta\ngamma\ndelta\n'
expected2=$'epsilon\nzeta\n'
file1=$(cat /home/user/xx00)
file2=$(cat /home/user/xx01)
if [ "$file1" = "alpha
beta
gamma
delta
" ] && [ "$file2" = "epsilon
zeta
" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

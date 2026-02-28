#!/bin/bash
expected='Name  Department    Salary
Jane  Engineering   85000
Mark  Design        76000
Sue   Marketing     68000'
actual=$(cat /home/user/people_table.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

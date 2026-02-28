#!/bin/bash
expected=$(tput -T vt100 cup)
actual=$(cat /home/user/vt100_cup.txt)
if [ "$expected" = "$actual" ] && [ -f /home/user/vt100_cup.txt ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

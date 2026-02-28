#!/bin/bash
expected="red green blue"
if [ "$(cat /home/user/colors.txt)" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/groupname.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$(id -gn user)
output=$(cat /home/user/groupname.txt)
if [ "$output" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

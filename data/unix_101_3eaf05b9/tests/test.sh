#!/bin/bash
if [ ! -f /home/user/current_user.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$(whoami)
actual=$(cat /home/user/current_user.txt | tr -d '\n')
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

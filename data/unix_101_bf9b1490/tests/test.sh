#!/bin/bash
if [ ! -f /home/user/current_dir.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$(pwd)
actual=$(cat /home/user/current_dir.txt | tr -d '\n')
if [ "$expected" = "$actual" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

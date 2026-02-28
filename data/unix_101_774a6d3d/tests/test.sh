#!/bin/bash
if [ ! -f /home/user/physical_path.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected="/home/user/original"
actual=$(cat /home/user/physical_path.txt | tr -d '\n')
if [ "$expected" = "$actual" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/yes_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$(yes | head -n 10)
actual=$(cat /home/user/yes_output.txt)
if [ "$expected" = "$actual" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

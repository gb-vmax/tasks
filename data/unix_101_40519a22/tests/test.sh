#!/bin/bash
if [ ! -f /home/user/abs_readme.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$(realpath /home/user/docs/readme.txt)
actual=$(cat /home/user/abs_readme.txt | tr -d '\n')
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

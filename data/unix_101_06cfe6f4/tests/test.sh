#!/bin/bash
if [ ! -f /home/user/output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='abcde
hijkl
opqrs'
actual=$(cat /home/user/output.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

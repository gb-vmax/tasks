#!/bin/bash
if [ ! -f /home/user/unsorted.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='apple
banana
orange
pear'
actual=$(cat /home/user/unsorted.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

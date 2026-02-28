#!/bin/bash
if [ ! -f /home/user/common.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'banana\ncherry\nfig'
actual=$(cat /home/user/common.txt)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

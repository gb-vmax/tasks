#!/bin/bash
if [ ! -f /home/user/restored.bin ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected='Hello, Unix!\n'
actual=$(cat /home/user/restored.bin)
if [ "$actual" = "Hello, Unix!" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/combined.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
expected=$'Hello world\nThis is file 2.\n'
actual=$(cat /home/user/combined.txt)
if [ "$actual" = "Hello world
This is file 2." ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

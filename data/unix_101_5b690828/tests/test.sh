#!/bin/bash
if [ ! -f /home/user/errors.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(grep -c 'error' /home/user/errors.txt)
[ "$count" -eq 2 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt

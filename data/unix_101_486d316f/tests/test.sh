#!/bin/bash
OUT=$(head -c 15 /home/user/data.log)
EXPECTED='abcdefghij12345'
if [ "$OUT" = "$EXPECTED" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/line_count.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
EXPECTED="4 /home/user/notes.txt"
ACTUAL=$(cat /home/user/line_count.txt | xargs)
if [ "$ACTUAL" = "$EXPECTED" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

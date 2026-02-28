#!/bin/bash
set -e
EXPECTED='bcde
hijk
nopq
tuvw'
if [ ! -f /home/user/col_2_to_5.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
ACTUAL=$(cat /home/user/col_2_to_5.txt)
if [ "$ACTUAL" = "$EXPECTED" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
set -e
EXPECTED='name
John
Alice
Bob'
if [ ! -f /home/user/first_column.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
ACTUAL=$(cat /home/user/first_column.txt)
if [ "$ACTUAL" = "$EXPECTED" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

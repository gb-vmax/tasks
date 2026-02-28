#!/bin/bash
expected=$'Line1
Line2	Tabbed
End'
file=/home/user/result.txt
if [ -f "$file" ] && cmp -s <(printf "%s" "$expected") "$file"; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

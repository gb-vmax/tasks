#!/bin/bash
pass=1
[ -f /home/user/part_00 ] && [ -f /home/user/part_01 ] || pass=0
cmp --silent /home/user/part_00 <(printf 'abcde') || pass=0
cmp --silent /home/user/part_01 <(printf 'fghij') || pass=0
[ -f /home/user/part_02 ] && pass=0
echo "$pass" > /logs/verifier/reward.txt

#!/bin/bash
pass=1
cmp --silent /home/user/xaa <(printf 'Alpha\nBravo\nCharlie\n') || pass=0
cmp --silent /home/user/xab <(printf 'Delta\nEcho\nFoxtrot\n') || pass=0
cmp --silent /home/user/xac <(printf 'Golf\n') || pass=0
[ -f /home/user/xad ] && pass=0
echo "$pass" > /logs/verifier/reward.txt

#!/bin/bash
if [ ! -f /home/user/apple_lines.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
count=$(grep -i -c 'apple' /home/user/fruits.txt)
output_count=$(wc -l < /home/user/apple_lines.txt)
if [ "$count" -eq "$output_count" ] && grep -qi 'apple' /home/user/apple_lines.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi

#!/bin/bash
if [ ! -f /home/user/fruits_columns.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Should have at least as many lines as input, and be wider due to columns
input_lines=$(wc -l < /home/user/fruits.txt)
output_lines=$(wc -l < /home/user/fruits_columns.txt)
[ "$output_lines" -le "$input_lines" ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# Should contain at least two fruit names on the same line
if grep -Eq "apple.*banana|banana.*cherry|cherry.*date|date.*fig|fig.*grape|grape.*kiwi" /home/user/fruits_columns.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
